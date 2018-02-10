from flask import Flask,request,render_template

app=Flask(__name__)

@app.route('/potato')
def welcome():
    return 'This is my first Flask App!'

@app.route('/',methods=['GET','POST'])
def rootpage():
    name=''
    food=''
    if request.method=='POST' and 'username' in request.form:
        name=request.form.get('username')
        food=request.form.get('userfood')
    return render_template('index.html',name=name,food=food)

@app.route('/bmi',methods=['GET','POST'])
def bmi_calculator():
    weight=''
    inches=''
    BMI=''
    if request.method=='POST' and 'userweight' in request.form:
        weight=request.form.get('userweight')
        inches=request.form.get('userinches')
        BMI=round((int(weight)*0.45)/((int(inches)*0.025)**2),2)
    return render_template('bmi.html',weight=weight,inches=inches,BMI=BMI)



# @app.route('/method',methods=['GET','POST'])
# def method():
#     if request.method=='POST':
#         return "You've used a POST request"
#     else:
#         return "You are using a GET request"



app.run()
