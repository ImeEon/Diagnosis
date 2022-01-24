from .user import User

class Admin(User):
    def __init__(self, username, password) -> None:
        super().__init__()
        self.usertype = 'admin'
        self.username = username
        self.password = password