def calcBMI(feet, inches, weight):
    if feet == 0 and inches == 0:
        return "Invalid input: Height cannot be zero"
    elif weight == 0:
        return "Invalid input: Weight cannot be zero"
    
    meters = ((feet * 12) + inches) * 0.0254
    kilos = weight * 0.453592
    
    meterSq = meters**2
    bmi = kilos / meterSq

    print(f"\nBMI: {bmi}")
    
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30.0:
        return "Overweight"
    else:
        return "Obese"

    
print("Please provide your height in feet (Ex. if 5' 3'', input 5)")
f = float(input())
print("Please provide your height in inches (Ex. if 5' 3'', input 3)")
i = float(input())
print("\nPlease provide your weight in lbs: ")
w = float(input())

result = calcBMI(f, i, w)
print("\n" + result + "\n")
