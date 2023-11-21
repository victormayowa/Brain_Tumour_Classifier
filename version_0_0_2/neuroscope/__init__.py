from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from .config import Config



db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
mail = Mail()

from .models import User

@login_manager.user_loader
def load_user(user_id):
    # This function should return the user object or None if not found
    return User.query.get(int(id))

def create_app(config_class):
    app = Flask(__name__, static_folder="static", static_url_path="/static")
    app.config.from_object(config_class)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from .routes import main
    app.register_blueprint(main)
    return app