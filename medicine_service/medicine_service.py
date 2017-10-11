import json

from bson.json_util import dumps
from nameko.rpc import rpc
from nameko.web.handlers import http

from medicine_service import medicine_repository


class MedicineService():
    name = "medicine_service"
    repo = medicine_repository.Repository()

    @rpc
    @http('GET', '/medicines/<name>')
    def get_medicine(self, request, name):
        medicine = self.repo.load(name)
        return dumps(medicine)

    @rpc
    @http('POST', '/medicines')
    def create_medicine(self, request):
        medicine = json.loads(request.get_data(as_text=True))
        medicine_id = self.repo.save(medicine)
        output = 'Created medicine ' + medicine['name']
        return output
