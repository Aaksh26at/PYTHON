from flask import Flask,redirect,request,render_template

app21 = Flask(__name__)

@app21.route('/')
def index1():
       return render_template("index8.html")

def calculatesum(n):
       if(n==1):
              return n
       else:
              return n + calculatesum(n-1)

@app21.route('/submit',methods=['POST'])
def sum1():
       NUM1 = int(request.form.get("Num1"))
       result = calculatesum(NUM1)
       return "The sum of n natural numbers is: "+str(result)


if __name__ == '__main__':
       app21.run(debug=True)