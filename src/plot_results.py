"""Tạo biểu đồ từ mô hình lý thuyết hoặc dữ liệu và metric đã tính."""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gamma, norm

from src.prepare_data import CATEGORY, GROUP, NUMERIC, RATES

INK = "#173340"
TEAL = "#006D69"
AMBER = "#B04D1D"
VIOLET = "#624893"
SLATE = "#758D99"
PALE = "#DCE7EA"
BASE = "#FFFFFF"
VN_LABELS = ("G1 · Điểm kỳ đầu", "absences · Số buổi vắng", "G3 · Điểm cuối kỳ")
UNITS = ("Điểm (thang 0–20)", "Số buổi vắng", "Điểm (thang 0–20)")
GUARDIANS = {"mother": "Mẹ", "father": "Cha", "other": "Khác"}

plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 13, "text.color": INK,
    "axes.labelcolor": INK, "xtick.color": INK, "ytick.color": INK,
    "axes.spines.top": False, "axes.spines.right": False,
    "axes.spines.left": False, "axes.edgecolor": PALE, "axes.titleweight": "bold",
    "grid.color": PALE, "grid.linewidth": 0.85, "figure.facecolor": BASE,
    "legend.frameon": False,
})


def save(figure, out, name):
    figure.savefig(out / f"{name}.png", dpi=240, facecolor=BASE, bbox_inches="tight", pad_inches=0.13)
    plt.close(figure)


def theory(out):
    fig, axes = plt.subplots(1, 3, figsize=(13, 3.85), layout="constrained", sharey=True)
    x = np.linspace(-11, 11, 641)
    right = gamma(a=3)
    descriptions = (
        ("Đối xứng một đỉnh", norm(0, 2).pdf(x), [0, 0, 0], "Mean = Median = Mode"),
        ("Lệch phải", right.pdf(x), [3, right.median(), 2], "Mode < Median < Mean"),
        ("Lệch trái", right.pdf(-x), [-3, -right.median(), -2], "Mean < Median < Mode"),
    )
    for ax, (title, density, centers, order) in zip(axes, descriptions):
        ax.fill_between(x, density, color=PALE)
        ax.plot(x, density, color=INK, linewidth=2)
        if centers[0] == centers[1] == centers[2]:
            ax.axvline(0, color=INK, linewidth=2)
        else:
            for c, color, style in zip(centers, [AMBER, TEAL, VIOLET], ["-", "--", ":"]):
                ax.axvline(c, color=color, linestyle=style, linewidth=2)
        ax.set(title=title, xlim=(-8, 8), ylim=(0, 0.31), yticks=[], xticks=[])
        ax.set_xlabel(order, fontsize=13)
    axes[0].set_ylabel("Mật độ")
    handles = [plt.Line2D([], [], color=c, ls=s, lw=2) for c, s in
               [(AMBER, "-"), (TEAL, "--"), (VIOLET, ":")]]
    fig.legend(handles, ["Mean", "Median", "Mode"], loc="outside lower center", ncols=3, fontsize=11)
    save(fig, out, "distribution_theory")


def numeric_eda(out, observed):
    fig, axes = plt.subplots(2, 2, figsize=(12, 4.5), height_ratios=(3, 1), layout="constrained")
    for index, (column, label) in enumerate(zip(NUMERIC[:2], VN_LABELS[:2])):
        values = observed[column].dropna()
        hist, box = axes[:, index]
        bins = np.arange(-0.5, (20 if index == 0 else observed[column].max()) + 1.5, 1)
        hist.hist(values, bins=bins, weights=np.full(len(values), 100 / len(values)),
                  color=PALE, edgecolor=BASE)
        hist.set_xlim(bins[0], bins[-1])
        hist.axvline(values.mean(), color=AMBER, label="Mean", linewidth=2)
        hist.axvline(values.median(), color=TEAL, label="Median", linewidth=2, linestyle="--")
        hist.set(title=label, ylabel="Tỷ trọng (%)", xticklabels=[])
        hist.legend(loc="upper right", fontsize=10)
        box.boxplot(values, orientation="horizontal", widths=0.55, patch_artist=True,
                    boxprops={"facecolor": PALE, "edgecolor": INK},
                    medianprops={"color": TEAL, "linewidth": 2},
                    flierprops={"marker": "o", "markersize": 3, "markeredgecolor": AMBER, "alpha": 0.42})
        box.set(xlim=hist.get_xlim(), yticks=[], xlabel=UNITS[index])
        if index == 1:
            box.text(0.98, 0.82, "Điểm ngoài hàng rào 1,5 IQR", fontsize=9,
                     ha="right", transform=box.transAxes, color=AMBER)
    save(fig, out, "eda_numeric")


def before_after(out, stages):
    variable = NUMERIC[1]
    arrays = [stages[s][variable].dropna() for s in ("Complete", "Observed", "Mean", "Median")]
    bins = np.arange(-0.25, arrays[0].max() + 0.76, 0.5)
    fig, ax = plt.subplots(figsize=(8.3, 4.1), layout="constrained")
    for values, label, color, ls in zip(
        arrays, ("Đầy đủ", "Quan sát", "Điền Mean", "Điền Median"),
        (SLATE, INK, AMBER, TEAL), (":", "--", "-", "-"),
    ):
        proportions = np.histogram(values, bins)[0] / len(values)
        ax.stairs(proportions * 100, bins, color=color, linestyle=ls, linewidth=2.2, label=label)
    ax.set(xlabel="Số buổi vắng", ylabel="Tỷ trọng mỗi khoảng (%)", xlim=(bins[0], bins[-1]))
    ax.grid(axis="y")
    ax.legend(loc="upper right", ncols=2, fontsize=11)
    save(fig, out, "numeric_imputation_before_after")


