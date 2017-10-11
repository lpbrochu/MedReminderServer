from bson import ObjectId
from pymongo import MongoClient
from nameko.extensions import DependencyProvider


class Repository(DependencyProvider):

    def setup(self):
        client = MongoClient()
        self.db = client.test_database

    def get_dependency(self, worker_ctx):
        return PatientRepository(self.db)


class PatientRepository:
    def __init__(self,db):
        self.patients = db.patients

    def save(self, patient):
        patient_id = self.patients.insert_one(patient).inserted_id
        return patient_id

    def load(self, patient_id):
        patient = self.patients.find_one({"_id": ObjectId(patient_id)})
        return patient

    def search_one(self, patient_name):
        patient = self.patients.find_one({"name": patient_name})
        return patient