from flask import Flask, render_template, request
from maths2 import sum, subtract, mul

app = Flask(__name__)

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route("/calculate", methods=["GET", "POST"])
def calculate_route():
    if request.method == "POST":
        operation = request.form.get("operation")
        num1 = float(request.form.get("num1"))
        num2 = float(request.form.get("num2"))
        
        if operation == "sum":
            result = sum(num1, num2)
        elif operation == "subtract":
            result = subtract(num1, num2)
        elif operation == "multiply":
            result = mul(num1, num2)
        else:
            result = "Invalid operation"

        return render_template('index.html', result=result)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
