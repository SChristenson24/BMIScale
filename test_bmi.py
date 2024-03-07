import unittest
from bmi import calcBMI

class TestBMICalculator(unittest.TestCase):
    def test_underweight(self):
        self.assertEqual(calcBMI(5, 0, 94), "Underweight")

    def test_normal(self):
        self.assertEqual(calcBMI(5, 0, 95), "Normal weight")

    def test_overweight(self):
        self.assertEqual(calcBMI(5, 0, 129), "Overweight")

    def test_obese(self):
        self.assertEqual(calcBMI(5, 0, 154), "Obese")

    def test_edge_case_height_zero(self):
        self.assertEqual(calcBMI(0, 0, 100), "Invalid input: Height cannot be zero")

    def test_edge_case_weight_zero(self):
        self.assertEqual(calcBMI(5, 0, 0), "Invalid input: Weight cannot be zero")

if __name__ == '__main__':
    unittest.main()
