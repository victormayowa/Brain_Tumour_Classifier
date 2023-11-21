# neuroscope/routes.py
from datetime import datetime
from flask import render_template, request, redirect, url_for, Blueprint
from .auth import authenticate_user
from flask_login import login_user, logout_user
from .models import Patient
#from .config import DevConfig
#from .main import create_app

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def home():
    return render_template('home.html')

# About route
@main.route('/about')
def about():
    return render_template('about.html')

# Upload route
@main.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Process the uploaded file if needed
        pass
    return render_template('upload.html')

# Dashboard route
@main.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# Analysis route
@main.route('/analysis')
def analysis():
    return render_template('analysis.html')

# Reports route
@main.route('/reports')
def reports():
    return render_template('reports.html')


@main.route('/patients')
def patient():
    patients = Patient.query.all()
    return render_template('patient.html', patients=patients)


@main.route('/submit', methods=['POST'])
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


@main.route("/login", methods=['POST'])
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

@main.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))