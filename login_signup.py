import mysql.connector
import os
import hashlib
from config import *


cursor = cnx.cursor(buffered=True)

def get_md(password):
    return hashlib.md5(password.encode('utf-8')).hexdigest()

def is_available(username):

    query = ("select * from User where username = %s")
    cursor.execute(query, (username, ))

    if cursor._rowcount > 0:
        return False

    query = ("select * from Community where community_id = %s")
    cursor.execute(query, (username, ))

    if cursor._rowcount > 0:
        return False
    print("This is new username")
    return True


def sign_up(username, name, password, age, email):
    query = "insert into User(username,name,password,age,email) \
            VALUES( '%s', '%s','%s', '%s','%s')" % \
          (username,name, get_md(password), age, email)
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
    print(is_available('piyushrathipr'))
