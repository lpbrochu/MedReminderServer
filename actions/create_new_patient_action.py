from nameko.events import event_handler, BROADCAST


class CreateNewPatientAction:
    name = "create_new_patient_action"

    @event_handler(
        "monitor", "create_new_patient", handler_type=BROADCAST, reliable_delivery=False
    )
    def handleEvent(self, action):
        patient = action['payload']
        print("patient received! " + patient)
