from flask import Flask,render_template,request
import pickle
app=Flask(__name__)
model=pickle.load(open('regression.pkl','rb'))

@app.route('/')
def intro():
    return render_template('index.html')

@app.route('/login', methods =["POST"])
def login():
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
    return render_template('index.html',label="The performance of the car is "+str(p))
if(__name__=='__main__') :
    app.run(debug = True,port=9000)
     
