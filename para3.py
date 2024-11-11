from flask import Flask,request,redirect,url_for

para3 = Flask(__name__)
@para3.route('/FAIL/<int:score>')
def fail(score):
       return "You failed and your score is " + str(score)

@para3.route('/PASS/<int:score>')
def passed(score):
       return "You passed and your score is " + str(score)

@para3.route('/result')
def result():
       marks = int(request.args.get('marks','0'))
       result = ''
       if marks<50:
              result = 'fail'
       else:
              result = 'passed'
              
       return redirect(url_for(result,score = marks))

if __name__ == '__main__':
       para3.run(debug=True)