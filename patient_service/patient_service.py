import json

from bson.json_util import dumps
from nameko.rpc import rpc

import patient_repository


class PatientService():
    name = "patient_service"
    repo = patient_repository.Repository()

    @rpc
    def get_patient(self, request, patient_id):
        patient = self.repo.load(patient_id)
        return dumps(patient)

    @rpc
    def get_patient_medicines(self, request, patient_id):
        patient = self.repo.load(patient_id)
        return dumps(patient.medicines)

    @rpc
    def create_patient(self, request):
        patient = json.loads(request.get_data(as_text=True))
        patient_id = self.repo.save(patient)
        output = 'Created patient ' + patient['name'] + ' with id: ' + dumps(patient_id)
        return output
