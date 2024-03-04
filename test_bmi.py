import unittest
from bmi import calcBMI

class TestBMICalculator(unittest.TestCase):
    
    def test_underweight(self):
        self.assertEqual(calcBMI(5, 2, 100), "Underweight")
        
    def test_normal_weight(self):
        self.assertEqual(calcBMI(5, 9, 145), "Normal weight")
        
    def test_overweight(self):
        self.assertEqual(calcBMI(5, 6, 180), "Overweight")
    #failed
    def test_obese(self):
        self.assertEqual(calcBMI(5, 3, 200), "Obese")
        
    def test_boundary_normal_weight_upper(self):
        self.assertEqual(calcBMI(5, 11, 174), "Normal weight")
        
    def test_boundary_overweight_lower(self):
        self.assertEqual(calcBMI(5, 11, 175), "Overweight")

if __name__ == '__main__':
    unittest.main()