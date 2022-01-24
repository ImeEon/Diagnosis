from .user import User
import os

class Patient(User):

    default_avater = 'patient.jpg'

    def __init__(self, username, password) -> None:
        super().__init__()
        self.usertype = 'patient'
        self.username = username
        self.password = password
        self.avatar = self.default_avater

