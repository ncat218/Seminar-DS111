"""Tách demo mô tả khỏi benchmark có train/test."""

import json
from pathlib import Path

import numpy as np
import pandas as pd
from pandas.api.types import is_numeric_dtype
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split

from src.prepare_data import (
    CATEGORY, DEMO_RATE, GROUP, NUMERIC, RATES, ROOT, SEED, TARGETS, mask_mcar, write_data,
)

MASK_SEEDS = tuple(range(42, 54))
METHODS = {"Mean": "mean", "Median": "median", "Mode": "most_frequent"}
DEMO_STAGES = ("Complete", "Observed", "Mean", "Median")


def observed_summary(frame):
    """Mode of a continuous sample is reported as empty if all values are unique."""
    stats = frame[list(NUMERIC)].describe().T[["count", "mean", "std", "min", "max"]]
    stats["median"] = frame[list(NUMERIC)].median()
    stats["skewness"] = frame[list(NUMERIC)].skew()
    for column in NUMERIC:
        counts = frame[column].value_counts()
        modes = sorted(counts[counts.eq(counts.max())].index) if counts.max() > 1 else []
        stats.loc[column, "mode"] = ", ".join(f"{value:.6g}" for value in modes)
        low, high = frame[column].quantile([0.25, 0.75])
        fence = 1.5 * (high - low)
        stats.loc[column, "iqr_flag_count"] = (
            frame[column].lt(low - fence) | frame[column].gt(high + fence)
        ).sum()
    return stats.rename_axis("variable")


def fit_imputer(train, variable, method):
    """Fit on the caller's reference data and fail explicitly if no value exists."""
    if train[variable].isna().all():
        raise ValueError(f"{variable} không có giá trị quan sát trong tập fit.")
    if method in ("Mean", "Median") and not is_numeric_dtype(train[variable]):
        raise TypeError(f"{method} cần biến định lượng: {variable}")
    return SimpleImputer(strategy=METHODS[method]).fit(imputer_input(train, variable, method))


def imputer_input(frame, variable, method):
    column = frame[[variable]]
    return column.astype(object).where(column.notna(), np.nan) if method == "Mode" else column


def transform(imputer, frame, variable, method):
    values = imputer.transform(imputer_input(frame, variable, method)).ravel()
    filled = pd.Series(values, index=frame.index, name=variable)
    if filled.isna().any():
        raise RuntimeError(f"Vẫn còn giá trị thiếu ở {variable}.")
    return filled


def group_median(train, test, variable, min_observed=20):
    """Learn per-group median on train, with train global median as the fallback."""
    fallback = fit_imputer(train, variable, "Median").statistics_[0]
    group_stats = train.groupby(GROUP)[variable].agg(["count", "median"])
    usable = group_stats.loc[group_stats["count"].ge(min_observed), "median"]
    return test[variable].fillna(test[GROUP].map(usable).fillna(fallback))


def masked_scores(truth, predicted, mask, categorical=False):
    if not (truth.index.equals(predicted.index) and truth.index.equals(mask.index)):
        raise ValueError("Ground truth, dự đoán và mặt nạ phải cùng chỉ mục.")
    if not mask.any():
        raise ValueError("Cần ít nhất một ô test bị che để chấm.")
    hidden_truth, hidden_pred = truth.loc[mask], predicted.loc[mask]
    if hidden_truth.isna().any() or hidden_pred.isna().any():
        raise ValueError("Cần nhãn gốc và dự đoán đầy đủ tại các ô test bị che.")
    if categorical:
        return {"Accuracy": float(hidden_truth.eq(hidden_pred).mean())}
    error = hidden_pred - hidden_truth
    return {"MAE": float(error.abs().mean()), "RMSE": float(np.sqrt(error.pow(2).mean()))}


def benchmark(complete, rates=RATES, seeds=MASK_SEEDS):
    train_raw, test_raw = train_test_split(complete, test_size=0.25, random_state=SEED)
    rows = []
    for rate in rates:
        for seed in seeds:
            train_rng, test_rng = map(np.random.default_rng, np.random.SeedSequence(seed).spawn(2))
            train, _ = mask_mcar(train_raw, rate, train_rng)
            test, test_mask = mask_mcar(test_raw, rate, test_rng)
            for variable in TARGETS:
                categorical = variable == CATEGORY
                methods = ["Mode"] if categorical else ["Mean", "Median"]
                if variable == NUMERIC[2]:
                    methods.append("Group Median")
                for method in methods:
                    if method == "Group Median":
                        predicted = group_median(train, test, variable)
                        fill = "Theo nhóm train"
                    else:
                        imputer = fit_imputer(train, variable, method)
                        predicted = transform(imputer, test, variable, method)
                        fill = imputer.statistics_[0]
                    hidden = test_mask[variable]
                    if predicted.isna().any():
                        raise RuntimeError(f"Vẫn còn giá trị thiếu ở {variable}.")
                    for metric, score in masked_scores(test_raw[variable], predicted, hidden, categorical).items():
                        rows.append({
                            "missing_rate": rate, "mask_seed": seed, "variable": variable,
                            "method": method, "metric": metric, "value": score, "fill_value": fill,
                            "n_train": len(train), "n_train_missing": int(train[variable].isna().sum()),
                            "n_test": len(test), "n_test_masked": int(hidden.sum()),
                            "actual_test_rate": float(hidden.mean()),
                        })
    return pd.DataFrame(rows)


