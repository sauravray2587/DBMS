import mysql.connector

cnx = mysql.connector.connect(user='root', password='qw',
                                  host='127.0.0.1',
                                  database='web')
cursor = cnx.cursor(buffered=True)


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
    if cursor.arraysize==0:
        print("User doesn't exist")
        return False

    for (saved_password,) in cursor:
        if password == saved_password:
            return True
        else:
            print("Password not matched password = ", password, "actual password = ",saved_password)
            return False




if __name__=="__main__":
    # sign_up("fsociety00","Shubham","say_hi", 21,"fsociety@gmail.com")
    print(check_login("fsociety00","say_hi"))
    # user_post("3" , "fsociety00", "high level content")