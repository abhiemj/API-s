from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

q = ""

@app.route("/")
def loadpage():
    return render_template('home.html', query="") # to run the home template , it should be in templates folder


@app.route("/",methods=["POST"])
def diabetesprediction():
    inputQuery1 = request.form['query1']
    inputQuery2 = request.form['query2']
    inputQuery3 = request.form['query3']
    inputQuery4 = request.form['query4']
    inputQuery5 = request.form['query5']
    inputQuery6 = request.form['query6']
    inputQuery7 = request.form['query7']
    inputQuery8 = request.form['query8']
    
    model = pickle.load(open("diabetes_model.sav",'rb'))
    input_list = [inputQuery1,inputQuery2,inputQuery3,inputQuery4,inputQuery5,inputQuery6,inputQuery7,inputQuery8]

    response = model.predict([input_list])
    
    if response == 1:
        o1 = "patient is Diabetic"
    else:
        o1 = "patient is non diabetic"
    return render_template("home.html",output1=o1,query1 = request.form['query1'], query2 = request.form['query2'],query3 = request.form['query3'],query4 = request.form['query4'],query5 = request.form['query5'],query6 = request.form['query6'],query7=request.form['query7'],query8=request.form['query8'])

app.run()