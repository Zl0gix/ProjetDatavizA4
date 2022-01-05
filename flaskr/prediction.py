from flask import Blueprint

bp = Blueprint("prediction", __name__)

@bp.route('/prediction')
def prediction():
    return "Hello World!"