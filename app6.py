from flask import Flask

app6 = Flask(__name__)

list1 = []

@app6.route('/name/<name>')

def index(name):
      list1.append(name)
      return f"The {name} has been append to the list"

@app6.route('/name/list_check')

def index1():
       return list1
                 
if __name__ == '__main__':
       app6.run(debug=True)
       