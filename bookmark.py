import mysql.connector
from stories import search_posts
import operator
import os

if (os.environ['USER']=='saurav'):
    pw = 'qwerty@123'
else:
    pw = 'qw'

dbase = 'web'

cnx = mysql.connector.connect(user='root', password=pw,
                                  host='127.0.0.1',
                                  database=dbase)
cursor = cnx.cursor(buffered=True)

def bookmark(username, post_id):

	query = ("INSERT INTO Bookmark \
		VALUES( '%s', '%s')" %(username,post_id)
	cursor.execute(query)
	cnx.commit()