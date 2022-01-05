from flask import Blueprint, render_template

bp = Blueprint("model", __name__)

@bp.route('/model')
def model():
    return render_template("model.html")