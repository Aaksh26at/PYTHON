from flask import Flask, render_template, request

app17 = Flask(__name__)


@app17.route('/')
def index():
    return render_template("index4.html")

@app17.route('/submit', methods=["POST"])
def submitpage():
    num1 = int(request.form.get('num1'))
    num2 = int(request.form.get('num2'))
    
    while num2 != 0:
        result = num1 % num2
        num1 = num2
        num2 = result

    return f"The GCD of the numbers is {num1}"

if __name__ == '__main__':
    app17.run(debug=True)
