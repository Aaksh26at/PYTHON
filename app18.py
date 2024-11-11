from flask import Flask,render_template,request

app18 = Flask(__name__)

list1 = []


@app18.route('/')
def index():
       return render_template("index5.html")

@app18.route('/submit', methods=['POST'])
def submit():

     num1 = int(request.form.get('NUM1'))
     num2 = int(request.form.get('NUM2'))
     num3 = int(request.form.get('NUM3'))
     num4 = int(request.form.get('NUM4'))
     num5 = int(request.form.get('NUM5'))
     
     list1.append(num1)
     list1.append(num2)
     list1.append(num3)
     list1.append(num4)
     list1.append(num5)
     
     count = 0
     count1 = 0
     for i in list1:
            if i%2==0:
                   count+=1
            else:
                   count1+=1
     return  (f"The count of the even number is: "+str(count),
              f"The count of the odd numbers is: "+str(count1))

       
                 

     
            
if __name__ == '__main__':
       app18.run(debug=True)