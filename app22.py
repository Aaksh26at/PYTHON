from flask import Flask,redirect,render_template,request

app22 = Flask(__name__)

@app22.route('/')
def index():
       return render_template("index9.html")

def fabisum(n):
       if(n<=1):
              return 1
       else:
              return fabisum(n-1) + fabisum(n-2)

@app22.route('/submit',methods=["POST"])
def index2():
       
       NUM2 = int(request.form.get("num2"))
       result1 = fabisum(NUM2)
       return "The fabi series of the number is: " + str(result1)

if __name__ == '__main__':
       app22.run(debug=True)