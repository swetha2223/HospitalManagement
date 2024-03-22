import sys

sys.path.append("C:/Users/Swetha/Desktop/HospManagement/dao")
from HospitalService import HospitalServiceImpl, Appointment

class MainModule:
    def main(self):
        hospital_service = HospitalServiceImpl()


        appointment_id = int(input("Enter appointment ID: "))
        
        appointment = hospital_service.getAppointmentById(appointment_id)
        
        if appointment:
            print("Patient ID:", appointment.patientId)
            print("Appointment Date:", appointment.appointmentDate)
            print("Doctor ID:", appointment.doctorId)
            print("Description:", appointment.description)


            appointments_for_patient = hospital_service.getAppointmentsForPatient(appointment.patientId)
            print("\nAppointments for Patient:")
            for appt in appointments_for_patient:
                status = "Scheduled" if appt.appointmentId == appointment_id else "Updated" if appt.appointmentId == appointment_id else "Canceled" if appt.appointmentId == appointment_id else "Unknown"
                print(f"Appointment ID: {appt.appointmentId},  Status: {status}")

            appointments_for_doctor = hospital_service.getAppointmentsForDoctor(appointment.doctorId)
            print("\nAppointments for Doctor:")
            for appt in appointments_for_doctor:
                status = "Scheduled" if appt.appointmentId == appointment_id else "Updated" if appt.appointmentId == appointment_id else "Canceled" if appt.appointmentId == appointment_id else "Unknown"
                print(f"Appointment ID: {appt.appointmentId}, Status: {status}")
        else:
            print("Appointment not found for ID:", appointment_id)

    def new_method(self):
        return HospitalServiceImpl()

if __name__ == "__main__":
    MainModule().main()

