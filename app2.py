from flask import Flask

app2 = Flask(__name__)


names_list = ["Aakshat", "Saksham", "Dhruv", "Tushar"]

@app2.route('/')
def index():
    return "Plz enter the name in the URL to check if the name is avaiable or not"

@app2.route('/check/<name>')
def check_name(name):
    if name in names_list:
        return f"{name} is in the list"
    else:
        return f"{name} is not in the list."

if __name__ == '__main__':
    app2.run(debug=True)
    