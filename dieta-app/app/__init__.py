# -*- coding: utf-8 -*-
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.secret_key = "dieta-app-local-secret"

    from .routes import bp
    app.register_blueprint(bp)

    return app
