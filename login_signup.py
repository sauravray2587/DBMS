import mysql.connector
import os
import hashlib
from config import *


cursor = cnx.cursor(buffered=True)

def get_md(password):
    return hashlib.md5(password.encode('utf-8')).hexdigest()

def sign_up(username, name, password, age, email):
    query = "insert into User(username,name,password,age,email) \
            VALUES( '%s', '%s','%s', '%s','%s')" % \
          (username,name, password, age, email)
    cursor.execute(query)
    cnx.commit()


def check_login(username, password):
    query = ("SELECT password FROM User"
             " WHERE username = %s ")
    cursor.execute(query, (username,))

 
    print("size, " ,cursor._rowcount)
    if cursor._rowcount==0:
        print("User doesn't exist")
        return False

    for (saved_password,) in cursor:
        if get_md(password) == saved_password:
            return True
        else:
            print("Password don't match")
            return False




if __name__=="__main__":
    # sign_up("fsociety00","Shubham","say_hi", 21,"fsociety@gmail.com")
    print(check_login("fsociety00","say_hi"))
    # user_post("3" , "fsociety00", "high level content")
