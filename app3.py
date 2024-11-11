from flask import Flask

app3 = Flask(__name__)

@app3.route('/check/<int:var1>')
def index(var1):
       if var1%2==0:
              return "number is even"
       else:
              return "Number is odd"


if __name__ == '__main__':
       app3.run(debug=True)
