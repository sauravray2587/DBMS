import mysql.connector
import operator
import os

if (os.environ['USER']=='saurav'):
    pw = 'qwerty@123'
else:
    pw = 'qw'


cnx = mysql.connector.connect(user='root', password=pw,
								  host='127.0.0.1',
								  database='web')
cursor = cnx.cursor(buffered=True)
cursor1 = cnx.cursor(buffered=True)


def get_rating(post_id):
	cursor2 = cnx.cursor(buffered=True)
	query = "select count(*) from Post_vote group by %s"
	cursor2.execute(query, (post_id,))

	for (count, ) in cursor2:
		return count

def user_post(username, content, rating = 0, tags = [], community_id = None):
	community_id = community_id.replace(" ", "")
	if len(community_id)==0:
		community_id = None
	query = ("select post_id from Post order by post_id desc limit 0, 1")
	cursor.execute(query, ())

	for (post_id, ) in cursor:
		id_here = int(post_id) + 1

	if community_id != None:
		s = "INSERT INTO `Post` (`post_id`, `username`, `content`, `rating`, `community_id`) VALUES (%s, %s, %s, %s, %s )";
		query = (s)
		cursor.execute(query, (id_here, username, content, rating, community_id))
	else:
		s = "INSERT INTO `Post` (`post_id`, `username`, `content`, `rating`, `community_id`) VALUES (%s, %s, %s, %s, NULL )";
		query = (s)
		cursor.execute(query, (id_here, username, content, rating))
	cnx.commit()



	for tag in tags:

		query = ("select * from Tags where tag_id = %s")
		cursor.execute(query, (tag, ))

		if cursor._rowcount == 0:

			query = ("insert into Tags VALUES(%s, NULL, 0)")
			cursor.execute(query, (tag, ))
			cnx.commit()


		query = ("insert into Post_tags values(%s, %s)")
		cursor.execute(query, (id_here, tag))

		cnx.commit()




def get_posts(cursor, cur_user):
	result_list = []
	# print("rows : " , cursor._rowcount)
	for (post_id, username, content, rating, community_id, post_time) in cursor:

		temp_dict = {}
		temp_dict['post_id'] = post_id
		temp_dict['username'] = username
		temp_dict['content'] = content
		temp_dict['rating'] = get_rating(post_id)
		temp_dict['community_id'] = community_id
		temp_dict['post_time'] = post_time
		temp_dict['tags'] = []

		query = ("SELECT tag_id from Post_tags where post_id = %s")
		cursor1.execute(query, (post_id,))

		for (tag, ) in cursor1:
			temp_dict['tags'].append(tag)


		query = ("SELECT * from Bookmark where username = %s and post_id = %s")
		cursor1.execute(query, (cur_user, post_id))

		if cursor1._rowcount == 0:
			temp_dict['bookmark'] = 0
		else:
			temp_dict['bookmark'] = 1


		query = ("SELECT * from Follower where username_1 = %s and username_2 = %s")
		cursor1.execute(query, (cur_user, username))

		if cursor1._rowcount == 0:
			temp_dict['follows'] = 0
		else:
			temp_dict['follows'] = 1


		query = ("SELECT * from Post_vote where post_id = %s and username = %s")
		cursor1.execute(query, (post_id, cur_user))

		if cursor1._rowcount == 0:
			temp_dict['upvote'] = 0
		else:
			temp_dict['upvote'] = 1


		result_list.append(temp_dict)

	print("result, ", result_list)
	result_list.sort(key = lambda x: x['post_time'], reverse = True)
	# print("result, ", result_list)
	return result_list



def search_username(username, cur_user):

	query = ("SELECT post_id, username, content, rating, community_id, post_time FROM Post"
			 " WHERE username = %s ")

	cursor.execute(query, (username,))
	# print("row count, ", cursor._rowcount)
	x = get_posts(cursor, cur_user)
	print("x, " , x)
	return x


if __name__ == '__main__':
	# get_posts('34' ,'piyushrathipr', 'Uber code', 2.2, tags = ['DL', 'Full Stack'])
	print(search_username("fsociety00", 'piyushrathipr'))