"""Đánh giá ảnh hưởng của điền khuyết đến mô hình dự đoán điểm G3."""

import json
import sys
from importlib.metadata import version
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.prepare_data import ROOT, RATES

NUMERIC_FEATURES = ("G1", "G2", "age", "absences")
CATEGORICAL_FEATURES = ("guardian", "school")
FEATURES = (*NUMERIC_FEATURES, *CATEGORICAL_FEATURES)
TARGET = "G3"
SPLIT_SEEDS = (42, 43, 44, 45, 46)
MASK_SEEDS = (42, 43, 44, 45)
STRATEGIES = {"Mean": "mean", "Median": "median", "Mode": "most_frequent"}
MODELS = ("Ridge", "Random Forest")


def load_model_data(root=ROOT):
    frame = pd.read_csv(root / "data/raw/student-por.csv", sep=";").rename_axis("row_id")
    if frame[[*FEATURES, TARGET]].isna().any().any():
        raise ValueError("Cần dữ liệu gốc đầy đủ để tạo thí nghiệm che.")
    return frame[list(FEATURES)], frame[TARGET]


def mask_features(frame, rate, rng):
    if not 0 <= rate <= 1:
        raise ValueError("Tỷ lệ thiếu phải thuộc [0, 1].")
    mask = pd.DataFrame(rng.random(frame.shape) < rate, index=frame.index, columns=frame.columns)
    masked = frame.mask(mask)
    for column in CATEGORICAL_FEATURES:
        masked[column] = masked[column].astype(object).where(masked[column].notna(), np.nan)
    return masked, mask


def build_pipeline(method, model):
    numeric_steps = [("imputer", SimpleImputer(strategy=STRATEGIES[method]))]
    if model == "Ridge":
        numeric_steps.append(("scale", StandardScaler()))
    numeric = Pipeline(numeric_steps)
    categorical = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encode", OneHotEncoder(handle_unknown="ignore", sparse_output=False)),
    ])
    preprocessing = ColumnTransformer([
        ("numeric", numeric, list(NUMERIC_FEATURES)),
        ("categorical", categorical, list(CATEGORICAL_FEATURES)),
    ])
    estimators = {
        "Ridge": Ridge(alpha=1.0),
        "Random Forest": RandomForestRegressor(
            n_estimators=100, min_samples_leaf=3, random_state=42, n_jobs=1,
        ),
    }
    return Pipeline([("preprocess", preprocessing), ("model", estimators[model])])


def regression_scores(truth, prediction):
    return {
        "MAE": float(mean_absolute_error(truth, prediction)),
        "RMSE": float(np.sqrt(mean_squared_error(truth, prediction))),
        "R2": float(r2_score(truth, prediction)),
    }


def metric_rows(truth, prediction, row_missing, reference_prediction, metadata):
    rows = []
    subsets = {
        "All test": np.ones(len(truth), dtype=bool),
        "Missing input": row_missing.to_numpy(),
        "Complete input": ~row_missing.to_numpy(),
    }
    for name, selected in subsets.items():
        if selected.sum() < 2:
            continue
        metrics = regression_scores(truth.to_numpy()[selected], prediction[selected])
        metrics["Prediction shift"] = float(np.abs(prediction[selected] - reference_prediction[selected]).mean())
        rows.extend({
            **metadata, "subset": name, "metric": metric, "value": value,
            "n_scored": int(selected.sum()),
        } for metric, value in metrics.items())
    return rows


