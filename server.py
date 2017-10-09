from bottle import route, run, template, request
from bson.json_util import dumps
from repository import Repository

import json

repo = Repository()


@route('/patients/<patient_id>', method='GET')
def get_patient(patient_id):
    patient = repo.load(patient_id)
    return dumps(patient)


@route('/patients', method='POST')
def create_patient():
    patient = json.loads(request.body.read().decode("utf-8"))
    patient_id = repo.save(patient)
    output = template('<b>Created patient {{name}}, id is {{patient_id}}</b>!', name=patient['name'],
                      patient_id=patient_id)
    return output


run(host='localhost', port=8080, debug=True)