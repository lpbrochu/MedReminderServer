from nameko.containers import ServiceContainer

# create a container
from gateway.PatientActions import PatientActions
from medicine_service.medicine_service import MedicineService
from patient_service.patient_service import PatientService

container = ServiceContainer(PatientService, config={'AMQP_URI': 'pyamqp://guest:guest@localhost'})

# ``container.extensions`` exposes all extensions used by the service
service_extensions = list(container.extensions)

# start service
container.start()