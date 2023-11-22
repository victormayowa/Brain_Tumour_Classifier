#neuroscope/models.py
from . import db
from flask_login import UserMixin
from datetime import datetime
#patient model


class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    birthdate = db.Column(db.Date, nullable=False)
    contact_info = db.Column(db.String(100), nullable=False)
    # medical_history = db.Column(db.Text)

    def __repr__(self):
        return f"<Patient {self.first_name}>"
    
    def save(self):
        """
        The save function is used to save the changes made to a model instance.
        It takes in no arguments and returns nothing.

        :param self: Refer to the current instance of the class
        :return: The object that was just saved
        """
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """
        The delete function is used to delete a specific row in the database. It takes no parameters and returns nothing.

        :param self: Refer to the current instance of the class, and is used to access variables that belongs to the class
        :return: Nothing
        """
        db.session.delete(self)
        db.session.commit()

    def update(self, birthdate, contact_info):
        """
        The update function updates the title and description of a given blog post.
        It takes two parameters, title and description.

        :param self: Access variables that belongs to the class
        :param birthdate: Update the birthdate of the patient
        :param description: Update the contactinfo of the patient
        :return: A dictionary with the updated values
        """
        self.birthdate = birthdate
        self.contact_info = contact_info

        db.session.commit()

# user model

"""
class User:
    id:integer
    username:string
    email:string
    password:string
"""


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), nullable=False, unique=True)
    email = db.Column(db.String(80), nullable=False)
    password = db.Column(db.Text(), nullable=False)

    def __repr__(self):
        """
        returns string rep of object

        """
        return f"<User {self.username}>"

    def save(self):
        db.session.add(self)
        db.session.commit()