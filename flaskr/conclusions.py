from flask import Blueprint, render_template

bp = Blueprint("conclusions", __name__)

@bp.route('/conclusions')
def conclusions():
    return render_template("conclusions.html")