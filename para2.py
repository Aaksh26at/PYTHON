from flask import Flask, request, redirect, url_for

para2 = Flask(__name__)

@para2.route('/EVEN/<int:num2>')
def even(num2):
    return f"The number {num2} is even."

@para2.route('/ODD/<int:num2>')
def odd(num2):
    return f"The number {num2} is odd."

@para2.route('/check_number')
def check_number():
    num1 = int(request.args.get('num1', 0))
    if num1 % 2 == 0:
        return redirect(url_for('even', num2=num1))
    else:
        return redirect(url_for('odd', num2=num1))

if __name__ == '__main__':
    para2.run(debug=True)
