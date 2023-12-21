from flask import Flask
import pickle 

app = Flask(__name__)

@app.route("/") #first endpoint
def hello():
    return ("Hello world")

@app.route("/Page2") #second page (set FLASK_DEBUG=1)
def page2():
    return ("This is page2")

@app.route("/MODEL")
def model_api():
    return ("1")

@app.route("/nextpage")
def next_page():
    return ("2")


app.run()