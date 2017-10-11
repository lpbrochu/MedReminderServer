from bson import ObjectId
from pymongo import MongoClient
from nameko.extensions import DependencyProvider


class Repository(DependencyProvider):

    def setup(self):
        client = MongoClient()
        self.db = client.test_database

    def get_dependency(self, worker_ctx):
        return ActionRepository(self.db)


class ActionRepository:
    def __init__(self,db):
        self.actions = db.actions

    def save(self, action):
        action_id = self.actions.insert_one(action).inserted_id
        return action_id

    def load(self, action_id):
        action = self.actions.find_one({"_id": ObjectId(action_id)})
        return action