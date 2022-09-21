from flask import Blueprint, render_template, request
from flask_cors import cross_origin
import pickle
import numpy as np

modelbs = pickle.load(open('pickle_files/strokeADB.pkl', 'rb'))

BrainStroke_blueprint = Blueprint("BrainStroke",__name__,static_folder="static",template_folder='template')

@BrainStroke_blueprint.route("/BrainStroke",methods=['GET'])

def BrainStroke():
    return render_template("BrainStroke.html")


@BrainStroke_blueprint.route("/predictbs", methods=['GET', 'POST'])
def predictbs():
    if request.method == 'POST':
        age = request.form['age']
        hypertension = float(request.form['hypertension'])
        heart_disease = float(request.form['heart_disease'])
        avg_glucose_level = float(request.form['avg_glucose_level'])
        bmi = float(request.form['bmi'])
        smoking_status = float(request.form['smoking_status'])
        gender = float(request.form['gender'])

        input_lst = np.array([[age, hypertension, heart_disease, avg_glucose_level,bmi,smoking_status,gender]],dtype=object)

        predbs= modelbs.predict(input_lst)

        output = predbs

        if output == 0:
            return render_template("Norisk.html")

        elif output == 1:
            return render_template("Risk.html")
