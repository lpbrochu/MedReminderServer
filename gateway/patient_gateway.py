from bson.json_util import dumps
from nameko.events import EventDispatcher
from nameko.web.handlers import http

import action_repository


class PatientActions:
    name = "patient_actions"

    dispatch = EventDispatcher()
    repo = action_repository.Repository()

    @http('POST', '/gateway/create_new_patient')
    def create_new_patient(self, request):
        new_patient = request.get_data(as_text=True)

        action = {}
        action['name'] = 'create_new_patient'
        action['status'] = 'IN_PROGRESS'
        action['payload'] = new_patient
        action_id = self.repo.save(action)
        self.dispatch('create_new_patient', action)
        return action_id

    @http('GET', '/gateway/create_new_patient/<action_id>')
    def get_status(self, request, action_id):
        action = self.repo.load(action_id)
        return dumps(action)

# @http('GET', '/patients/<patient_id>/medicines')
# def get_patient_medicines(self, request, patient_id):
#     patient = self.repo.load(patient_id)
#     return dumps(patient.medicines)
#
#
# @http('POST', '/patients')
# def create_patient(self, request):
#     patient = json.loads(request.get_data(as_text=True))
#     patient_id = self.repo.save(patient)
#     output = 'Created patient ' + patient['name'] + ' with id: ' + dumps(patient_id)
#     return output
