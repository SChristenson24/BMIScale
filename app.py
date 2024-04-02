from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

def calcBMI(feet, inches, weight):
    if feet <= 0 and inches <= 0:
        return "Invalid input: Height must be greater than zero."
    elif weight <= 0:
        return "Invalid input: Weight must be greater than zero."
    
    meters = ((feet * 12) + inches) * 0.0254
    kilos = weight * 0.453592
    bmi = kilos / (meters ** 2)

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
        try:
            feet = float(request.form.get('feet', 0))
            inches = float(request.form.get('inches', 0))
            weight = float(request.form.get('weight', 0))
        except ValueError:
            return jsonify({'result': 'Invalid input: Please enter numeric values.'}), 400

        result = calcBMI(feet, inches, weight)
        return jsonify({'result': result})
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
