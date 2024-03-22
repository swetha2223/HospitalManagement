class Appointment:
    def __init__(self, appointment_id=None, patient_id=None, doctor_id=None, appointment_date=None, description=None):
        self.appointment_id = appointment_id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.appointment_date = appointment_date
        self.description = description

    def setappointment_id(self, appointment_id):
        self.appointment_id = appointment_id

    def getappointment_id(self):
        return self.appointment_id
    
    def setpatient_id(self, patient_id):
        self.patient_id = patient_id
    def getpatient_id(self):
        return self.patient_id


    def setdoctor_id(self, doctor_id):
        self.doctor_id = doctor_id
    def getdoctor_id(self):
        return self.doctor_id

    def setappointment_date(self, appointment_date):
        self.appointment_date = appointment_date
    def getappointment_date(self):
        return self.appointment_date

    def set_description(self, description):
        self.description = description
    def getdescription(self):
        return self.description
    def __str__(self):
        return f"Appointment ID: {self.appointment_id}, Patient ID: {self.patient_id}, Doctor ID: {self.doctor_id}, Date: {self.appointment_date}, Description: {self.description}"