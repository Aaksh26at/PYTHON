from flask import Flask,render_template,redirect,url_for,request

app11 = Flask(__name__)


@app11.route('/')
def welcome():
       return render_template("index.html")

@app11.route('/thank_you/<sname>')
def thank_you(sname):
       return " Thanks for register " + str(sname)

@app11.route('/submit',methods=["POST"])
def submit_page():
  name = request.form.get("name")
  email = request.form.get("email")
  message = request.form.get("message")
  
  return redirect(url_for('thank_you',sname = name))

if __name__ == '__main__':
       app11.run(debug=True)