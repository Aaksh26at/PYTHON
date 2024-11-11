from flask import Flask, redirect, request, url_for

app = Flask(__name__)

@app.route('/sum/<int:num1>/<int:num2>')
def index(num1, num2):
    return f"The sum of the numbers is {num1 + num2}"

@app.route('/result')
def result():
    num1 = int(request.args.get('num1'))
    num2 = int(request.args.get('num2'))
    return redirect(url_for('index', num1=num1, num2=num2))

if __name__ == '__main__':
    app.run(debug=True)
