from flask import Flask,request,redirect,render_template,url_for

app12 = Flask(__name__)

@app12.route('/')
def welcome():
       return render_template("index2.html")

@app12.route('/submit')
def submit():
       return "All your task has been submitted"

@app12.route('/submit',methods = ["POST"])
def submit_page():
       Task1 = request.args.get('Task1')
       Task2 = request.args.get('Task2')
       Task3 = request.args.get('Task3')
       Task4 = request.args.get('Task4')
       
       return redirect(url_for('submit'))


if __name__ == '__main__':
       app12.run(debug=True)