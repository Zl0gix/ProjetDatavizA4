from flask import Blueprint, render_template
import joblib

bp = Blueprint("restrictions", __name__)

@bp.route('/restrictions')
def restrictions():
    dic = joblib.load("flaskr/Backend/dic.joblib")

    res = []
    for k,v in dic.items():
        res.append(f"{k}:{v}")
    res = "\n".join(res)

    return render_template("restrictions.html")