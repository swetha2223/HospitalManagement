class Patient:
    def __init__(self, patient_Id, first_name, last_name, date_of_birth, gender,  contact_number, address):
        self.patient_id = patient_Id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.contact_number = contact_number
        self.address = address

    def setpatient_id(self, patient_id):
        self.patient_id = patient_id
    def getpatient_id(self):
        return self.patient_id
    
    def setfirst_name(self, first_name):
        self.first_name = first_name
    def getfirst_name(self):
        return self.first_name
        
    def setlast_name(self, last_name):
        self.last_name = last_name
    def getlast_name(self):
        return self.last_name
    
    def setdate_of_birth(self, date_of_birth):
        self.date_of_birth = date_of_birth
    def getdate_of_birth(self):
        return self.date_of_birth
    
    def setgender(self, gender):
        self.gender = gender
    def getgender(self):
        return self.gender
    
    def setcontact_number(self, contact_number):
        self.contact_number = contact_number
    def get_contact_number(self):
        return self.contact_number
    
    def get_address(self):
        return self.__address

    def __str__(self):
        return f"Patient ID: {self.patient_id}, Name: {self.first_name} {self.last_name}, DOB: {self.date_of_birth}, Gender: {self.gender}, Contact: {self.contact_number}, Address: {self.address}"