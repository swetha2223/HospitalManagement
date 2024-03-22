class Doctor:
    def __init__(self, doctor_id, first_name, last_name, specialization, contact_number):
        self.doctor_id = doctor_id
        self.first_name = first_name
        self.last_name = last_name
        self.specialization = specialization
        self.contact_number = contact_number

    def setdoctor_id(self, doctor_id):
        self.doctor_id = doctor_id
        
    def getdoctor_id(self):
        return self.doctor_id

    def setfirst_name(self, first_name):
        self.first_name = first_name
    def getfirst_name(self):
        return self.first_name

    def setlast_name(self, last_name):
        self.last_name = last_name
    def getlast_name(self):
        return self.last_name

    def setspecialization(self, specialization):
        self.specialization = specialization
    def getspecialization(self):
        return self.specialization

    def setcontact_number(self, contact_number):
        self.contact_number = contact_number

    def getcontact_number(self):
        return self.contact_number

    def __str__(self):
        return f"Doctor ID: {self.doctor_id}, Name: {self.first_name} {self.last_name}, Specialization: {self.specialization}, Contact: {self.contact_number}"