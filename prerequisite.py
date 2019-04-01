import mysql.connector
from config import connect_database


cnx = connect_database()
cursor = cnx.cursor(buffered=True)
cursor1 = cnx.cursor(buffered=True)

def create_prerequisite(post_id1, post_id2):
	query = "INSERT INTO Prerequisite VALUES (%s, %s)"
	cursor.execute(query,(post_id1,post_id2))
	cnx.commit()


def get_prerequisites(cur_user, post_id):
	query = "SELECT post_id_2 FROM Prerequisite\
			WHERE post_id_1 = %s"
	cursor.execute(query,(post_id,))

	prerequisites = []
	for (prerequisite_id,) in cursor:
		query = ("SELECT post_id, username, content, rating, community_id, post_time FROM Post"
			 " WHERE post_id = %s ")

		cursor1.execute(query, (prerequisite_id,))

		prerequisites.extend(get_post(cursor1,cur_user))
	return prerequisites

if __name__=="__main__":
	# create_prerequisite(0,2)
	print(get_prerequisites(0))