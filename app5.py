from flask import Flask

app5 = Flask(__name__)

list = [23,45,67,89]

@app5.route('/check_number/<int:var3>')

def index3(var3):
       if var3 in list:
              return f"The  {var3} is present"
       else:
              return f"The {var3} is not present in the list"
       
if __name__ == '__main__':
       app5.run(debug=True)