
def calcBMI(feet, inches, weight):
    meters = ((feet * 12) + inches) * 0.025
    kilos = weight * 0.450
    
    meterSq = meters**2
    bmi = kilos/meterSq

    #60.05 45 3606.0025
    
    if bmi < 18.5:
        print (bmi)
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        print (bmi)
        return "Normal weight"
    elif 25 <= bmi <= 29.9:
        print (bmi)
        return "Overweight"
    else:
        print (bmi)
        return "Obese"

print("Please provide your height in feet and inches (Ex. 5 3): ")
f = float(input())
i = float(input())

print("\nPlease provide your weight in lbs: ")
w = float(input())

result = calcBMI(f, i, w)
print("\n" + result)