from flask import Flask, redirect, url_for

revi2 = Flask(__name__)

@revi2.route('/')
def index():
    return "hello world"

@revi2.route('/pass/<int:score>')
def index2(score):
    return "the student is pass and the score is " + str(score)

@revi2.route('/fail/<int:score>')
def index3(score):
    return "The student is fail and the score is " + str(score)

@revi2.route('/results/<int:marks>')
def results(marks):
    result = ""
    if marks < 50:
        result = 'fail'
    else:
        result = 'pass'
    return redirect(url_for(result, score=marks))

if __name__ == '__main__':
    revi2.run(debug=True)
