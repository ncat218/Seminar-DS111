import tempfile
from pathlib import Path
import shutil
import unittest

import numpy as np
import pandas as pd
from numpy.testing import assert_allclose

from src.prepare_data import ROOT
from src.run_model_experiments import (
    FEATURES, NUMERIC_FEATURES, TARGET, build_pipeline, load_model_data, mask_features, metric_rows, run,
)


class ModelExperimentTests(unittest.TestCase):
    def test_mask_never_includes_target_and_preserves_index(self):
        X, y = load_model_data()
        before = y.copy()
        observed, mask = mask_features(X, .3, np.random.default_rng(42))
        self.assertNotIn(TARGET, FEATURES)
        self.assertEqual(list(observed.columns), list(FEATURES))
        self.assertTrue(observed.index.equals(X.index))
        pd.testing.assert_frame_equal(observed.isna(), mask)
        pd.testing.assert_series_equal(y, before)

    def test_statistics_use_train_and_unknown_category_is_supported(self):
        train = pd.DataFrame({
            "G1": [1., 3., np.nan], "G2": [2., 4., 6.], "age": [15., 16., 17.],
            "absences": [0., 2., 4.], "guardian": ["mother", "father", "mother"],
            "school": ["GP", "GP", "MS"],
        })
        test = train.iloc[:2].copy()
        test.loc[0, "G1"] = 1_000_000
        test.loc[1, "G1"] = np.nan
        test.loc[1, "school"] = "UNKNOWN"
        pipeline = build_pipeline("Mean", "Ridge").fit(train, [8., 12., 14.])
        imputer = pipeline["preprocess"].named_transformers_["numeric"]["imputer"]
        assert_allclose(imputer.statistics_, [2., 4., 16., 2.])
        previous = imputer.statistics_.copy()
        self.assertTrue(np.isfinite(pipeline.predict(test)).all())
        assert_allclose(imputer.statistics_, previous)

    def test_task_metrics_score_all_test_rows(self):
        truth = pd.Series([10., 12., 14., 16.])
        prediction = np.array([9., 11., 15., 18.])
        missing = pd.Series([True, False, True, False])
        rows = pd.DataFrame(metric_rows(truth, prediction, missing, truth.to_numpy(), {}))
        all_mae = rows.loc[rows.subset.eq("All test") & rows.metric.eq("MAE")].iloc[0]
        self.assertEqual(all_mae.n_scored, 4)
        self.assertEqual(all_mae.value, 1.25)
        subset_mae = rows.loc[rows.subset.eq("Missing input") & rows.metric.eq("MAE")].iloc[0]
        self.assertEqual(subset_mae.n_scored, 2)
        self.assertEqual(subset_mae.value, 1.)

    def test_all_numeric_strategies_work_through_pipeline(self):
        X, y = load_model_data()
        train, _ = mask_features(X.iloc[:120], .3, np.random.default_rng(42))
        test, _ = mask_features(X.iloc[120:140], .3, np.random.default_rng(43))
        for method in ("Mean", "Median", "Mode"):
            with self.subTest(method=method):
                prediction = build_pipeline(method, "Ridge").fit(train, y.iloc[:120]).predict(test)
                self.assertEqual(prediction.shape, (20,))
                self.assertTrue(np.isfinite(prediction).all())

    def test_small_end_to_end_run_scores_both_phases(self):
        with tempfile.TemporaryDirectory() as directory:
            task = Path(directory)
            raw = task / "data/raw"
            raw.mkdir(parents=True)
            shutil.copyfile(ROOT / "data/raw/student-por.csv", raw / "student-por.csv")
            evidence = run(task, rates=(.15,), split_seeds=(42,), mask_seeds=(42,))
            self.assertEqual(evidence["fits"], 8)
            scores = pd.read_csv(task / "results/model_evaluation.csv")
            self.assertEqual(set(scores.phase), {"Masked train, clean test", "Masked train, masked test"})
            self.assertTrue(scores.loc[scores.subset.eq("All test"), "mean_n_scored"].eq(163).all())
            self.assertEqual(set(scores.method), {"Mean", "Median", "Mode"})
            self.assertEqual(set(scores.model), {"Ridge", "Random Forest"})


if __name__ == "__main__":
    unittest.main()
