from .baseDB import BaseDatabase
import sqlite3
import os

"""
    患者个人信息表:
        存放患者的个人信息
        (username[primary key], name, birth, tel, intro)
"""

class PatientInfoDatabase(BaseDatabase):
    table_name = 'patient_info'
    op_create = f'''CREATE TABLE IF NOT EXISTS {table_name}(
        username TEXT PRIMARY KEY,
        name TEXT,
        birth TEXT,
        tel TEXT,
        intro TEXT
        )'''
    op_insert = f"INSERT INTO {table_name} VALUES ('%s','%s','%s','%s','%s')"
    op_select_by_username = f"SELECT * FROM {table_name} WHERE username='%s'"
    op_update_by_username = f'''UPDATE {table_name} SET 
        name = '%s',
        birth = '%s',
        tel = '%s',
        intro = '%s'
        WHERE username = '%s'
    '''

    def __init__(self) -> None:
        super().__init__()
        self.con = sqlite3.connect(self.db_path, check_same_thread=False)
        self.cur = self.con.cursor()
        self.create()

    def create(self):
        self.cur.execute(self.op_create)

    def updateByUsername(self, username, name, birth, tel, intro):
        self.cur.execute(self.op_update_by_username % (name, birth, tel, intro, username))
        self.con.commit()

    def insert(self, username, name, birth, tel, intro):
        self.cur.execute(self.op_insert % (username, name, birth, tel, intro))
        self.con.commit()

    def insertOrUpdate(self, username, name, birth, tel, intro):
        """添加或更新患者信息

        Args:
            username (str)
            name (str)
            birth (str)
            tel (str)
            intro (str)

        Returns:
            ret (dict): 
                flag (bool): success or not,
                message (str): reason

        """
        
        if len(self.selectByUsername(username)) > 0:
            # 更新
            self.updateByUsername(username, name, birth, tel, intro)
            return { 'flag': True, 'message': 'User info updated!' }
        else:
            self.insert(username, name, birth, tel, intro)
            return { 'flag': True, 'message': 'User info inserted!' }

    def getByUsername(self, username):
        result = self.selectByUsername(username)
        if len(result) > 0:
            user = result[0]
            return { 
                'flag': True, 
                'message': 'Get user info', 
                'name': user[1],
                'birth': user[2],
                'tel': user[3],
                'intro': user[4]
            }
        else:
            return { 'flag': False, 'message': 'Username does not exists!' }

    def selectByUsername(self, username):
        self.cur.execute(self.op_select_by_username % username)
        return self.cur.fetchall()

    def close(self):
        self.cur.close()
        self.con.close()