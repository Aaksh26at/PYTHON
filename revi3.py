from flask import Flask,redirect,url_for,request,render_template

revi3 = Flask(__name__)

@revi3.route('/')
def homepage():
       return "This is my home page"

@revi3.route('/pass/<int:score>')

def pass1(score):
       return f"The student hass pass and the score is {score}"


@revi3.route('/fail/<int:score>')
def fail(score):
       return f"The student is fail and the score is {score}"
       

@revi3.route('/results/<int:score>')
def results(score):
    result = ''
    if score>50:
           result = 'pass'
    else:
           result = 'fail'
    return redirect(url_for(result,score=score))


if __name__ == '__main__':
       revi3.run(debug=True)