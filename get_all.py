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
                                  database=dbase)
cursor = cnx.cursor(buffered=True)


def get_all_comm():

	query = "SELECT community_id FROM Community"

	cursor.execute(query, ())

	communities_list = []

	for (idd, ) in cursor:
		communities_list.append(idd)

	return communities_list


def get_all_tags():

	query = "SELECT tag_id FROM Tags"

	cursor.execute(query, ())

	tags_list = []

	for (idd, ) in cursor:
		tags_list.append(idd)

	return tags_list


def get_all_user():

	query = "SELECT username FROM User"

	cursor.execute(query, ())

	users_list = []

	for (idd, ) in cursor:
		users_list.append(idd)

	return users_list


def get_all_posts():

	query = "SELECT * FROM Post"

	cursor.execute(query, ())

	return get_posts(cursor, None)


if __name__ == '__main__':
	print(get_all_posts())