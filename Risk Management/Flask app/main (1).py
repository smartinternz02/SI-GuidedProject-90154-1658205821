import pandas as pd
from flask import Flask,render_template,request
app = Flask(__name__)
import pickle,joblib
model = pickle.load(open('model.pkl','rb'))
ct=joblib.load("ct")
@app.route('/')
def helloworld():
    return render_template("base.html")
@app.route('/assesment', methods=["POST","GET"])
def prediction():
    return render_template("index1.html")
@app.route('/model',methods=['POST'])
def admin():
    #values=[[x for x in request.form.values()]]
    names=["Age","Sex","Job","Housing","Saving accounts","Checking account","Credit amount","Duration","Purpose"]

    sex= request.form["Sex"]

    housing= request.form["Housing"]

    job = request.form["Job"]

    saving_account = request.form["Saving accounts"]

    checking_account=request.form["Checking account"]

    credit_amount=request.form["Credit amount"]
    duration=request.form["Duration"]
    purpose=request.form["Purpose"]
    age=request.form["Age"]
    values=[[age,sex,job,housing,saving_account,checking_account,credit_amount,duration,purpose]]

    #y=[[int(x1),int(x2),int(x3),int(x4),int(x5),int(x6),int(x7),int(x8),int(r1),int(r2),int(r3),int(t1),int(t2),int(t3),int(t4),int(t5),int(u1),int(u2),int(u3),int(u4)]]
    #x=le.transform([sex,housing,checking_account,purpose,saving_account])
    #print(x)
    data=pd.DataFrame(values,columns=names)
    data=ct.transform(data)
    #le_cols = ["Sex", "Housing", "Checking account", "Purpose","Saving accounts"]
    #le.transform(data[le_cols])
    a = model.predict(data)
    if (a[0]==0):
        b="Bad"
        return render_template("predbad.html",z=b)
    if (a[0]==1):
        b ="Good"
        return render_template("predgood.html",z=b)

if __name__=='__main__':
    app.run(debug = True)