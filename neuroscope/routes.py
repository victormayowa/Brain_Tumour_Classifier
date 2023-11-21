# neuroscope/routes.py
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
from .auth import auth_ns, login_user, logout_user, authenticate_user
from .models import Patient
from .config import DevConfig
from .main import create_app

app = create_app(DevConfig)

@app.route("/")
def index():
    return app.send_static_file("index.html")

@app.errorhandler(404)
def not_found(err):
    return app.send_static_file("index.html")

@app.route('/patients')
def patient():
    patients = Patient.query.all()
    return render_template('patient.html', patients=patients)


@app.route('/submit', methods=['POST'])
def submit():
    # Retrieve form data
    first_name = request.form.get('firstName')
    last_name = request.form.get('lastName')
    birthdate_str = request.form.get('birthdate')
    contact_info = request.form.get('contactInfo')

    # Convert birthdate string to a date object
    birthdate = datetime.strptime(birthdate_str, '%Y-%m-%d').date()
    # Create a Patient object
    patient = Patient(first_name=first_name, last_name=last_name, birthdate=birthdate, contact_info=contact_info)

    # Add the patient to the database
    patient.save()
    #db.session.add(patient)
    #db.session.commit()

    return redirect(url_for('index'))


@app.route("/login", methods=['POST'])
def login():
    data = request.form
    username = data.get("username")
    password = data.get("password")

    user = authenticate_user(username, password)

    if user:
        # Successful login
        login_user(user)
        return redirect(url_for("index"))
    else:
        # Failed login
        return render_template("login.html", message="Invalid username or password")

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))