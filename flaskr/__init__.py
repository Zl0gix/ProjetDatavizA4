import os

from flask import Flask

BEST_MODEL = 'SupportVector'

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # There will be a blueprint for each page

    from . import index
    app.register_blueprint(index.bp)
    app.add_url_rule('/', endpoint='index')

    from . import restrictions
    app.register_blueprint(restrictions.bp)

    from . import prediction
    app.register_blueprint(prediction.bp)

    return app