import os

import joblib
from flaskr import BEST_MODEL
from flask import Blueprint, request, abort
from joblib import load
import pandas as pd
import numpy as np

bp = Blueprint("prediction", __name__)

@bp.route('/prediction')
def prediction():
    if 'model' in request.args.keys():
        model = load("flaskr/Backend/models/"+request.args['model']+".joblib")
    else:
        model = load("flaskr/Backend/models/"+BEST_MODEL+".joblib")

    mandatory = [
        'gender', 
        'age', 
        'admission_type_id', 
        'discharge_disposition_id',
        'admission_source_id', 
        'time_in_hospital', 
        'medical_specialty',
        'num_lab_procedures', 
        'num_procedures',
        'num_medications',
        'number_outpatient', 
        'number_emergency', 
        'number_inpatient', 
        'diag_1',
        'diag_2', 
        'diag_3', 
        'number_diagnoses', 
        'A1Cresult', 
        'metformin',
        'repaglinide', 
        'nateglinide', 
        'chlorpropamide', 
        'glimepiride',
        'acetohexamide', 
        'glipizide', 
        'glyburide', 
        'tolbutamide',
        'pioglitazone', 
        'rosiglitazone', 
        'acarbose', 
        'miglitol', 
        'troglitazone',
        'tolazamide', 
        'examide', 
        'citoglipton', 
        'insulin',
        'glyburide-metformin', 
        'glipizide-metformin',
        'glimepiride-pioglitazone', 
        'metformin-rosiglitazone',
        'metformin-pioglitazone', 
        'change', 
        'diabetesMed'
    ]
    for item in mandatory:
        if item not in request.args.keys():
            abort(400)

    arr = []
    for k in mandatory:
        arr.append(request.values[k])

    if 'to_format' in request.args.keys():
        dic = joblib.load("flaskr/Backend/dic.joblib")
        for k, v in dic.items():
            arr[mandatory.index(k)] = v.index(arr[mandatory.index(k)])

    return str(model.predict(np.array(arr).reshape(1, -1))[0])