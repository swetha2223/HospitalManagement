
import sys

sys.path.append("C:/Users/Swetha/Desktop/HospManagement/Entity")

import pyodbc
from abc import ABC, abstractmethod
from typing import List
from appointment import Appointment

class IHospitalService(ABC):

    @abstractmethod
    def getAppointmentById(self, appointmentId: int) -> Appointment:
        pass

    @abstractmethod
    def getAppointmentsForPatient(self, patientId: int) -> List[Appointment]:
        pass

    @abstractmethod
    def getAppointmentsForDoctor(self, doctorId: int) -> List[Appointment]:
        pass

    @abstractmethod
    def scheduleAppointment(self, appointment: Appointment) -> bool:
        pass

    @abstractmethod
    def updateAppointment(self, appointment: Appointment) -> bool:
        pass

    @abstractmethod
    def cancelAppointment(self, appointmentId: int) -> bool:
        pass

class HospitalServiceImpl(IHospitalService):
    def __init__(self):
        self.connection_string = self.get_connection_string()
        self.connection = pyodbc.connect(self.connection_string)
        self.cursor = self.connection.cursor()

    def get_connection_string(self):
        server_name = "LAPTOP-EDPN5EA9\\SQLEXPRESS"
        database_name = "HospitalManagement"
        trusted_connection = "yes"
        return f'Driver={{SQL Server}};Server={server_name};Database={database_name};Trusted_Connection={trusted_connection};'

    def getAppointmentById(self, appointmentId):
        self.cursor.execute("SELECT * FROM Appointment WHERE appointmentId = ?", (appointmentId,))
        appointment = self.cursor.fetchone()
        return appointment

    def getAppointmentsForPatient(self, patientId):
        self.cursor.execute("SELECT * FROM Appointment WHERE patientId = ?", (patientId,))
        appointments = self.cursor.fetchall()
        return appointments

    def getAppointmentsForDoctor(self, doctorId):
        self.cursor.execute("SELECT * FROM Appointment WHERE doctorId = ?", (doctorId,))
        appointments = self.cursor.fetchall()
        return appointments

    def scheduleAppointment(self, appointment):
        self.cursor.execute("INSERT INTO Appointment (patientId, doctorId, appointmentDate, description) VALUES (?, ?, ?, ?)",
                            (appointment.patientId, appointment.doctorId, appointment.appointmentDate, appointment.description))
        self.connection.commit()
        return True

    def updateAppointment(self, appointment):
        self.cursor.execute("UPDATE Appointment SET patientId = ?, doctorId = ?, appointmentDate = ?, description = ? WHERE appointmentId = ?",
                            (appointment.patientId, appointment.doctorId, appointment.appointmentDate, appointment.description, appointment.appointmentId))
        self.connection.commit()
        return True

    def cancelAppointment(self, appointmentId):
        self.cursor.execute("DELETE FROM Appointment WHERE appointmentId = ?", (appointmentId,))
        self.connection.commit()
        return True


