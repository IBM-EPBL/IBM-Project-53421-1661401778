import numpy as np
from flask import Flask,request,jsonify,render_template
import request
import json
API_KEY="HEiDudCYxnCSUXVZnh0YbyeSb7v9r9qqECxOQ9ASyXKI"
token_response=request.post("https://us-south.ml.cloud.ibm.com/identity/token",data={"apikey":API_KEY,"grant_type":"client_credentials"}
mltoken=token_response.json()["access_token"]
print("mltoken",mltoken)  
header={'content-type':'application/json','Authorization':'Bearer'+ mltoken}                           
import pickle
app=Flask(__name__)
model=pickle.load(open('regression.pkl','rb'))

@app.predict('/')
def intro():
    return render_template('index.html')

@app.route('/y_predict', methods =["POST"])
def y_predict():
    cyl=request.form["input1"]
    dis=request.form["input2"]
    hp=request.form["input3"]
    w=request.form["input4"]
    a=request.form["input5"]
    my=request.form["input6"]
    ori=request.form["input7"]
    total=[[int(cyl),int(dis),int(hp),int(w),int(a),int(my),int(ori)]]


    p=model.predict(total)
    p=p[0]
    return render_template('index.html',prediction_text=p,label="The performance of the car is ".format(p))
if(__name__=='__main__') :
    app.run(debug = True,port=9000)
     
