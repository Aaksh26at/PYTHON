from flask import Flask, request

app9 = Flask(__name__)

@app9.route('/example')
def example():
    name1 = request.args.get('name1')
    name2 = request.args.get('name2')
    return f'param1: {name1}, param2: {name2}'

if __name__ == '__main__':
    app9.run(debug=True)
