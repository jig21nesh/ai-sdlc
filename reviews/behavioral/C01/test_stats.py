import unittest
from stats import mean


class StatsTests(unittest.TestCase):
    def test_nonempty(self):
        self.assertEqual(mean([2, 4]), 3)

    def test_empty(self):
        self.assertEqual(mean([]), 0)

    def test_mixed_numbers(self):
        self.assertEqual(mean([-2, 1, 2.5]), 0.5)
