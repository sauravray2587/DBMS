import mysql.connector
import operator
from stories import *
import os

if (os.environ['USER']=='saurav'):
    pw = 'qwerty@123'
else:
    pw = 'qw'

cnx = mysql.connector.connect(user='root', password=pw,
								  host='127.0.0.1',
								  database='web',
								  autocommit = True)
cursor = cnx.cursor(buffered=True)


def create_community(community_name, no_of_members = 0, no_of_posts = 0):

	query = ("select community_id from Community order by community_id desc limit 0, 1")
	cursor.execute(query, ())

	id_here = 0
	for (post_id, ) in cursor:
		id_here = int(post_id) + 1

	query = ("insert into Community VALUES(%s, %s, %s, %s)")
	cursor.execute(query, (id_here, community_name, no_of_members,\
		 no_of_posts))

	cnx.commit()



def search_community(community_id, cur_user):

	query = ("SELECT post_id, Post.username, content, rating, post_time FROM User_community, Post"
			 " WHERE Post.username = User_community.username and User_community.community_id = %s")

	cursor.execute(query, (community_id,))

	x = get_posts(cursor, cur_user)
	return x


def add_user(community_id,cur_user):

	query = "INSERT INTO User_community VALUES(%s, %s, %s)"
	cursor.execute(query,(community_id,cur_user,0))
	cnx.commit()


if __name__ == '__main__':
	# print(search_community('0'))
	add_user("piyushrathipr","0")
