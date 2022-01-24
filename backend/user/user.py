class User:
    """
        所有用户的基类
    """

    def __init__(self) -> None:
        self.usertype = ''
        self.username = ''
        self.password = ''
        self.avatar = None

    def toTuple(self):
        return (self.username, self.password, self.usertype, self.avatar)

    