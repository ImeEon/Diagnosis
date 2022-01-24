from .baseDB import BaseDatabase
import sqlite3

"""
    医疗图片:
        存放患者上传的医疗图片url和相应的检测结果url
        (id[primary key], username, upload, result)
"""

class MedicalImagesDatabase(BaseDatabase):
    table_name = 'medical_images'
    op_create = f'''CREATE TABLE IF NOT EXISTS {table_name}(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        upload TEXT,
        result TEXT
        )'''
    op_insert = f"INSERT INTO {table_name} VALUES (NULL, '%s','%s','%s')"
    op_select_by_username = f"SELECT * FROM {table_name} WHERE username='%s'"

    def __init__(self) -> None:
        super().__init__()
        self.con = sqlite3.connect(self.db_path, check_same_thread=False)
        self.cur = self.con.cursor()
        self.create()

    def create(self):
        self.cur.execute(self.op_create)

    def insert(self, username, upload, result):
        self.cur.execute(self.op_insert % (username, upload, result))
        self.con.commit()
        return { 'flag': True, 'message': 'Insert success', 'upload': upload, 'result': result }

    def getImagesByUsername(self, username):
        result = self.selectByUsername(username)
        if len(result) > 0:
            return { 
                'flag': True, 
                'message': 'Get upload and result', 
                'upload': [item[2] for item in result],
                'result': [item[3] for item in result],
            }
        else:
            return { 'flag': False, 'message': 'Username does not exists or no record' }

    def selectByUsername(self, username):
        self.cur.execute(self.op_select_by_username % username)
        return self.cur.fetchall()

    def close(self):
        self.cur.close()
        self.con.close()