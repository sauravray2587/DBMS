import mysql.connector
from stories import search_posts

if (os.getlogin()=='saurav'):
    pw = 'qwerty@123'
else:
    pw = 'qw'

cnx = mysql.connector.connect(user='root', password=pw,
								  host='127.0.0.1',
								  database='web')
cursor = cnx.cursor(buffered=True)
cursor1 = cnx.cursor(buffered=True)


def get_feed(username):

	query = ("SELECT username_1 FROM Follower"
			 " WHERE username_2 = %s ")
	cursor.execute(query, (username,))
	feed_list = []

	for (follower) in cursor:
		feed_list.append(search_posts(follower))
	print(feed_list)
	return feed_list
	