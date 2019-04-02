import mysql.connector
import os
from config import *

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