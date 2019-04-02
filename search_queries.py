import mysql.connector
import operator
import os
from stories import get_posts
from config import *

cursor = cnx.cursor(buffered=True)

def search_tags(tag, cur_user):

	query = """SELECT * FROM Post WHERE 
			post_id in (SELECT post_id FROM Post_tags 
				WHERE tag_id = %s)"""
	cursor.execute(query, (tag,))

	return get_posts(cursor, cur_user)



if __name__=="__main__":
	print(search_tags("greedy"))