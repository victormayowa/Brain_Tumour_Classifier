from flask import Flask
from flask_restx import Api
from .models import Patient, User
from . import db
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from .routes import app as frontend_app
from .api_routes import patient_ns
from .auth import auth_ns
from flask_cors import CORS


def create_app(config):
    app = Flask(__name__, template_folder='templates', static_url_path="/", static_folder="static")
    app.config.from_object(config)

    CORS(app)

    db.init_app(app)

    migrate = Migrate(app, db)
    JWTManager(app)

    api = Api(app, doc="/docs")

    api.add_namespace(patient_ns)
    api.add_namespace(auth_ns)
     # Add frontend routes
    app.register_blueprint(frontend_app)


    # model (serializer)
    @app.shell_context_processor
    def make_shell_context():
        return {"db": db, "Patient": Patient, "user": User}

    return app