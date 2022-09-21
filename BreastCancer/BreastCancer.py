from flask import Blueprint, render_template, request
from flask_cors import cross_origin
import pickle
import numpy as np

modelbc = pickle.load(open('pickle_files/BreastcancerRF.pkl', 'rb'))
BreastCancer_blueprint = Blueprint("BreastCancer",__name__,static_folder="static",template_folder='template')

@BreastCancer_blueprint.route("/BreastCancer",methods=['GET'])

def BreastCancer():
    return render_template("BreastCancer.html")


@BreastCancer_blueprint.route("/predictbc", methods=['GET', 'POST'])
def predictbc():
    if request.method == 'POST':
        radius_mean = float(request.form['radius_mean'])
        perimeter_mean = request.form['perimeter_mean']
        area_mean = float(request.form['area_mean'])
        concavity_mean = float(request.form['concavity_mean'])
        concave_points_mean = float(request.form['concave_points_mean'])

        input_lst = np.array([[radius_mean, perimeter_mean, area_mean, concavity_mean,concave_points_mean]],dtype=object)

        predbc= modelbc.predict(input_lst)

        output = predbc

        if output == 0:
            return render_template("Norisk.html")

        elif output == 1:
            return render_template("Risk.html")
