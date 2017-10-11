from bson import ObjectId
from pymongo import MongoClient


class MedicineRepository:
    client = MongoClient()
    db = client.test_database
    medicines = db.medicine

    def save(self, medicine):
        medicine_id = self.medecines.insert_one(medicine).inserted_id
        return medicine_id

    def load(self, medicine_id):
        medicine = self.medecines.find_one({"_id": ObjectId(medicine_id)})
        return medicine

    def search_one(self, medicine_name):
        medicine = self.medecines.find_one({"name": medicine_name})
        return medicine
