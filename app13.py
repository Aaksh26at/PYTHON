from flask import Flask, render_template, redirect, url_for, request

app13 = Flask(__name__)

@app13.route('/')
def index():
    return render_template("index3.html")

@app13.route('/result')
def result():
    # Get the values from the query parameters
    maths = int(request.args.get('maths'))
    science = int(request.args.get('science'))
    java = int(request.args.get('java'))

    # Calculate the average
    avg = (maths + science + java) / 3

    # Return the result
    return f"The average of the subjects is {avg}"

@app13.route('/avg')
def avg():
    # Get the values from the request
    maths = request.args.get('maths')
    science = request.args.get('science')
    java = request.args.get('java')

    # Redirect to the result route with the parameters
    return redirect(url_for('result', maths=maths, science=science, java=java))

if __name__ == '__main__':
    app13.run(debug=True)
