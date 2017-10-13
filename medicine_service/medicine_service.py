import json
import logging
from bson.json_util import dumps
from nameko.rpc import rpc
from nameko.web.handlers import http

import medicine_repository
import schemas

logger = logging.getLogger(__name__)


class MedicineService():
    name = "medicine_service"
    repo = medicine_repository.Repository()

    @rpc
    @http('GET', '/medicines/<name>')
    def get_medicine(self, request, name):
        medicine = self.repo.load(name)
        return schemas.Medicine().dumps(dumps(medicine)).data

    @rpc
    @http('POST', '/medicines')
    def create_medicine(self, request):
        medicine = schemas.Medicine(strict=True).load(request.get_data(as_text=True)).data
        medicine_id = self.repo.save(medicine)
        output = 'Created medicine ' + medicine['name']
        return output
