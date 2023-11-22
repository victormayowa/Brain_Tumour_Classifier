from .models import User
from werkzeug.security import check_password_hash

def authenticate_user(username, password):
    # Query the database to find the user with the provided username
    user = User.query.filter_by(username=username).first()

    # Check if the user exists and the provided password is correct
    if user and check_password_hash(user.password, password):
        return user  # Return the user object if authentication is successful
    else:
        return None  # Return None if authentication fails
    