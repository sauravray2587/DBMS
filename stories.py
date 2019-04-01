import mysql.connector

cnx = mysql.connector.connect(user='root', password='qw',
								  host='127.0.0.1',
								  database='web')
cursor = cnx.cursor(buffered=True)
cursor1 = cnx.cursor(buffered=True)


def user_post(post_id, username, content, rating, community_id, tags):
	query = ("insert into Post VALUES(%s, %s, %s, %s, %s)")
	cursor.execute(query, (post_id, username, content, rating, community_id))

	cnx.commit()

	for tag in tags:
		query = ("insert into Post_tags values(%s, %s)")
		cursor.execute(query, (post_id, tag))

		cnx.commit()



def search_posts(username):

	query = ("SELECT post_id, username, content, rating, community_id FROM Post"
			 " WHERE username = %s ")

	cursor.execute(query, (username,))

	result_dict = {}

	for (post_id, username, content, rating, community_id) in cursor:
		temp_dict = {}
		temp_dict['username'] = username
		temp_dict['content'] = content
		temp_dict['rating'] = rating
		temp_dict['community_id'] = community_id

		temp_dict['tags'] = []

		query = ("SELECT tag_id from Post_tags where post_id = %s")
		cursor1.execute(query, (post_id,))

		for (tag, ) in cursor1:
			temp_dict['tags'].append(tag)

		result_dict[post_id] = temp_dict

	return result_dict


if __name__ == '__main__':
	print(search_posts('fsociety00'))