from flask import Flask

app4 = Flask(__name__)

@app4.route('/num1/<int:var1>')

def check_prime(var1):
       if var1%2==0:
              return "The number is not prime"
       else:
              return "The number is prime"
       
if __name__ == '__main__':
       app4.run(debug=True)