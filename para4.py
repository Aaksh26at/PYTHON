from flask import Flask,redirect,request,url_for

para4 = Flask(__name__)

@para4.route('/EVEN<int:num2>')
def even(num2):
     return  f"The number is even " + str(num2) 

@para4.route('/ODD<int:num2>')
def odd(num2):
     return  f"The number is odd " + str(num2)

@para4.route('/check_number')
def check_number():
       num1 = int(request.args.get('num1','0'))
       result = ''
       if num1 % 2 ==0:
              result = "even"
       else:
              result = "odd"
       
       return redirect(url_for('even',num2 = num1))





if __name__ == '__main__':
       para4.run(debug=True)