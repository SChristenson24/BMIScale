from flask import Flask, request, render_template

app = Flask(__name__)

def calcBMI(feet, inches, weight):
    if feet == 0 and inches == 0:
        return "Invalid input: Height cannot be zero"
    elif weight == 0:
        return "Invalid input: Weight cannot be zero"
    
    meters = ((feet * 12) + inches) * 0.0254
    kilos = weight * 0.453592
    meterSq = meters**2
    bmi = kilos / meterSq

    if bmi < 18.5:
        return f"BMI: {bmi:.2f} - Underweight"
    elif bmi < 25:
        return f"BMI: {bmi:.2f} - Normal weight"
    elif bmi < 30.0:
        return f"BMI: {bmi:.2f} - Overweight"
    else:
        return f"BMI: {bmi:.2f} - Obese"

@app.route('/', methods=['GET', 'POST'])
def bmi_calculator():
    if request.method == 'POST':
        feet = float(request.form.get('feet', 0))
        inches = float(request.form.get('inches', 0))
        weight = float(request.form.get('weight', 0))
        result = calcBMI(feet, inches, weight)
        return render_template("results.html", result=result)
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