def run(root: Path = ROOT, rates=RATES, split_seeds=SPLIT_SEEDS, mask_seeds=MASK_SEEDS):
    X, y = load_model_data(root)
    X.join(y).to_csv(root / "data/student_model_complete.csv", index=True)
    destination = root / "results"
    destination.mkdir(parents=True, exist_ok=True)
    runtime = {"python": sys.version, "packages": {
        name: version(name) for name in ("numpy", "pandas", "scipy", "matplotlib", "scikit-learn", "Pillow")
    }}
    (destination / "runtime_versions.json").write_text(
        json.dumps(runtime, ensure_ascii=False, indent=2), encoding="utf-8",
    )
    scores, predictions, references, assignments, coefficients = [], [], [], [], []
    fit_count = 0
    for split_seed in split_seeds:
        train_ids, test_ids = train_test_split(X.index, test_size=.25, random_state=split_seed)
        X_train, X_test = X.loc[train_ids], X.loc[test_ids]
        y_train, y_test = y.loc[train_ids], y.loc[test_ids]
        assignments.extend({"split_seed": split_seed, "row_id": int(row), "set": label}
                           for label, ids in (("train", train_ids), ("test", test_ids)) for row in ids)
        reference_predictions = {}
        for model in MODELS:
            fitted = build_pipeline("Mean", model).fit(X_train, y_train)
            fit_count += 1
            prediction = fitted.predict(X_test)
            reference_predictions[model] = prediction
            references.extend({
                "split_seed": split_seed, "model": model, "metric": metric, "value": value,
                "n_train": len(train_ids), "n_test": len(test_ids),
            } for metric, value in regression_scores(y_test, prediction).items())
            if split_seed == 42 and model == "Ridge":
                coefficients.extend({
                    "method": "Complete reference", "feature": feature, "coefficient": float(value),
                } for feature, value in zip(
                    fitted["preprocess"].get_feature_names_out(), fitted["model"].coef_,
                ))
        dummy_prediction = np.repeat(y_train.mean(), len(y_test))
        references.extend({
            "split_seed": split_seed, "model": "Predict train mean", "metric": metric,
            "value": value, "n_train": len(train_ids), "n_test": len(test_ids),
        } for metric, value in regression_scores(y_test, dummy_prediction).items())

        for rate in rates:
            for mask_seed in mask_seeds:
                child_seeds = np.random.SeedSequence([split_seed, mask_seed]).spawn(2)
                train, train_mask = mask_features(X_train, rate, np.random.default_rng(child_seeds[0]))
                test, test_mask = mask_features(X_test, rate, np.random.default_rng(child_seeds[1]))
                if split_seed == 42 and mask_seed == 42 and rate == .15:
                    example = pd.concat([train.assign(set="train"), test.assign(set="test")])
                    example.join(y).to_csv(root / "data/student_model_missing_15pct.csv", index=True)
                    example_mask = pd.concat([
                        train_mask.assign(set="train"), test_mask.assign(set="test"),
                    ])
                    example_mask.to_csv(root / "data/student_model_mask_15pct.csv", index=True)
                if train.isna().all().any():
                    raise ValueError("Có cột train toàn thiếu, cần quy tắc nghiệp vụ hoặc thêm dữ liệu.")
                missing_rows = test_mask.any(axis=1)
                for method in STRATEGIES:
                    for model in MODELS:
                        fitted = build_pipeline(method, model).fit(train, y_train)
                        fit_count += 1
                        for phase, test_input in (("Masked train, clean test", X_test),
                                                  ("Masked train, masked test", test)):
                            prediction = fitted.predict(test_input)
                            metadata = {
                                "split_seed": split_seed, "mask_seed": mask_seed,
                                "missing_rate": rate, "method": method, "model": model, "phase": phase,
                                "n_train": len(train), "n_test": len(test),
                                "train_missing_rate": float(train_mask.to_numpy().mean()),
                                "test_missing_rate": float(test_mask.to_numpy().mean()),
                            }
                            scores.extend(metric_rows(
                                y_test, prediction, missing_rows, reference_predictions[model], metadata,
                            ))
                            predictions.extend({
                                **metadata, "row_id": int(row), "true_G3": float(truth),
                                "prediction": float(pred), "complete_reference_prediction": float(reference),
                                "row_missing": bool(missing),
                            } for row, truth, pred, reference, missing in zip(
                                test.index, y_test, prediction, reference_predictions[model], missing_rows,
                            ))
                        if split_seed == 42 and mask_seed == 42 and rate == .15 and model == "Ridge":
                            coefficients.extend({
                                "method": method, "feature": feature, "coefficient": float(value),
                            } for feature, value in zip(
                                fitted["preprocess"].get_feature_names_out(), fitted["model"].coef_,
                            ))
    by_run = pd.DataFrame(scores)
    keys = ["missing_rate", "method", "model", "phase", "subset", "metric"]
    summary = by_run.groupby(keys, as_index=False).agg(
        mean=("value", "mean"), std=("value", "std"), runs=("value", "size"),
        mean_n_scored=("n_scored", "mean"),
    )
    reference_by_split = pd.DataFrame(references)
    reference_summary = reference_by_split.groupby(["model", "metric"], as_index=False).agg(
        mean=("value", "mean"), std=("value", "std"), splits=("value", "size"),
    )
    for name, table in (
        ("model_evaluation_by_run", by_run), ("model_evaluation", summary),
        ("model_predictions", pd.DataFrame(predictions)),
        ("model_reference_by_split", reference_by_split), ("model_reference", reference_summary),
        ("model_coefficients", pd.DataFrame(coefficients)), ("model_split_assignments", pd.DataFrame(assignments)),
    ):
        table.to_csv(destination / f"{name}.csv", index=False)
    manifest = {
        "target": TARGET, "numeric_features": list(NUMERIC_FEATURES),
        "categorical_features": list(CATEGORICAL_FEATURES),
        "split_seeds": list(split_seeds), "mask_seeds": list(mask_seeds), "rates": list(rates),
        "n_rows": len(X), "n_test": 163, "fits": fit_count,
        "model_settings": {"Ridge": {"alpha": 1.0},
                           "Random Forest": {"n_estimators": 100, "min_samples_leaf": 3, "random_state": 42}},
        "scope": "Dự đoán G3 sau khi có G1/G2. Không mô phỏng dự báo trước năm học.",
        "evaluation": json.loads(summary.to_json(orient="records", double_precision=12)),
        "reference": json.loads(reference_summary.to_json(orient="records", double_precision=12)),
    }
    (destination / "model_evidence.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    write_report(destination, manifest)
    create_model_figures(root / "figures", summary, reference_summary, pd.DataFrame(predictions))
    return manifest


def write_report(destination, evidence):
    rows = pd.DataFrame(evidence["evaluation"])
    focus = rows.loc[rows.missing_rate.eq(.15) & rows.phase.eq("Masked train, masked test")
                     & rows.subset.eq("All test")]
    reference = pd.DataFrame(evidence["reference"]).set_index(["model", "metric"])
    lines = [
        "# Điền khuyết ảnh hưởng mô hình dự đoán G3 thế nào?", "",
        "Đích là điểm cuối kỳ G3. Đầu vào gồm G1, G2, age, absences, guardian và school. "
        "G3 luôn được giữ đầy đủ. Bối cảnh dự đoán là sau khi đã có điểm G1/G2.", "",
        f"Thiết kế gồm {len(evidence['split_seeds'])} lần chia 75/25 × "
        f"{len(evidence['mask_seeds'])} mặt nạ tại mỗi mức thiếu. "
        "Mỗi phương pháp dùng cùng hàng và mặt nạ. Học imputer, mã hóa, chuẩn hóa và mô hình chỉ từ train. "
        "Giữ siêu tham số cố định trước khi chấm test.", "",
        "Biến số so Mean, Median, Mode. Biến loại dùng Mode ở cả ba phương án. "
        "Các biến số là điểm, tuổi và số buổi vắng dạng rời rạc, nên Mode là baseline có ý nghĩa. "
        "Kết quả chính chấm mọi dòng test bằng nhãn G3 thật.", "",
        "## Mốc dùng đầu vào đầy đủ", "",
        "| Mô hình | MAE | RMSE | R² |", "|---|---:|---:|---:|",
    ]
    for model in (*MODELS, "Predict train mean"):
        values = [reference.loc[(model, metric), "mean"] for metric in ("MAE", "RMSE", "R2")]
        lines.append(f"| {model} | {values[0]:.3f} | {values[1]:.3f} | {values[2]:.3f} |")
    lines += ["", "## Cả train và test có đầu vào thiếu 15%", "",
              "| Mô hình | Điền biến số | MAE | RMSE | R² | ΔRMSE so đầu vào đầy đủ |",
              "|---|---|---:|---:|---:|---:|"]
    for model in MODELS:
        for method in STRATEGIES:
            selected = focus.loc[focus.model.eq(model) & focus.method.eq(method)].set_index("metric")
            mae, rmse, r2 = [selected.loc[metric, "mean"] for metric in ("MAE", "RMSE", "R2")]
            delta = rmse - reference.loc[(model, "RMSE"), "mean"]
            lines.append(f"| {model} | {method} | {mae:.3f} | {rmse:.3f} | {r2:.3f} | {delta:+.3f} |")
    lines += [
        "", "## Cách diễn giải", "",
        "Bảng model_evaluation.csv có đủ 5%, 15%, 30%, hai pha và ba tập dòng test. "
        "Pha train thiếu/test đầy đủ khảo sát mô hình học từ đầu vào đã điền. "
        "Pha cả hai thiếu thêm ảnh hưởng của đầu vào mất thông tin lúc áp dụng. "
        "Cùng mô hình đã fit được dùng để dự đoán hai pha, nên khác biệt pha không đến từ việc huấn luyện lại.", "",
        "Trong CSV, row_missing và các nhóm Missing input / Complete input được xác định bằng mặt nạ test. "
        "Ở pha clean test, chúng vẫn chỉ cùng các hàng của mặt nạ đối chiếu để so sánh theo cặp; "
        "đầu vào thực tế ở pha này đầy đủ. All test luôn gồm mọi dòng test.", "",
        "Prediction shift là trung bình độ lệch tuyệt đối giữa dự đoán hiện tại và dự đoán từ mô hình "
        "học/áp dụng trên đầu vào đầy đủ, ghép đúng split và row_id. Nó đo độ thay đổi dự đoán, "
        "còn MAE/RMSE/R² đo độ đúng với G3 thật.", "",
        "SD mô tả dao động của 20 tổ hợp chia/che trên cùng dataset. "
        "Các tập test chồng lấn giữa lần chia, nên không xem chúng như 20 mẫu học sinh độc lập. "
        "Mốc đầu vào đầy đủ là điểm tham chiếu của từng mô hình, không bảo đảm là cận trên hiệu năng. "
        "Không điều chỉnh siêu tham số theo các điểm test đã báo.", "",
        "Sai số khôi phục một đặc trưng và sai số dự đoán G3 có hai hàm mục tiêu khác nhau. "
        "Lựa chọn tốt cần được kiểm chứng bằng chỉ tiêu của tác vụ cuối cùng. "
        "Các kết quả giới hạn ở hai mô hình, sáu biến, MCAR và bộ Student Performance này.",
    ]
    (destination / "model_conclusions.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def create_model_figures(out, summary, reference, predictions):
    from src.plot_results import AMBER, TEAL, VIOLET, INK, save, plt

    out.mkdir(parents=True, exist_ok=True)
    focus = summary.loc[summary.phase.eq("Masked train, masked test")
                        & summary.subset.eq("All test") & summary.metric.eq("RMSE")]
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.6), layout="constrained")
    for model, ax in zip(MODELS, axes):
        for method, color in zip(STRATEGIES, (AMBER, TEAL, VIOLET)):
            data = focus.loc[focus.model.eq(model) & focus.method.eq(method)].sort_values("missing_rate")
            ax.errorbar(100 * data.missing_rate, data["mean"], yerr=data["std"],
                        label=method, color=color, marker="o", capsize=4, linewidth=2)
        clean = reference.loc[reference.model.eq(model) & reference.metric.eq("RMSE"), "mean"].iloc[0]
        ax.axhline(clean, color=INK, linestyle="--", label="Đầu vào đầy đủ")
        ax.set(title=model, xlabel="Xác suất thiếu đầu vào (%)", ylabel="RMSE dự đoán G3 (điểm)",
               xticks=[5, 15, 30])
        ax.grid(axis="y")
    axes[0].legend(fontsize=10)
    fig.supxlabel("Trung bình ± SD của 5 lần chia × 4 mặt nạ tại mỗi mức")
    save(fig, out, "model_performance")

    fig, axes = plt.subplots(1, 2, figsize=(12, 4.5), layout="constrained")
    for model, ax in zip(MODELS, axes):
        clean = reference.loc[reference.model.eq(model) & reference.metric.eq("RMSE"), "mean"].iloc[0]
        labels = ["Đầy đủ", "Train thiếu", "Train/test thiếu"]
        phase_scores = [clean]
        for phase in ("Masked train, clean test", "Masked train, masked test"):
            row = summary.loc[summary.model.eq(model) & summary.method.eq("Median")
                              & summary.missing_rate.eq(.15) & summary.phase.eq(phase)
                              & summary.subset.eq("All test") & summary.metric.eq("RMSE")]
            phase_scores.append(row["mean"].iloc[0])
        bars = ax.bar(labels, phase_scores, color=[INK, VIOLET, TEAL])
        ax.bar_label(bars, fmt="%.2f", padding=4)
        ax.set(title=model, ylabel="RMSE G3 (điểm)", ylim=(0, max(phase_scores) * 1.25))
        ax.grid(axis="y")
        ax.set_axisbelow(True)
    fig.supxlabel("Điền Median cho biến số và Mode cho biến loại, mức thiếu 15%")
    save(fig, out, "model_train_test_effect")

    example = predictions.loc[predictions.split_seed.eq(42) & predictions.mask_seed.eq(42)
                              & predictions.missing_rate.eq(.30) & predictions.method.eq("Median")
                              & predictions.phase.eq("Masked train, masked test")]
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 4.6), layout="constrained")
    for model, ax in zip(MODELS, axes):
        sample = example.loc[example.model.eq(model)]
        ax.scatter(sample.true_G3, sample.complete_reference_prediction, color=INK, marker="x", alpha=.55,
                   s=26, label="Đầu vào đầy đủ")
        ax.scatter(sample.true_G3, sample.prediction, color=TEAL, alpha=.55, s=26,
                   label="Thiếu 30%, điền Median")
        ax.plot([0, 20], [0, 20], color=AMBER, linestyle="--", linewidth=1)
        ax.set(title=model, xlabel="G3 thật", ylabel="G3 dự đoán", xlim=(-.5, 20.5), ylim=(-.5, 20.5))
    axes[0].legend(fontsize=9)
    save(fig, out, "model_predictions")


if __name__ == "__main__":
    evidence = run()
    print(f"Đã fit {evidence['fits']} pipeline, lưu đầy đủ điểm và dự đoán.")
