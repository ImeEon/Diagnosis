from user import user
from .baseDB import BaseDatabase
import sqlite3
import os
from config import IMAGE_AVATAR_DIR

"""
    用户表:
        存放每个用户必须的信息
        (username[primary key], password, usertype, avatar)
"""

class UserDatabase(BaseDatabase):
    table_name = 'user'
    op_create = f'''CREATE TABLE IF NOT EXISTS {table_name}(
        username TEXT PRIMARY KEY,
        password TEXT,
        usertype TEXT,
        avatar TEXT
        )'''
    op_insert = f"INSERT INTO {table_name} VALUES ('%s','%s','%s','%s')"
    op_select_by_username = f"SELECT * FROM {table_name} WHERE username='%s'"
    op_update_by_username = f'''UPDATE {table_name} SET 
        password = '%s',
        usertype = '%s',
        avatar = '%s'
        WHERE username = '%s'
    '''
    op_select_by_usertype = f"SELECT * FROM {table_name} WHERE usertype='%s'"

    def __init__(self) -> None:
        super().__init__()
        self.con = sqlite3.connect(self.db_path, check_same_thread=False)
        self.cur = self.con.cursor()
        self.create()

    def create(self):
        self.cur.execute(self.op_create)

    def getAvatar(self, username):
        result = self.selectByUsername(username)
        if len(result) > 0:
            user = result[0]
            return { 'flag': True, 'message': 'Success!', 'avatar': user[3] }
        else:
            return { 'flag': False, 'message': 'Failed!' }

    def setAvatar(self, username, filename):
        result = self.selectByUsername(username)
        if len(result) > 0:
            user = result[0]
            self.updateByUsername(username, user[1], user[2], filename)
            return { 'flag': True, 'message': 'Success!', 'avatar': filename}
        else:
            return { 'flag': False, 'message': 'Username does not exists!' }

    def getUsertype(self, username):
        result = self.selectByUsername(username)
        if len(result) > 0:
            return { 'flag': True, 'message': 'Success!', 'usertype': result[0][2]}
        else:
            return { 'flag': False, 'message': 'Username does not exists!' }

    def updateByUsername(self, username, password, usertype, avatar):
        self.cur.execute(self.op_update_by_username % (password, usertype, avatar, username))
        self.con.commit()

    def getAllDoctorUsername(self):
        result = self.selectByUserType('doctor')
        if len(result) > 0:
            return { 'flag': True, 'message': 'Success!', 'doctors': [item[0] for item in result] }
        else:
            return { 'flag': False, 'message': 'Zero.' }

    def getAllPatientUsername(self):
        result = self.selectByUserType('patient')
        if len(result) > 0:
            return { 'flag': True, 'message': 'Success!', 'patients': [item[0] for item in result] }
        else:
            return { 'flag': False, 'message': 'Zero.' }

    def insert(self, user):
        """添加新用户

        Args:
            user (User): user to be insert

        Returns:
            ret (dict): 
                flag (bool): success or not,
                message (str): reason

        """
        
        if len(self.selectByUsername(user.username)) > 0:
            return { 'flag': False, 'message': 'Same username found!' }
        self.cur.execute(self.op_insert % user.toTuple())
        self.con.commit()
        return { 'flag': True, 'message': 'Success!' }

    def selectByUsername(self, username):
        self.cur.execute(self.op_select_by_username % (username))
        return self.cur.fetchall()

    def selectByUserType(self, usertype):
        self.cur.execute(self.op_select_by_usertype % (usertype))
        return self.cur.fetchall()

    def check(self, username, password):
        result = self.selectByUsername(username)
        if len(result) == 0:
            return { 'flag': False, 'message': 'Username not found!' }
        user = result[0]
        pwd = user[1]
        if password == pwd:
            return { 'flag': True, 'message': 'Success!' }
        else:
            return { 'flag': False, 'message': 'Wrong password!' }

    def close(self):
        self.cur.close()
        self.con.close()