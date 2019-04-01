import mysql.connector
from config import connect_database


cnx = connect_database()
cursor = cnx.cursor(buffered=True)

def create_prerequisite(post_id1, post_id2):
	query = "INSERT INTO Prerequisite VALUES (%s, %s)"
	cursor.execute(query,(post_id1,post_id2))
	cnx.commit()


def get_prerequisits(post_id):
	query = "SELECT post_id_1 FROM Prerequisite\
			WHERE post_id_2 = %s"
	cursor.execute(query,(post_id,))

	prerequisites = []
	for (prerequisite_id,) in cursor:
		prerequisites.append(prerequisite_id)
	return prerequisites


if __name__=="__main__":
	# create_prerequisite(0,2)
	print(get_prerequisits(2))