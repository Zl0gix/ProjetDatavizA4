from flaskr import BEST_MODEL
from flask import Blueprint, request
from joblib import load

bp = Blueprint("prediction", __name__)

@bp.route('/prediction')
def prediction():
    if 'model' in request.args.keys():
        model = load("Backend/models/"+request.args['model']+".joblib")
    else:
        model = load("Backend/models/"+BEST_MODEL+".joblib")

    mandatory = [""]
    for item in mandatory:
        if item not in request.args.keys():
            return ""

    return str(list(request.args.keys()) + list(request.args.values()))