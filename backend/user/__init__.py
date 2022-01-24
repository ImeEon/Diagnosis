from .patient import Patient
from .doctor import Doctor


class UserCenter:
    def __init__(self) -> None:
        pass

    def getUser(self, usertype, username, password):
        if usertype == 'patient':
            return Patient(username, password)
        elif usertype == 'doctor':
            return Doctor(username, password)
        else:
            # TODO admin
            pass

userCenter = UserCenter()