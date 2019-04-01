import mysql.connector
from stories import search_posts
import operator

cnx = mysql.connector.connect(user='root', password='qw',
								  host='127.0.0.1',
								  database='web')
cursor = cnx.cursor(buffered=True)

def get_feed(username):

	query = ("SELECT username_2 FROM Follower"
			 " WHERE username_1 = %s ")
	cursor.execute(query, (username,))
	feed_dict = {}

	for (following,) in cursor:
		posts = search_posts(following)
		for post_id in posts:
			feed_dict[post_id] = posts[post_id]

	feed = {}
	for key,value in  sorted(feed_dict.items(),key = lambda x: x[1]["post_time"],reverse=True):
		feed[key] = value
	return feed

if __name__=="__main__":
	print(get_feed("piyushrathipr"))