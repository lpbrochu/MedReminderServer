import json

from bottle import Bottle, request, template
from bson.json_util import dumps

from medicine_repository import MedicineRepository

repo = MedicineRepository()
medicine_service = Bottle()


@medicine_service.route('/patients/<patient_id>', method='GET')
def get_patient(patient_id):
    patient = repo.load(patient_id)
    return dumps(patient)


@medicine_service.route('/patients', method='POST')
def create_patient():
    patient = json.loads(request.body.read().decode("utf-8"))
    patient_id = repo.save(patient)
    output = template('<b>Created patient {{name}}, id is {{patient_id}}</b>!', name=patient['name'],
                      patient_id=patient_id)
    return output


@medicine_service.route('/patients', method='GET')
def search_patient():
    name = request.query['name']
    output = None

    if name is not None:
        patient = repo.search_one(name)

        if patient is not None:
            output = template('<b>Found patient {{name}}, it is {{patient}}</b>!', name=patient['name'], patient=dumps(patient))

    if output is None:
        output = template('Nothing found for patient {{name}}', name=name)

    return output


