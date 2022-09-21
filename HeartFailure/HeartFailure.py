from flask import Blueprint, render_template, request
from flask_cors import cross_origin
import pickle
import numpy as np

modelhf = pickle.load(open('pickle_files/HeartfailurKNN.pkl', 'rb'))

HeartFailure_blueprint = Blueprint("HeartFailure", __name__, static_folder="static", template_folder='template')


@HeartFailure_blueprint.route("/HeartFailure", methods=['GET'])
def HeartFailure():
    return render_template("HeartFailure.html")


@HeartFailure_blueprint.route("/predicthf", methods=['GET', 'POST'])
def predicthf():
    if request.method == 'POST':
        Age = request.form['Age']
        ChestPainType = float(request.form['ChestPainType'])
        RestingBP = request.form['RestingBP']
        Cholesterol = float(request.form['Cholesterol'])
        FastingBS = float(request.form['FastingBS'])
        RestingECG = float(request.form['RestingECG'])
        MaxHR = float(request.form['MaxHR'])
        Oldpeak = float(request.form['Oldpeak'])
        Gender = float(request.form['Gender'])
        ExerciseAngina = float(request.form['ExerciseAngina'])

        input_lst = np.array(
            [[Age, ChestPainType, RestingBP, Cholesterol, FastingBS,RestingECG, MaxHR, Oldpeak, Gender, ExerciseAngina]],
            dtype=object)

        predhf= modelhf.predict(input_lst)

        output = predhf

        if output == 0:
            return render_template("Norisk.html")

        elif output == 1:
            return render_template("Risk.html")
