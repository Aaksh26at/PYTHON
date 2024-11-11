from flask import Flask


revi = Flask(__name__)


@revi.route('/')
def index():
       return "hello world"

@revi.route('/hi')
def index1():
       return "hi aakshat"

@revi.route('/hi/<int:var1>/<int:var2>')
def index2(var1,var2):
       return "The sum of the numbers are " +  str (var1 + var2)


if __name__ == '__main__':
      revi.run(debug=True) 

