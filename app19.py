from flask import Flask,request,render_template

fact = Flask(__name__)

@fact.route('/')
def index():
    return render_template('fact.html')


def fact1(n):
    if n == 0 :
        return 1
    else:
        return n * factorial(n-1)

@fact.route('/submit',methods = ['POST'])
def factorial():
    
    result = 0
    NUM1 = int(request.form['NUM1'])
    result = fact1(NUM1)

    return result