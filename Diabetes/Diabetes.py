from flask import Blueprint, render_template, request
from flask_cors import cross_origin
import pickle
import numpy as np

modeldia = pickle.load(open('pickle_files/DiabetesADB.pkl', 'rb'))


Diabetes_blueprint = Blueprint("Diabetes",__name__,static_folder="static",template_folder='template')

@Diabetes_blueprint.route("/Diabetes",methods=['GET'])

def Diabetes():
    return render_template("Diabetes.html")


@Diabetes_blueprint.route("/predictdia", methods=['GET', 'POST'])
def predictdia():
    if request.method == 'POST':
        Pregnancies = request.form['Pregnancies']
        Glucose = float(request.form['Glucose'])
        BloodPressure = request.form['BloodPressure']
        SkinThickness = float(request.form['SkinThickness'])
        Insulin = float(request.form['Insulin'])
        BMI = float(request.form['BMI'])
        DiabetesPedigreeFunction = float(request.form['DiabetesPedigreeFunction'])
        Age = request.form['Age']

        input_lst = np.array(
            [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,BMI, DiabetesPedigreeFunction, Age]],
            dtype=object)

        preddia= modeldia.predict(input_lst)

        output = preddia

        if output == 0:
            return render_template("Norisk.html")

        elif output == 1:
            return render_template("Risk.html")
