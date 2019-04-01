import mysql.connector

cnx = mysql.connector.connect(user='root', password='qw',
								  host='127.0.0.1',
								  database='web')
cursor = cnx.cursor(buffered=True)


def create_community(community_id, community_name, no_of_members, no_of_posts):

	query = ("insert into Community VALUES(%s, %s, %s, %s)")
	cursor.execute(query, (community_id, community_name, no_of_members,\
		 no_of_posts))

	cnx.commit()

def search_community(community_id):

	query = ("SELECT post_id, username, content, rating, post_time FROM User_community, Post"
			 " WHERE Post.username = User_community.username and User_community.community_id = %s")

	cursor.execute(query, (community_id,))

	result_dict = {}

	for (post_id, username, content, rating, post_time) in cursor:

		temp_dict = {}

		temp_dict['username'] = username
		temp_dict['content'] = content
		temp_dict['rating'] = rating
		temp_dict['post_time'] = post_time

		result_dict[post_id] = temp_dict

	unsorted_dict = {}

	for it in result_dict:
		unsorted_dict[it] = result_dict[it]["post_time"]

	sorted_dict = sorted(unsorted_dict.items(), key = operator.itemgetter(1), reverse =True) 

	sorted_final_dict = {}

	count = 0
	for it in sorted_dict:
		if count >= 10:
			break
		sorted_final_dict[it[0]] = result_dict[it[0]]

		count += 1