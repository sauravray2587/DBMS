import os
import mysql.connector

if (os.environ['USER']=='saurav'):
    pw = 'qwerty@123'
else:
    pw = 'qw'


cnx = mysql.connector.connect(user='root', password=pw,
								  host='127.0.0.1',
								  database='web',
								  autocommit = True)

