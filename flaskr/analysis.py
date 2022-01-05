from flask import Blueprint, render_template

bp = Blueprint("analysis", __name__)

@bp.route('/analysis')
def analysis():
    return render_template("analysis.html")