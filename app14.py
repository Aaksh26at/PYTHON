from flask import Flask

app14 = Flask(__name__)

@app14.route('/')
def index():
       return "Welcome to flask again"

@app14.route('/sum/<int:var1>/<int:var2>')
def index2(var1,var2):
       var3 = var1+var2
       return "WELCOME AGAIN " + str(var3)


if __name__ == '__main__':
       app14.run(debug=True)