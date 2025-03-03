import os
import sys
import unittest

paces_dir = os.path.abspath(__file__).split("test")[0]
sys.path.append(paces_dir)

from paces_calc import pace_math


class TestConversions(unittest.TestCase):

    def test_km_conversions(self):
        test_cases = [("1km", 1000.0), ("324km", 324000.0), ("1.234km", 1234.0)]
        for input, expected in test_cases:
            with self.subTest(input=input):
                self.assertAlmostEqual(pace_math.convert_to_meters(input), expected, 2, f"{input} to meter wrong")

    def test_mi_conversions(self):
        test_cases = [("1mi", 1609.34), ("121mi", 194730.14), ("2.345mi", 3773.9023)]
        for input, expected in test_cases:
            with self.subTest(input=input):
                self.assertAlmostEqual(pace_math.convert_to_meters(input), expected, 2, f"{input} to meter wrong")

    def test_meter_conversions(self):
        test_cases = [("1m", 1.0), ("521m", 521.0), ("2.345m", 2.345)]
        for input, expected in test_cases:
            with self.subTest(input=input):
                self.assertAlmostEqual(pace_math.convert_to_meters(input), expected, 2, f"{input} to meter wrong")

    def test_common_distances_conversions(self):
        test_cases = [
                ("0.5mi", 804.672), ("3km", 3000.0), ("2mi", 3218.68),
                ("5km", 5000.0), ("26.2mi", 42164.708), ("42.195km", 42195.0),
                ("100mi", 160934.0), ("161km", 161000.0)
            ]
        for input, expected in test_cases:
            with self.subTest(input=input):
                self.assertAlmostEqual(pace_math.convert_to_meters(input), expected, 2, f"{input} to meter wrong")

if __name__ == "__main__":
    unittest.main()
