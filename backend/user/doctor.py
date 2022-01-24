from .user import User
import os

class Doctor(User):

    default_avater = 'doctor.jpg'

    def __init__(self, username, password) -> None:
        super().__init__()
        self.usertype = 'doctor'
        self.username = username
        self.password = password
        self.avatar = self.default_avater