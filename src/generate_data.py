"""Sinh dữ liệu đầy đủ và mặt nạ MCAR độc lập với giá trị dữ liệu."""

from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
SEED = 42
N_ROWS = 3200
DEMO_RATE = 0.15
RATES = (0.05, 0.15, 0.30)
NUMERIC = ("symmetric_numeric", "skewed_numeric", "multimodal_numeric")
CATEGORY = "category"
TARGETS = (*NUMERIC, CATEGORY)


def generate_complete(n=N_ROWS, seed=SEED):
    """Append group labels observed by design. Numeric units are arbitrary."""
    rng = np.random.default_rng(seed)
    group = rng.choice(["A", "B"], size=n)
    return pd.DataFrame({
        NUMERIC[0]: rng.triangular(30, 50, 70, size=n),
        NUMERIC[1]: rng.lognormal(2.8, 0.85, size=n),
        NUMERIC[2]: rng.normal(np.where(group == "A", 35, 65), 4, size=n),
        CATEGORY: rng.choice(["M", "S", "L"], size=n, p=[0.61, 0.26, 0.13]),
        "group": group,
    }, index=pd.RangeIndex(n, name="row_id"))


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
    destination.mkdir(parents=True, exist_ok=True)
    complete = generate_complete()
    observed, mask = demo_data(complete)
    complete.to_csv(destination / "synthetic_complete.csv")
    observed.to_csv(destination / "synthetic_missing_15pct.csv")
    mask.to_csv(destination / "synthetic_mask_15pct.csv")
    return complete, observed, mask


if __name__ == "__main__":
    write_data()
