import mysql.connector

cnx = mysql.connector.connect(user='root', password='qw',
                                  host='127.0.0.1',
                                  database='web')
cursor = cnx.cursor(buffered=True)

def updateDb(username,name,password,age,email):
    # if type(message_new) == type(""):
    sql = "insert into User(username,name,password,age,email) VALUES( '%s', '%s','%s', '%s','%s')" % \
          (username,name,password,age,email)
    cursor_internal_func = cnx.cursor(buffered=True)
    cursor_internal_func.execute(sql)
    # else:
    #     sql = "insert into chatbot(candidateId,message,isChatbotReply, responseType , parentid , haveCards,previous) VALUES( '%s', '%s','%s', '%s','%s','%s','%s')" % \
    #           (candidate_id, message_display, 1, 1, -1, 2, id)
    #   , cursor_internal_func = cnx.cursor(buffered=True)
    #     cursor_internal_func.execute(sql)
    #     queryId = cursor_internal_2.lastrowid
    cnx.commit()

if __name__=="__main__":
    updateDb("fsociety00","Shubham","say_hi",21,"fsociety@gmail.com")