def errors(out, scores):
    fig, axes = plt.subplots(2, 2, figsize=(10.8, 6.9), layout="constrained")
    x = np.arange(len(RATES))
    for row, (var, label) in enumerate(zip(NUMERIC[:2], VN_LABELS[:2])):
        for col, metric in enumerate(("MAE", "RMSE")):
            ax = axes[row, col]
            for method, color, dx in (("Mean", AMBER, -0.17), ("Median", TEAL, 0.17)):
                data = scores.loc[(scores.variable == var) & (scores.metric == metric)
                                  & (scores.method == method)].sort_values("missing_rate")
                ax.bar(x + dx, data["mean"], 0.32, yerr=data["std"], capsize=4, color=color, label=method)
            ax.set(title=f"{label} · {metric}", xticks=x, xticklabels=[f"{rate:.0%}" for rate in RATES],
                   ylabel=("Sai số (điểm)" if row == 0 else "Sai số (buổi vắng)"), ylim=(0, None))
            ax.set_axisbelow(True)
            ax.grid(axis="y")
    axes[0, 0].legend(ncols=2, fontsize=11)
    fig.supxlabel("Tỷ lệ thiếu danh nghĩa · Cột = trung bình, thanh sai số = SD qua 12 mặt nạ")
    save(fig, out, "imputation_errors")


def categorical(out, stages):
    labels = sorted(stages["Complete"][CATEGORY].unique())
    x = np.arange(len(labels))
    fig, ax = plt.subplots(figsize=(7.8, 4.35), layout="constrained")
    for stage, label, dx, color in (
        ("Complete", "Đầy đủ", -0.28, SLATE), ("Observed", "Quan sát", 0, INK),
        ("Mode", "Điền Mode", 0.28, TEAL),
    ):
        counts = stages[stage][CATEGORY].value_counts().reindex(labels, fill_value=0)
        bars = ax.bar(x + dx, counts, width=0.24, color=color, label=label)
        ax.bar_label(bars, padding=3, fontsize=10)
    ax.set(xticks=x, xticklabels=[GUARDIANS[label] for label in labels],
           xlabel="Người giám hộ (guardian)", ylabel="Số quan sát")
    ax.set_ylim(0, ax.get_ylim()[1] * 1.12)
    ax.legend(ncols=3, fontsize=11)
    ax.set_axisbelow(True)
    ax.grid(axis="y")
    save(fig, out, "categorical_mode")


def groups(out, stages):
    fig, ax = plt.subplots(figsize=(8, 4), layout="constrained")
    frame = stages["Observed"]
    variable = NUMERIC[2]
    bins = np.arange(-0.5, 21.5, 1)
    for group, color in (("GP", TEAL), ("MS", VIOLET)):
        values = frame.loc[frame[GROUP] == group, variable].dropna()
        ax.hist(values, bins=bins, weights=np.full(len(values), 100 / len(values)),
                color=color, alpha=0.38, label=f"Trường {group}")
        ax.axvline(values.median(), color=color, linewidth=2, linestyle="--")
    ax.axvline(frame[variable].median(), color=INK, linewidth=2, label="Median toàn cục")
    ax.set(xlabel="Điểm G3 (thang 0–20)", ylabel="Tỷ trọng trong từng trường (%)")
    ax.legend(fontsize=11)
    save(fig, out, "g3_by_school")


def constant_loss(out, support):
    curve = support["age_loss_curve"]
    candidates = [row["candidate"] for row in curve]
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 4.1), layout="constrained")
    for ax, metric, best, color in zip(axes, ("MAE", "RMSE"), (23, 34), (TEAL, AMBER)):
        values = [row[metric] for row in curve]
        ax.plot(candidates, values, color=color, linewidth=2.5)
        point = next(row[metric] for row in curve if row["candidate"] == best)
        ax.scatter([best], [point], color=color, s=55, zorder=3)
        ax.axvline(best, color=color, linestyle="--", linewidth=1.4)
        ax.set(title=f"{metric} nhỏ nhất tại {best}", xlabel="Giá trị dự đoán chung c",
               ylabel="Sai số trên 5 tuổi quan sát (năm)")
        ax.grid(axis="y")
    save(fig, out, "constant_prediction_loss")


def iqr_outliers(out, observed):
    values = observed["absences"].dropna()
    q1, q3 = values.quantile([.25, .75])
    iqr = q3 - q1
    lower, upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    fig, ax = plt.subplots(figsize=(10.2, 2.4), layout="constrained")
    ax.boxplot(values, orientation="horizontal", widths=.45, patch_artist=True,
               boxprops={"facecolor": PALE, "edgecolor": INK},
               medianprops={"color": TEAL, "linewidth": 2},
               flierprops={"marker": "o", "markersize": 5, "markeredgecolor": AMBER})
    for fence in (lower, upper):
        ax.axvline(fence, color=AMBER, linestyle="--", linewidth=1.5)
    flagged = int((values.lt(lower) | values.gt(upper)).sum())
    ax.set(yticks=[], xlabel="Số buổi vắng",
           title=f"Demo absences · Q1 = {q1:g}, Q3 = {q3:g}, IQR = {iqr:g} · {flagged} điểm gắn cờ",
           xlim=(lower - 1, values.max() + 2))
    save(fig, out, "iqr_outliers")


def create_figures(out, stages, scores, support):
    out.mkdir(parents=True, exist_ok=True)
    theory(out)
    numeric_eda(out, stages["Observed"])
    before_after(out, stages)
    errors(out, scores)
    categorical(out, stages)
    groups(out, stages)
    constant_loss(out, support)
    iqr_outliers(out, stages["Observed"])
