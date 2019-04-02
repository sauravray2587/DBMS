import mysql.connector
from config import connect_database

cnx = connect_database()
cursor = cnx.cursor(buffered=True)
cursor1 = cnx.cursor(buffered=True)


def add_request(username, content, taglist):
	query = ("SELECT request_id from Request order by request_id desc limit 0, 1")
	cursor.execute(query)

	cur_id=0
	for (post_id, ) in cursor:
		cur_id = int(post_id) + 1

	query = "INSERT INTO Request VALUES (%s, %s, %s)"
	cursor.execute(query,(cur_id,username,content))
	cnx.commit()

	for tag_id in taglist:
		query = "INSERT INTO Request_tag VALUES (%s,%s)"
		cursor.execute(query,(cur_id,tag_id))
	cnx.commit()



def get_pending_requests():
	
	query = "SELECT * FROM Request"
	cursor.execute(query)
	requests = []
	for (request_id, username, content) in cursor:
		temp_dict = {}
		temp_dict["request_id"] = request_id
		temp_dict["username"] = username
		temp_dict["content"] = content

		temp_query = "SELECT tag_id FROM Request_tag WHERE request_id = %s"
		cursor1.execute(temp_query,(request_id,))
		temp_dict["tags"] = []
		for (tag_id,) in cursor1:
			temp_dict["tags"].append(tag_id)

		requests.append(temp_dict)

	return requests

def delete_request(request_id):

	query = "DELETE FROM Request_tag WHERE request_id = %s"
	cursor.execute(query,(request_id,))
	cnx.commit()
	query = "DELETE FROM Request WHERE request_id = %s"
	cursor.execute(query,(request_id,))
	cnx.commit()

if __name__=="__main__":
	print(get_pending_requests())
	# add_request("piyushrathipr", "java", ["dp","greedy"])