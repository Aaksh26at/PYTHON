from flask import Flask

app7 = Flask(__name__)

list2 = []

@app7.route('/')
def index2():
       return "Plz enter the name in the above URL to check if the given name is present or not"

@app7.route('/name/<name>')
def index3(name):
       list2.append(name)
       return "The name is append to the list"

@app7.route('/name/list_check')
def index4():
       return list2


if __name__ == '__main__':
       app7.run(debug=True)
