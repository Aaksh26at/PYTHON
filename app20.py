from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculate_sum():
    if request.method == 'POST':
        n = int(request.form['num'])
        sum = n * (n + 1) // 2
        return render_template('result.html', result=sum)
    else:
        return render_template('index7.html')

if __name__ == '__main__':
    app.run(debug=True)