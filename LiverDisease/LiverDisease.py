from flask import Blueprint,render_template,request
from flask_cors import cross_origin
import pickle
import numpy as np

model = pickle.load(open('pickle_files/liverdiseaseXGB.pkl','rb'))

LiverDisease_blueprint = Blueprint("LiverDisease",__name__,static_folder="static",template_folder='template')

@LiverDisease_blueprint.route("/LiverDisease",methods=['GET'])

def LiverDisease():
    return render_template("LiverDisease.html")

@LiverDisease_blueprint.route("/predict",methods=['GET','POST'])
def predict():
    if request.method == 'POST':


        Age = request.form['Age']
        Total_Bilirubin = float(request.form['Total_Bilirubin'])
        Direct_Bilirubin = float(request.form['Direct_Bilirubin'])
        Alkaline_Phosphotase = float(request.form['Alkaline_Phosphotase'])
        Alamine_Aminotransferase = float(request.form['Alamine_Aminotransferase'])
        Aspartate_Aminotransferase = float(request.form['Aspartate_Aminotransferase'])
        Total_Protiens = float(request.form['Total_Protiens'])
        Albumin = float(request.form['Albumin'])
        Albumin_and_Globulin_Ratio = float(request.form['Albumin_and_Globulin_Ratio'])
        Gender = float(request.form['Gender'])

        input_lst = np.array([[Age, Total_Bilirubin, Direct_Bilirubin, Alkaline_Phosphotase, Alamine_Aminotransferase, Aspartate_Aminotransferase, Total_Protiens,Albumin,Albumin_and_Globulin_Ratio,Gender]], dtype=object)


        pred = model.predict(input_lst)

        output = pred

        if output == 0:
            return render_template("Norisk.html")

        elif output == 1:
            return render_template("Risk.html")

