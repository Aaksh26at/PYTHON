from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
       return "Hello world"

@app.route('/login/<int:var1>/<int:var2>')
def index1(var1,var2):
       var3 = var1+var2
       return " Hello aakshat " + str(var3)

@app.route('/login/profile')
def index2():
       return "Hi aakshat"


if __name__ == '__main__':
       app.run(debug=True)       