from user import userCenter
from database import dbCenter
import os
from config import IMAGE_AVATAR_DIR, IMAGE_MEDICAL_DIR
from diagnosis import getResult

class Service:
    def __init__(self) -> None:
        pass

    def signup(self, usertype, username, password):
        user = userCenter.getUser(usertype, username, password)
        return dbCenter.userDB.insert(user)

    def signin(self, username, password):
        return dbCenter.userDB.check(username, password)

    def getUsertype(self, username):
        return dbCenter.userDB.getUsertype(username)

    def setPatientInfo(self, username, name, birth, tel, intro):
        return dbCenter.patientInfoDB.insertOrUpdate(username, name, birth, tel, intro)

    def getPatientInfo(self, username):
        return dbCenter.patientInfoDB.getByUsername(username)

    def setDoctorInfo(self, username, name, birth, tel, intro):
        return dbCenter.doctorInfoDB.insertOrUpdate(username, name, birth, tel, intro)

    def getDoctorInfo(self, username):
        return dbCenter.doctorInfoDB.getByUsername(username)

    def getAvatar(self, username):
        return dbCenter.userDB.getAvatar(username)
    
    def setAvatar(self, username, file):
        filename = file.filename
        file.save(os.path.join(IMAGE_AVATAR_DIR, filename))
        return dbCenter.userDB.setAvatar(username, filename)

    def setMedicalImage(self, username, file):
        upload = file.filename
        file.save(os.path.join(IMAGE_MEDICAL_DIR, upload))
        result = getResult(upload)
        return dbCenter.medicalImagesDB.insert(username, upload, result)

    def getMedicalImages(self, username):
        return dbCenter.medicalImagesDB.getImagesByUsername(username)

    def getAllDoctorUsername(self):
        return dbCenter.userDB.getAllDoctorUsername()

service = Service()