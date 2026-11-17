import unittest

import numpy as np
import pandas as pd
from numpy.testing import assert_allclose
from pandas.testing import assert_frame_equal
from sklearn.model_selection import train_test_split

from src.generate_data import CATEGORY, NUMERIC, SEED, TARGETS, generate_complete, mask_mcar
from src.run_experiments import (
    benchmark, describe_demo, fit_imputer, group_median, masked_scores, summarize_scores, transform,
)


class ImputationTests(unittest.TestCase):
    def test_mean_and_median_preserve_observed_ages(self):
        age = pd.DataFrame({"age": [20, 22, 23, 25, 80, np.nan]})
        for method, expected in (("Mean", 34), ("Median", 23)):
            with self.subTest(method=method):
                result = transform(fit_imputer(age, "age", method), age, "age", method)
                self.assertEqual(result.iloc[-1], expected)
                assert_allclose(result.iloc[:-1], age["age"].iloc[:-1])

    def test_mode_and_tie(self):
        size = pd.DataFrame({"category": ["M", "M", "L", "S", None, "M"]})
        mode = fit_imputer(size, CATEGORY, "Mode")
        self.assertEqual(transform(mode, size, CATEGORY, "Mode").iloc[4], "M")
        tie = pd.DataFrame({"category": ["Z", "A", "Z", "A", np.nan]})
        self.assertEqual(fit_imputer(tie, CATEGORY, "Mode").statistics_[0], "A")

    def test_all_missing_and_wrong_dtype(self):
        frame = pd.DataFrame({"x": [np.nan, np.nan], "category": ["M", None]})
        for method in ("Mean", "Median", "Mode"):
            with self.assertRaisesRegex(ValueError, "không có giá trị quan sát"):
                fit_imputer(frame, "x", method)
        with self.assertRaises(TypeError):
            fit_imputer(frame, CATEGORY, "Mean")

    def test_test_values_cannot_change_fill(self):
        train = pd.DataFrame({"x": [1.0, 3.0, np.nan]})
        test = pd.DataFrame({"x": [1e6, np.nan]})
        imputer = fit_imputer(train, "x", "Mean")
        result = transform(imputer, test, "x", "Mean")
        assert_allclose(result, [1e6, 2])

    def test_metrics_only_score_hidden_cells(self):
        mask = pd.Series([True, False, True])
        numeric = masked_scores(pd.Series([1., 2., 5.]), pd.Series([2., 1e9, 8.]), mask)
        self.assertEqual(numeric["MAE"], 2)
        self.assertAlmostEqual(numeric["RMSE"], np.sqrt(5))
        label = masked_scores(pd.Series(["M", "S", "L"]), pd.Series(["M", "S", "M"]), mask, True)
        self.assertEqual(label["Accuracy"], 0.5)
        with self.assertRaises(ValueError):
            masked_scores(pd.Series([1.]), pd.Series([1.]), pd.Series([False]))

    def test_group_fallback_for_unknown_or_small_groups(self):
        train = pd.DataFrame({"group": ["A", "A", "B"], "x": [2., 4., 100.]})
        test = pd.DataFrame({"group": ["A", "B", "C"], "x": [np.nan, np.nan, np.nan]})
        assert_allclose(group_median(train, test, "x", min_observed=2), [3, 4, 4])

    def test_mask_and_demo_invariance(self):
        full = generate_complete(200)
        observed, mask = mask_mcar(full, 0.15, np.random.default_rng(SEED))
        _, repeated = mask_mcar(full, 0.15, np.random.default_rng(SEED))
        assert_frame_equal(mask, repeated)
        assert_frame_equal(observed[list(TARGETS)].isna(), mask)
        self.assertTrue(observed["group"].equals(full["group"]))
        stages, _, _ = describe_demo(full, observed)
        variable = NUMERIC[1]
        count = observed[variable].count()
        self.assertAlmostEqual(stages["Mean"][variable].mean(), observed[variable].mean())
        self.assertAlmostEqual(stages["Mean"][variable].var(),
                               (count - 1) / (len(full) - 1) * observed[variable].var())

    def test_benchmark_row_matches_independent_train_and_mask(self):
        complete = generate_complete()
        rate, seed = 0.15, 47
        train_raw, test_raw = train_test_split(complete, test_size=0.25, random_state=42)
        self.assertFalse(len(train_raw.index.intersection(test_raw.index)))
        children = np.random.SeedSequence(seed).spawn(2)
        variable = NUMERIC[1]
        column_index = TARGETS.index(variable)
        train_hidden = np.random.default_rng(children[0]).random((len(train_raw), len(TARGETS))) < rate
        test_hidden = np.random.default_rng(children[1]).random((len(test_raw), len(TARGETS))) < rate
        expected_fill = train_raw.loc[~train_hidden[:, column_index], variable].mean()
        expected_mae = (test_raw.loc[test_hidden[:, column_index], variable] - expected_fill).abs().mean()

        score = benchmark(complete, rates=(rate,), seeds=(seed,))
        row = score.query("variable == @variable and method == 'Mean' and metric == 'MAE'").iloc[0]
        self.assertEqual(row.n_test_masked, test_hidden[:, column_index].sum())
        self.assertAlmostEqual(float(row.fill_value), expected_fill)
        self.assertAlmostEqual(row.value, expected_mae)

    def test_main_benchmark_covers_three_rates_and_twelve_masks(self):
        scores = summarize_scores(benchmark(generate_complete()))
        self.assertEqual(set(scores.missing_rate), {0.05, 0.15, 0.30})
        self.assertEqual(set(scores.repeats), {12})
        self.assertEqual(len(scores), 45)


if __name__ == "__main__":
    unittest.main()
