from flask import Flask

app15 = Flask(__name__)

@app15.route('/')
def index():
    return "HELLO WORLD"

@app15.route('/GCD/<int:var1>/<int:var2>')
def gcd(var1, var2):
          
    while var2 != 0:
        result = var1 % var2
        var1 = var2
        var2 = result
    return f"The GCD is {var1}"




if __name__ == '__main__':
    app15.run(debug=True)
