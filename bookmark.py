import mysql.connector
import operator
import os
from stories import *

if (os.environ['USER']=='saurav'):
    pw = 'qwerty@123'
else:
    pw = 'qw'

dbase = 'web'

cnx = mysql.connector.connect(user='root', password=pw,
                                  host='127.0.0.1',
                                  database=dbase,
                                  autocommit = True)
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


def get_bookmarked(username):

	query = ("SELECT Post.post_id, Post.username, content, rating, community_id, post_time\
			FROM Bookmark INNER JOIN Post ON Post.post_id = Bookmark.post_id and Bookmark.username = %s")

	cursor.execute(query, (username, ))

	x = get_posts(cursor, username)

	return x


if __name__ == '__main__':
	print(get_bookmarked('fsociety00'))