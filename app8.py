from flask import Flask

app8 = Flask(__name__)

@app8.route('/')

def index():
       return "plz enter the value in the above url"

@app8.route('/value/<int:value>')

def index2(value):
       return " The reciving value is " + str(value)


if __name__ == '__main__':
       app8.run(debug=True)