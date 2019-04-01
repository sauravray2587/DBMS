import mysql.connector
from stories import *
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


def get_feed(username):

	query = ("SELECT username_2 FROM Follower"
			 " WHERE username_1 = %s ")
	cursor.execute(query, (username,))

	feed_list = []

	for (following,) in cursor:
		posts = search_username(following)
		feed_list.extend(posts)

	return feed_list.sort(key = lambda x: x['post_time'], reverse = True)


if __name__=="__main__":
	print(get_feed("piyushrathipr"))
