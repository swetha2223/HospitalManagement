
import pyodbc

class PropertyUtil:
    @staticmethod
    def getPropertyString():
        server_name = "LAPTOP-EDPN5EA9\\SQLEXPRESS"
        database_name = "HospitalManagement"
        trusted_connection = "yes"
        return f"Driver={{SQL Server}};Server={server_name};Database={database_name};Trusted_Connection={trusted_connection};"



