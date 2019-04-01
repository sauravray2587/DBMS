import mysql.connector

cnx = mysql.connector.connect(user='root', password='qw',
								  host='127.0.0.1',
								  database='web')
cursor = cnx.cursor(buffered=True)


def follow(username_1, username_2):

	query = ("insert into Follower values(%s, %s)")
	cursor.execute(query, (username_1, username_2))

	cnx.commit()


def unfollow(username_1, username_2):

	query = ("delete from Follower where username_1 = %s and username_2 = %s")
	cursor.execute(query, (username_1, username_2))

	cnx.commit()


if __name__ == '__main__':
	follow('piyushrathipr', 'fsociety00')