import mysql.connector

cnx = mysql.connector.connect(user='root', password='qw',
								  host='127.0.0.1',
								  database='web')
cursor = cnx.cursor(buffered=True)
cursor1 = cnx.cursor(buffered=True)


def user_post(post_id, username, content, rating = 0, tags = [], community_id = None):
	if community_id != None:
		query = ("insert into Post VALUES(%s, %s, %s, %s, %s, NULL )")
		cursor.execute(query, (post_id, username, content, rating, community_id))
	else:
		query = ("insert into Post VALUES(%s, %s, %s, %s, NULL, NULL)")
		cursor.execute(query, (post_id, username, content, rating))
	cnx.commit()



	for tag in tags:

		query = ("select * from Tags where tag_id = %s")
		cursor.execute(query, (tag, ))

		if cursor._rowcount == 0:

			query = ("insert into Tags VALUES(%s, NULL, 0)")
			cursor.execute(query, (tag, ))
			cnx.commit()


		query = ("insert into Post_tags values(%s, %s)")
		cursor.execute(query, (post_id, tag))

		cnx.commit()


def get_posts(cursor, cur_user):
	result_dict = {}

	for (post_id, username, content, rating, community_id, post_time) in cursor:
		temp_dict = {}
		temp_dict['username'] = username
		temp_dict['content'] = content
		temp_dict['rating'] = rating
		temp_dict['community_id'] = community_id
		temp_dict['post_time'] = post_time
		temp_dict['tags'] = []

		query = ("SELECT tag_id from Post_tags where post_id = %s")
		cursor1.execute(query, (post_id,))

		for (tag, ) in cursor1:
			temp_dict['tags'].append(tag)


		query = ("SELECT * from Bookmark where username = %s and post_id = %s")
		cursor.execute(query, (cur_user, post_id))

		if cursor._rowcount == 0:
			temp_dict['bookmark'] = 0
		else:
			temp_dict['bookmark'] = 1


		query = ("SELECT * from Follower where username_1 = %s and username_2 = %s")
		cursor.execute(query, (cur_user, username))

		if cursor._rowcount == 0:
			temp_dict['follows'] = 0
		else:
			temp_dict['follows'] = 1


		result_dict[post_id] = temp_dict

	return result_dict

def search_username(username, cur_user):

	query = ("SELECT post_id, username, content, rating, community_id, post_time FROM Post"
			 " WHERE username = %s ")

	cursor.execute(query, (username,))

	return get_posts(cursor, cur_user) 


if __name__ == '__main__':
	get_posts('34' ,'piyushrathipr', 'Uber code', 2.2, tags = ['DL', 'Full Stack'])