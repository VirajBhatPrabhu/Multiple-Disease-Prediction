from flask import Flask,render_template,url_for,request,jsonify
from flask import Blueprint
from flask_cors import cross_origin
import pandas as pd
import numpy as np
from BrainStroke.BrainStroke import BrainStroke_blueprint
from BreastCancer.BreastCancer import BreastCancer_blueprint
from ProstateCancer.ProstateCancer import ProstateCancer_blueprint
from Diabetes.Diabetes import Diabetes_blueprint
from HeartFailure.HeartFailure import HeartFailure_blueprint
from LiverDisease.LiverDisease import LiverDisease_blueprint



app = Flask(__name__, template_folder="template")

app.register_blueprint(BrainStroke_blueprint, url_prefix="")
app.register_blueprint(BreastCancer_blueprint, url_prefix="")
app.register_blueprint(ProstateCancer_blueprint, url_prefix="")
app.register_blueprint(Diabetes_blueprint, url_prefix="")
app.register_blueprint(HeartFailure_blueprint, url_prefix="")
app.register_blueprint(LiverDisease_blueprint, url_prefix="")




@app.route("/",methods= ['GET'])
@cross_origin()
def index():
    return render_template('index.html')

@app.route("/Home",methods= ['GET'])
@cross_origin()
def Home():
    return render_template('Home.html')

@app.route("/About",methods= ['GET'])
@cross_origin()
def About():
    return render_template('About.html')

if __name__ == '__main__':
    app.run(debug=True)