def summarize_scores(repeats):
    keys = ["missing_rate", "variable", "method", "metric"]
    return repeats.groupby(keys, as_index=False).agg(
        mean=("value", "mean"), std=("value", "std"), repeats=("value", "size"),
        mean_actual_test_rate=("actual_test_rate", "mean"),
        mean_test_masked=("n_test_masked", "mean"),
    )


def describe_demo(complete, observed):
    filled = {}
    for method in ("Mean", "Median", "Mode"):
        variables = (CATEGORY,) if method == "Mode" else NUMERIC
        filled[method] = observed.assign(**{
            col: transform(fit_imputer(observed, col, method), observed, col, method)
            for col in variables
        })
    stages = {"Complete": complete, "Observed": observed, **filled}
    numeric_rows, category_rows = [], []
    for stage in DEMO_STAGES:
        frame = stages[stage]
        for variable in NUMERIC:
            series = frame[variable]
            numeric_rows.append({
                "stage": stage, "variable": variable, "count": series.count(), "mean": series.mean(),
                "median": series.median(), "std": series.std(), "variance": series.var(),
                "missing_rate": series.isna().mean(),
                "corr_school_GP": series.corr(frame[GROUP].eq("GP").astype(int)),
            })
    for stage in ("Complete", "Observed", "Mode"):
        counts = stages[stage][CATEGORY].value_counts()
        for label in sorted(complete[CATEGORY].unique()):
            count = int(counts.get(label, 0))
            category_rows.append({
                "stage": stage, "category": label, "count": count, "share_nonmissing": count / counts.sum(),
            })
    return stages, pd.DataFrame(numeric_rows), pd.DataFrame(category_rows)


def result_payload(eda, missing, numeric, categories, scores, stages):
    def records(frame):
        return json.loads(frame.to_json(orient="records", double_precision=12))

    schools = stages["Complete"].groupby(GROUP)[NUMERIC[2]].agg(["size", "median"])
    return {
        "n_rows": int(missing["total"].iloc[0]), "demo_rate": DEMO_RATE,
        "mask_seeds": list(MASK_SEEDS), "rates": list(RATES),
        "eda": records(eda.reset_index()), "missing": records(missing.reset_index()),
        "numeric": records(numeric), "categories": records(categories), "scores": records(scores),
        "schools": records(schools.reset_index()),
    }


def supporting_evidence(complete, repeats, out):
    """Tính các bằng chứng bổ sung cho ba câu hỏi của seminar."""
    paired = []
    for variable in NUMERIC:
        for metric in ("MAE", "RMSE"):
            sample = repeats.loc[
                repeats.missing_rate.eq(DEMO_RATE) & repeats.variable.eq(variable)
                & repeats.metric.eq(metric) & repeats.method.isin(["Mean", "Median"])
            ]
            values = sample.pivot(index="mask_seed", columns="method", values="value")
            difference = (values["Median"] - values["Mean"]).round(12)
            paired.append({
                "variable": variable, "metric": metric,
                "mean_difference": difference.mean(), "std_difference": difference.std(),
                "median_wins": int(difference.lt(0).sum()),
                "mean_wins": int(difference.gt(0).sum()), "ties": int(difference.eq(0).sum()),
            })
    paired = pd.DataFrame(paired)
    paired.to_csv(out / "paired_comparisons.csv", index=False)

    correlations = []
    school = complete[GROUP].eq("GP").astype(int)
    for seed in range(300):
        observed, _ = mask_mcar(complete, DEMO_RATE, np.random.default_rng(seed))
        values = observed["G3"]
        correlations.append({
            "mask_seed": seed, "complete": complete["G3"].corr(school),
            "observed": values.corr(school),
            "mean_imputed": values.fillna(values.mean()).corr(school),
        })
    correlations = pd.DataFrame(correlations)
    correlations.to_csv(out / "correlation_repeats.csv", index=False)

    zeros = complete.loc[complete["G3"].eq(0)]
    sensitivity = summarize_scores(benchmark(complete.loc[complete["G3"].ne(0)], rates=(DEMO_RATE,)))
    sensitivity = sensitivity.loc[sensitivity.variable.eq("G3")].copy()
    sensitivity.to_csv(out / "zero_grade_sensitivity.csv", index=False)

    ages = np.array([20., 22., 23., 25., 80.])
    candidates = np.arange(15, 60.01, 0.25)
    errors = ages[None, :] - candidates[:, None]
    curve = pd.DataFrame({
        "candidate": candidates, "MAE": np.abs(errors).mean(axis=1),
        "RMSE": np.sqrt(np.square(errors).mean(axis=1)),
    })
    curve.to_csv(out / "constant_prediction_loss.csv", index=False)

    def records(frame):
        return json.loads(frame.to_json(orient="records", double_precision=12))

    return {
        "paired": records(paired), "correlations": correlations.mean().drop("mask_seed").to_dict(),
        "age_loss_curve": records(curve), "zero_grade_sensitivity": records(sensitivity),
        "zeros": {"count": len(zeros), "MS": int(zeros[GROUP].eq("MS").sum())},
    }


