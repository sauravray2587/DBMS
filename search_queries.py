import mysql.connector
from stories import search_posts
import operator
import os
from stories import get_posts

if (os.environ['USER']=='saurav'):
    pw = 'qwerty@123'
else:
    pw = 'qw'

dbase = 'web'

cnx = mysql.connector.connect(user='root', password=pw,
                                  host='127.0.0.1',
                                  database=dbase)
cursor = cnx.cursor(buffered=True)

def search_tags(taglist):

	var_string = ', '.join('?' * len(taglist))
	print(var_string)
	query = ("SELECT * FROM Post WHERE \
			post_id in (SELECT post_id FROM Post_tags \
				WHERE tag_id in (%s))"% var_string)
	cursor.execute(query, (taglist,))

	return get_posts(cursor)



if __name__=="__main__":
	print(search_tags(["dp","greedy"]))