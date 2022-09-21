from flask import Blueprint,render_template,request
from flask_cors import cross_origin
import pickle
import numpy as np

modelpc = pickle.load(open('pickle_files/ProstateDecisionTree.pkl','rb'))
ProstateCancer_blueprint = Blueprint("ProstateCancer",__name__,static_folder="static",template_folder='template')

@ProstateCancer_blueprint.route("/ProstateCancer",methods=['GET'])

def ProstateCancer():
    return render_template("ProstateCancer.html")


@ProstateCancer_blueprint.route("/predictpc",methods=['GET','POST'])
def predictpc():
    if request.method == 'POST':
        radius = float(request.form['radius'])
        texture = float(request.form['texture'])
        perimeter = float(request.form['perimeter'])
        area = float(request.form['area'])
        smoothness = float(request.form['smoothness'])
        compactness = float(request.form['compactness'])
        symmetry = float(request.form['symmetry'])
        fractal_dimension = float(request.form['fractal_dimension'])

        input_lst = np.array([[radius, texture, perimeter, area, smoothness, compactness, symmetry,fractal_dimension]])


        predpc = modelpc.predict(input_lst)

        output = predpc

        if output == 0:
            return render_template("Norisk.html")

        elif output == 1:
            return render_template("Risk.html")
