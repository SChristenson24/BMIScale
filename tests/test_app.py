from app import calcBMI

def test_underweight():
    assert calcBMI(5, 0, 94.7) == "BMI: 18.495 - Underweight"

def test_normal():
    assert calcBMI(5, 0, 94.8) == "BMI: 18.514 - Normal weight"

def test_normal_upper():
    assert calcBMI(5, 0, 128) == "BMI: 24.998 - Normal weight"

def test_overweight():
    assert calcBMI(5, 0, 128.1) == "BMI: 25.018 - Overweight"

def test_overweight_upper():
    assert calcBMI(5, 0, 153.6) == "BMI: 29.998 - Overweight"

def test_obese():
    assert calcBMI(5, 0, 153.7) == "BMI: 30.017 - Obese"

def test_edge_case_height_zero():
    assert calcBMI(0, 0, 100) == "Invalid input: Feet must be greater than zero."

def test_edge_case_weight_zero():
    assert calcBMI(5, 0, 0) == "Invalid input: Weight must be greater than zero."
