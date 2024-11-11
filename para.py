from flask import Flask,request,redirect,url_for

para = Flask(__name__)

@para.route('/FAIL/<int:score>')
def fail(score):
       return "you failed and your score is " + str(score)

@para.route('/PASS/<int:score>')
def passed(score):
       return "You passed and your score is " + str(score)

@para.route('/result')
def result():
       marks = int(request.args.get('marks','40'))
       result = ''
       if marks<50:
              result = 'fail'
       else:
              result = 'passed'
       return redirect(url_for(result,score = marks))

if __name__ == '__main__':
       para.run(debug=True)