from flask import Flask
import config 

def create_app():
    app = Flask(__name__)

    from .routes import bp as main_bp
    app.register_blueprint(main_bp)

    return app
