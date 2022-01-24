# By Vamei
import os
import sqlite3

# test.db is a file in the working directory.
conn = sqlite3.connect(os.path.join('.', 'backend', 'data', 'db', 'test.db'))

c = conn.cursor()

# create tables
c.execute('CREATE TABLE IF NOT EXISTS test(id int primary key, name text)')
# c.execute('INSERT INTO test VALUES (?,?)', (1, 'as'))
# c.execute('INSERT INTO test VALUES (?,?)', (2, 'qw'))
# try:
#       c.execute('INSERT INTO test VALUES (?,?)', (1, 'fda'))
# except Exception as e:
#       print(e)

sql_text_3 = """
UPDATE test
SET name = '%s', id = '%d'
WHERE id = '1';
"""
c.execute(sql_text_3 % ('fasdfs', 3))
print(c.fetchall())

# save the changes
conn.commit()

# close the connection with the database
conn.close()