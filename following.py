import mysql.connector
import os
from config import *

cursor = cnx.cursor(buffered=True)


def follow(username_1, username_2):

	query = ("SELECT * from Follower where username_1 = %s and username_2 = %s")
	cursor.execute(query, (username_1, username_2))

	if cursor._rowcount > 0:
		return

	query = ("insert into Follower values(%s, %s)")
	cursor.execute(query, (username_1, username_2))

	cnx.commit()


def unfollow(username_1, username_2):

	query = ("delete from Follower where username_1 = %s and username_2 = %s")
	cursor.execute(query, (username_1, username_2))

	cnx.commit()

def check_follow(username_1, username_2):
	
	query = ("select * from Follower where username_1 = %s and username_2 = %s")
	cursor.execute(query, (username_1, username_2))

	if cursor._rowcount>0:
		return True
	else:
		return False


if __name__ == '__main__':
	follow('piyushrathipr', 'fsociety00')