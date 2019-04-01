import mysql.connector
import os

if (os.environ['USER']=='saurav'):
    pw = 'qwerty@123'
else:
    pw = 'qw'

dbase = 'web'

cnx = mysql.connector.connect(user='root', password=pw,
                                  host='127.0.0.1',
                                  database=dbase)
cursor = cnx.cursor(buffered=True)

def list_tags():

	query = "SELECT tag_id FROM Tags"
	cursor.execute(query)

	tag_list = []
	for (tag_id,) in cursor:
		tag_list.append(tag_id)

	return tag_list

if __name__=="__main__":
	print(list_tags())