"""
Flask application that provides an endpoint for performing arithmetic operations
using the Calculator class.
"""

from flask import Flask, request, render_template_string
from calculator import Calculator

app = Flask(__name__)

@app.route('/calculate', methods=['GET'])
def calculate():
    """
    Handles GET requests to the calculator and performs operations based on the given parameters.
    """
    # Retrieve parameters from URL
    operand1 = request.args.get('op1', type=float)
    operand2 = request.args.get('op2', type=float)
    operation = request.args.get('operation')


    calculator = Calculator(operand1, operand2)


    try:
        if operation == 'sum':
            result = calculator.sum()
            operator = '+'
        elif operation == 'subtract':
            result = calculator.subtract()
            operator = '-'
        elif operation == 'multiply':
            result = calculator.multiply()
            operator = '*'
        elif operation == 'divide':
            result = calculator.divide()
            operator = '/'
        else:
            return "<h3>Unknown operation</h3>", 400

        # Render the result in a nice way with a title and an author signature
        html_template = """
        <!doctype html>
        <html lang="en">
        <head>
            <meta charset="utf-8">
            <title>Calculation Result</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    text-align: center;
                    margin-top: 50px;
                }
                .result {
                    font-size: 48px;
                    font-weight: bold;
                    margin-bottom: 30px;
                }
                .title {
                    font-size: 32px;
                    margin-bottom: 20px;
                }
                .author {
                    font-size: 20px;
                    font-style: italic;
                    color: gray;
                    margin-top: 50px;
                }
            </style>
        </head>
        <body>
            <div class="title">Calculation Result</div>
            <div class="result">{{ operand1 }} {{ operator }} {{ operand2 }} = {{ result }}</div>
            <div class="author">author: Jan Ślusarek</div>
        </body>
        </html>
        """

        return render_template_string(
            html_template,
            operand1=operand1,
            operator=operator,
            operand2=operand2,
            result=result
        )

    except ValueError as e:
        return f"<h3>Error: {str(e)}</h3>", 400

if __name__ == '__main__':
    app.run(debug=True)