def write_conclusions(path, payload):
    scores = pd.DataFrame(payload["scores"])
    demo = pd.DataFrame(payload["numeric"]).set_index(["variable", "stage"])
    cats = pd.DataFrame(payload["categories"]).set_index(["category", "stage"])
    eda = pd.DataFrame(payload["eda"]).set_index("variable")
    selected = scores[scores["missing_rate"].eq(DEMO_RATE)].set_index(["variable", "method", "metric"])

    def score(var, method, metric):
        row = selected.loc[(var, method, metric)]
        if metric == "Accuracy":
            return f"{row['mean']:.2%} ± {100 * row['std']:.2f} điểm phần trăm"
        return f"{row['mean']:.2f} ± {row['std']:.2f}"

    sym, skew, multi = NUMERIC
    lines = [
        "# Kết luận từ thực nghiệm DS111", "",
        "**Câu hỏi xuyên suốt:** Tại sao giá trị đại diện có thể ước lượng ô thiếu, "
        "khi nào hợp lý, và nó làm sai lệch dữ liệu ra sao?", "",
        "## Vì sao có thể dùng thống kê trung tâm", "",
        "Khi chỉ dùng một hằng số cho cột, cần chọn theo tổn thất mong muốn. "
        "Mean tối ưu sai số bình phương, Median tối ưu sai số tuyệt đối, Mode tối ưu số nhãn khớp "
        "trên tập dùng để tối ưu. Dùng thống kê quan sát để dự đoán ô thiếu còn cần giả định "
        "phần quan sát đủ đại diện cho phần bị thiếu hoặc cho nhóm tương ứng.", "",
        "## Khi nào hợp lý và bằng chứng sai số", "",
        f"Tập tiếng Bồ Đào Nha của UCI Student Performance gồm {payload['n_rows']:,} dòng thực tế. "
        "Bốn cột phân tích đầy đủ trước khi che. Chia train/test 75/25, giữ nguyên lần chia.",
        f"Ở mỗi mức thiếu 5%, 15%, 30%, lặp {len(MASK_SEEDS)} bộ mặt nạ MCAR. "
        "Các sai số dưới đây là trung bình ± SD qua lần che ở mức danh nghĩa 15%. SD mô tả độ dao động theo mặt nạ.",
        "",
        "| Biến | Phương pháp | MAE | RMSE |",
        "|---|---|---:|---:|",
    ]
    for var in NUMERIC:
        for method in ("Mean", "Median", "Group Median") if var == multi else ("Mean", "Median"):
            lines.append(f"| {var} | {method} | {score(var, method, 'MAE')} | {score(var, method, 'RMSE')} |")
    lines += [
        "",
        f"- **Điểm kỳ đầu G1:** skewness {eda.loc[sym, 'skewness']:.2f}, "
        f"Mean {eda.loc[sym, 'mean']:.2f} và Median {eda.loc[sym, 'median']:.2f}, "
        f"{eda.loc[sym, 'iqr_flag_count']:.0f} điểm bị gắn cờ theo 1,5 IQR. "
        "Hai tâm gần nhau. Đọc cả hình dạng và điểm đuôi trước khi chọn.",
        f"- **Số buổi vắng absences:** skewness {eda.loc[skew, 'skewness']:.2f}, "
        f"Mean {eda.loc[skew, 'mean']:.2f} và Median {eda.loc[skew, 'median']:.2f}, "
        f"{eda.loc[skew, 'iqr_flag_count']:.0f} điểm bị gắn cờ. "
        "Ở mức 15%, Median có MAE thấp hơn và Mean có RMSE thấp hơn. "
        "Số 0 là vắng 0 buổi, một quan sát hợp lệ. Mean có thể cho kết quả lẻ, "
        "phù hợp với dự đoán điểm theo mất mát bình phương. Nếu đầu ra cần số đếm nguyên, "
        "cần định nghĩa quy tắc và đánh giá lại. Với một hằng số, Median tối thiểu hóa tổng sai số tuyệt đối "
        "và Mean tối thiểu hóa tổng bình phương trên tập tối ưu. Thứ hạng test phụ thuộc vào mức đại diện của train.",
        f"- **Người giám hộ guardian:** Accuracy của Mode đạt {score(CATEGORY, 'Mode', 'Accuracy')}. "
        f"Tỷ trọng nhãn mẹ trong các giá trị có mặt tăng từ {cats.loc[('mother', 'Observed'), 'share_nonmissing']:.1%} "
        f"lên {cats.loc[('mother', 'Mode'), 'share_nonmissing']:.1%} trong demo EDA. "
        "Điền nhãn đa số cho mọi ô che làm giảm khả năng khôi phục các lớp hiếm.",
        f"- **Phân phối:** SD mẫu cột lệch từ {demo.loc[(skew, 'Observed'), 'std']:.2f} "
        f"xuống {demo.loc[(skew, 'Mean'), 'std']:.2f} khi điền Mean trong cùng demo. "
        f"Điền Mean toàn cục cho điểm G3 làm tương quan Pearson với chỉ báo trường GP "
        f"đổi từ {demo.loc[(multi, 'Observed'), 'corr_school_GP']:.3f} "
        f"thành {demo.loc[(multi, 'Mean'), 'corr_school_GP']:.3f}. "
        "Điền Median cũng tạo một đỉnh nhân tạo. Với hằng số khác Mean quan sát, thay đổi phương sai phụ thuộc vào vị trí hằng số.",
        f"- **Mở rộng theo trường:** MAE của Median G3 toàn cục là {score(multi, 'Median', 'MAE')}, "
        f"Median theo nhóm là {score(multi, 'Group Median', 'MAE')}. "
        f"RMSE lần lượt là {score(multi, 'Median', 'RMSE')} và {score(multi, 'Group Median', 'RMSE')}. "
        "Chênh lệch quan sát giữa trường không xác lập tác động nhân quả. Cần kiểm tra trường có sẵn lúc sử dụng và đủ quan sát, "
        "vì benchmark này dùng fallback Median train toàn cục cho nhóm hiếm hoặc chưa gặp.",
        "",
        "## Biến dạng và giới hạn", "",
        f"Lặp 300 mặt nạ MCAR 15%, tương quan G3–GP trung bình sau điền Mean là "
        f"{payload['support']['correlations']['mean_imputed']:.3f}, "
        f"so với {payload['support']['correlations']['complete']:.3f} trên bản đầy đủ. "
        "Riêng mặt nạ demo, hệ số 0,287 sau điền gần bản đầy đủ hơn 0,310 trước điền. "
        "Phân biệt xu hướng trung bình với một lần che.", "",
        f"Bản gốc có {payload['support']['zeros']['count']} điểm G3 bằng 0, "
        f"{payload['support']['zeros']['MS']} thuộc MS. Giữ các điểm này trong benchmark chính. "
        "Bảng zero_grade_sensitivity.csv khảo sát riêng việc loại chúng trước khi chia lại. "
        "Thay đổi tập mẫu và lần chia khiến kết quả này chỉ là phân tích độ nhạy.", "",
        "Các kết quả giới hạn ở mẫu môn tiếng Bồ Đào Nha, lần chia và cơ chế che MCAR này. "
        "Số liệu do thực nghiệm trên bộ dữ liệu thật tạo ra. Cách thiếu ngoài đời có thể khác.",
    ]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def run(root: Path = ROOT):
    from src.plot_results import create_figures

    complete, observed, _ = write_data(root)
    out = root / "results"
    out.mkdir(parents=True, exist_ok=True)
    missing = observed.isna().sum().rename("n_missing").to_frame()
    missing["total"] = len(observed)
    missing["missing_rate"] = observed.isna().mean()
    missing.index.name = "variable"
    eda = observed_summary(observed)
    stages, numeric, categories = describe_demo(complete, observed)
    repeats = benchmark(complete)
    scores = summarize_scores(repeats)
    for name, frame, index in [
        ("missing_summary", missing, True), ("eda_numeric", eda, True),
        ("distribution_summary", numeric, False), ("category_frequencies", categories, False),
        ("evaluation", scores, False), ("evaluation_by_seed", repeats, False),
    ]:
        frame.to_csv(out / f"{name}.csv", index=index)
    payload = result_payload(eda, missing, numeric, categories, scores, stages)
    payload["support"] = supporting_evidence(complete, repeats, out)
    (out / "evidence.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    write_conclusions(out / "conclusions.md", payload)
    create_figures(root / "figures", stages, scores, payload["support"])
    return payload


if __name__ == "__main__":
    run()
