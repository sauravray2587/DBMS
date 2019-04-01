import mysql.connector
import operator
from stories import *

cnx = mysql.connector.connect(user='root', password='qw',
								  host='127.0.0.1',
								  database='web')
cursor = cnx.cursor(buffered=True)


def create_community(community_id, community_name, no_of_members, no_of_posts):

	query = ("insert into Community VALUES(%s, %s, %s, %s)")
	cursor.execute(query, (community_id, community_name, no_of_members,\
		 no_of_posts))

	cnx.commit()



def search_community(community_id, cur_user):

	query = ("SELECT post_id, Post.username, content, rating, post_time FROM User_community, Post"
			 " WHERE Post.username = User_community.username and User_community.community_id = %s")

	cursor.execute(query, (community_id,))

	return get_posts(cursor, cur_user)


if __name__ == '__main__':
	print(search_community('0'))