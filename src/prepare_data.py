"""Đọc Student Performance của UCI và che ô độc lập với giá trị dữ liệu."""

from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
SEED = 42
DEMO_RATE = 0.15
RATES = (0.05, 0.15, 0.30)
NUMERIC = ("G1", "absences", "G3")
CATEGORY = "guardian"
GROUP = "school"
TARGETS = (*NUMERIC, CATEGORY)


def load_complete(root=ROOT):
    """Read the original Portuguese course CSV and select the seminar columns."""
    source = root / "data" / "raw" / "student-por.csv"
    frame = pd.read_csv(source, sep=";", usecols=[*TARGETS, GROUP])
    complete = frame[[*TARGETS, GROUP]].rename_axis("row_id")
    if complete.isna().any().any():
        raise ValueError("Các cột benchmark cần đầy đủ trước khi tạo mặt nạ.")
    return complete


def mask_mcar(complete, rate, rng):
    """Draw one independent Bernoulli mask per target cell and preserve row IDs."""
    if not 0 <= rate <= 1:
        raise ValueError("Tỷ lệ thiếu phải nằm trong [0, 1].")
    mask = pd.DataFrame(
        rng.random((len(complete), len(TARGETS))) < rate,
        columns=list(TARGETS),
        index=complete.index,
    )
    return complete.mask(mask.reindex(columns=complete.columns, fill_value=False)), mask


def demo_data(complete):
    return mask_mcar(complete, DEMO_RATE, np.random.default_rng(SEED))


def write_data(root=ROOT):
    destination = root / "data"
    complete = load_complete(root)
    observed, mask = demo_data(complete)
    complete.to_csv(destination / "student_complete.csv")
    observed.to_csv(destination / "student_missing_15pct.csv")
    mask.to_csv(destination / "student_mask_15pct.csv")
    return complete, observed, mask


if __name__ == "__main__":
    write_data()
