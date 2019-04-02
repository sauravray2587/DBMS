import mysql.connector
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
	
	query = ("SELECT * from Bookmark where username = %s and post_id = %s")
	cursor.execute(query, (username, post_id))

	if cursor._rowcount > 0:
		return

	query = ("INSERT INTO Bookmark VALUES( %s, %s)")
	cursor.execute(query, (username, post_id))
	cnx.commit()

def unbookmark(username, post_id):

	query = ("delete from Bookmark where username = %s and post_id = %s")
	cursor.execute(query, (username, post_id))

	cnx.commit()

if __name__ == '__main__':
	bookmark('piyushrathipr', 32)