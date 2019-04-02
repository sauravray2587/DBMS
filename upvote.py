import mysql.connector
import os
from config import *

cursor = cnx.cursor(buffered=True)

def upvote(post_id, username):

	query = ("SELECT * from Post_vote where username = %s and post_id = %s")
	cursor.execute(query, (username, post_id))

	if cursor._rowcount > 0:
		return

	query = ("insert into Post_vote values(%s, %s)")
	cursor.execute(query, (post_id, username))

	cnx.commit()


def downvote(post_id, username):

	query = ("delete from Post_vote where post_id = %s and username = %s")
	cursor.execute(query, (post_id, username))

	cnx.commit()


if __name__ == '__main__':
	upvote(32, 'piyushrathipr')