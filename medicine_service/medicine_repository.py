from bson import ObjectId
from pymongo import MongoClient
from nameko.extensions import DependencyProvider


class Repository(DependencyProvider):

    def setup(self):
        client = MongoClient()
        self.db = client.test_database

    def get_dependency(self, worker_ctx):
        return MedicineRepository(self.db)


class MedicineRepository:
    def __init__(self,db):
        self.medicines = db.medicines

    def save(self, medicine):
        medicine_id = self.medicines.insert_one(medicine).inserted_id
        return medicine_id

    def load(self, medicine_name):
        medicine = self.medicines.find_one({"name": medicine_name})
        return medicine
