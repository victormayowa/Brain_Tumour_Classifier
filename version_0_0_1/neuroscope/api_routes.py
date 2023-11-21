#neuroscope/api_routes.py
from flask_restx import Namespace, Resource, fields
from .models import Patient
from flask_jwt_extended import jwt_required
from flask import request


patient_ns = Namespace("patient", description="A namespace for Patients")


patient_model = patient_ns.model(
    "Patient",
    {"id": fields.Integer(), "username": fields.String(), "first_name": fields.String(), "last_name": fields.String(), "birthdate": fields.Date(), "contact_info": fields.String()},
)


@patient_ns.route("/hello")
class HelloResource(Resource):
    def get(self):
        return {"message": "Hello Patients"}


@patient_ns.route("/patients")
class PatientsResource(Resource):
    @patient_ns.marshal_list_with(patient_model)
    def get(self):
        """Get all recipes"""

        patients = Patient.query.all()

        return patients

    @patient_ns.marshal_with(patient_model)
    @patient_ns.expect(patient_model)
    @jwt_required()
    def post(self):
        """Create a new recipe"""

        data = request.get_json()

        new_patient = Patient(
            first_name=data.get("first_name"),last_name=data.get("last_name")
        )

        new_patient.save()

        return new_patient, 201


@patient_ns.route("/patient/<int:id>")
class PatientResource(Resource):
    @patient_ns.marshal_with(patient_model)
    def get(self, id):
        """Get a recipe by id"""
        patient = Patient.query.get_or_404(id)

        return patient

    @patient_ns.marshal_with(patient_model)
    @jwt_required()
    def put(self, id):
        """Update a recipe by id"""

        patient_to_update = Patient.query.get_or_404(id)

        data = request.get_json()

        patient_to_update.update(data.get("first_name"), data.get("last_name"))

        return patient_to_update

    @patient_ns.marshal_with(patient_model)
    @jwt_required()
    def delete(self, id):
        """Delete a recipe by id"""

        patient_to_delete = Patient.query.get_or_404(id)

        patient_to_delete.delete()

        return patient_to_delete