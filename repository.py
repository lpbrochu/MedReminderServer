from bson import ObjectId
from pymongo import MongoClient


class Repository:
    client = MongoClient()
    db = client.test_database
    patients = db.patients

    def save(self, patient):
        patient_id = self.patients.insert_one(patient).inserted_id
        return patient_id

    def load(self, patient_id):
        patient = self.patients.find_one({"_id": ObjectId(patient_id)})
        return patient
