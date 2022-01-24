from .userDB import UserDatabase
from .patientInfoDB import PatientInfoDatabase
from .medicalImagesDB import MedicalImagesDatabase
from .doctorInfoDB import DoctorInfoDatabase

class DatabaseCenter:
    def __init__(self) -> None:
        self.userDB = UserDatabase()
        self.patientInfoDB = PatientInfoDatabase()
        self.doctorInfoDB = DoctorInfoDatabase()
        self.medicalImagesDB = MedicalImagesDatabase()


dbCenter = DatabaseCenter()