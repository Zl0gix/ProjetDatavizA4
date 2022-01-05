from flask import Blueprint, render_template

bp = Blueprint("predictions", __name__)

@bp.route('/predictions')
def predictions():
    return render_template("predictions.html")