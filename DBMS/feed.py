import mysql.connector
from stories import *
import operator
import os
from config import *

cursor = cnx.cursor(buffered=True)


def get_feed(username):

	query = ("SELECT username_2 FROM Follower"
			 " WHERE username_1 = %s ")
	cursor.execute(query, (username,))

	feed_list = []

	for (following,) in cursor:
		posts = search_username(following, username)
		for post in posts:
			feed_list.append(post)

	feed_list.sort(key = lambda z: (print(z), z['post_time']), reverse = True)
	return feed_list


if __name__ == "__main__":
	print(get_feed("piyushrathipr"))
