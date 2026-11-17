"""Tách demo mô tả khỏi benchmark có train/test."""

import json
from pathlib import Path

import numpy as np
import pandas as pd
from pandas.api.types import is_numeric_dtype
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split

from src.generate_data import (
    CATEGORY, DEMO_RATE, NUMERIC, RATES, ROOT, SEED, TARGETS, mask_mcar, write_data,
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
    group_stats = train.groupby("group")[variable].agg(["count", "median"])
    usable = group_stats.loc[group_stats["count"].ge(min_observed), "median"]
    return test[variable].fillna(test["group"].map(usable).fillna(fallback))


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
                "corr_group_B": series.corr(frame["group"].eq("B").astype(int)),
            })
    for stage in ("Complete", "Observed", "Mode"):
        counts = stages[stage][CATEGORY].value_counts()
        for label in sorted(complete[CATEGORY].unique()):
            count = int(counts.get(label, 0))
            category_rows.append({
                "stage": stage, "category": label, "count": count, "share_nonmissing": count / counts.sum(),
            })
    return stages, pd.DataFrame(numeric_rows), pd.DataFrame(category_rows)


def result_payload(eda, missing, numeric, categories, scores):
    def records(frame):
        return json.loads(frame.to_json(orient="records", double_precision=12))

    return {
        "n_rows": int(missing["total"].iloc[0]), "demo_rate": DEMO_RATE,
        "mask_seeds": list(MASK_SEEDS), "rates": list(RATES),
        "eda": records(eda.reset_index()), "missing": records(missing.reset_index()),
        "numeric": records(numeric), "categories": records(categories), "scores": records(scores),
    }


def write_conclusions(path, payload):
    scores = pd.DataFrame(payload["scores"])
    demo = pd.DataFrame(payload["numeric"]).set_index(["variable", "stage"])
    cats = pd.DataFrame(payload["categories"]).set_index(["category", "stage"])
    eda = pd.DataFrame(payload["eda"]).set_index("variable")
    selected = scores[scores["missing_rate"].eq(DEMO_RATE)].set_index(["variable", "method", "metric"])

    def score(var, method, metric):
        row = selected.loc[(var, method, metric)]
        factor = 100 if metric == "Accuracy" else 1
        suffix = "%" if metric == "Accuracy" else ""
        return f"{factor * row['mean']:.2f} ± {factor * row['std']:.2f}{suffix}"

    sym, skew, multi = NUMERIC
    lines = [
        "# Kết luận từ thực nghiệm DS111", "",
        f"Dữ liệu mô phỏng gồm {payload['n_rows']:,} dòng. Chia train/test 75/25, giữ nguyên lần chia.",
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
        f"- **Gần đối xứng:** skewness {eda.loc[sym, 'skewness']:.2f}, "
        f"Mean {eda.loc[sym, 'mean']:.2f} và Median {eda.loc[sym, 'median']:.2f}, "
        f"{eda.loc[sym, 'iqr_flag_count']:.0f} điểm bị gắn cờ theo 1,5 IQR. "
        "Hai giá trị điền gần nhau nên sai số chênh ít trong benchmark này.",
        f"- **Lệch phải:** skewness {eda.loc[skew, 'skewness']:.2f}, "
        f"Mean {eda.loc[skew, 'mean']:.2f} và Median {eda.loc[skew, 'median']:.2f}, "
        f"{eda.loc[skew, 'iqr_flag_count']:.0f} điểm bị gắn cờ. "
        "Ở mức 15%, Median giảm MAE còn Mean giảm RMSE. Với một hằng số, "
        "trung vị tối thiểu hóa tổng sai số tuyệt đối và trung bình tối thiểu hóa tổng bình phương sai số trên tập dùng để tối ưu. "
        "Thứ hạng trên test còn phụ thuộc vào mức đại diện của train.",
        f"- **Biến loại:** Accuracy của Mode đạt {score(CATEGORY, 'Mode', 'Accuracy')}. "
        f"Tỷ trọng M trong các giá trị có mặt tăng từ {cats.loc[('M', 'Observed'), 'share_nonmissing']:.1%} "
        f"lên {cats.loc[('M', 'Mode'), 'share_nonmissing']:.1%} trong demo EDA. "
        "Mọi ô che đều nhận M, nên accuracy bằng tỷ lệ M thật trong các ô che và tỷ lệ khôi phục của các lớp còn lại bằng 0 khi có mặt.",
        f"- **Phân phối:** SD mẫu cột lệch từ {demo.loc[(skew, 'Observed'), 'std']:.2f} "
        f"xuống {demo.loc[(skew, 'Mean'), 'std']:.2f} khi điền Mean trong cùng demo. "
        f"Điền Mean toàn cục cho cột hai cụm làm tương quan Pearson với chỉ báo nhóm B "
        f"đổi từ {demo.loc[(multi, 'Observed'), 'corr_group_B']:.3f} "
        f"xuống {demo.loc[(multi, 'Mean'), 'corr_group_B']:.3f}. "
        "Điền Median cũng tạo một đỉnh nhân tạo. Với hằng số khác Mean quan sát, thay đổi phương sai phụ thuộc vào vị trí hằng số.",
        f"- **Mở rộng theo nhóm:** MAE của Median toàn cục là {score(multi, 'Median', 'MAE')}, "
        f"Median theo nhóm là {score(multi, 'Group Median', 'MAE')}. "
        "Nhóm A/B mang thông tin theo cách sinh dữ liệu. Cần kiểm tra nhóm có sẵn lúc sử dụng và đủ quan sát, "
        "vì benchmark này dùng fallback Median train toàn cục cho nhóm hiếm hoặc chưa gặp.",
        "",
        "Các kết quả giới hạn ở bộ sinh dữ liệu, lần chia và cơ chế MCAR này. Tiêu chí sai số từng ô, "
        "bảo toàn phân phối marginal và bảo toàn quan hệ giữa biến cần được kiểm tra riêng.",
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
    payload = result_payload(eda, missing, numeric, categories, scores)
    (out / "evidence.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    write_conclusions(out / "conclusions.md", payload)
    create_figures(root / "figures", stages, scores)
    return payload


if __name__ == "__main__":
    run()
