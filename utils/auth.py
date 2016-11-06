from flask import session
import hashlib, sqlite3


def hashy(word):
    myHashObject = hashlib.sha256()
    w = word.encode('utf-8')
    myHashObject.update(w)
    return myHashObject.hexdigest()
       #returns hex string


def authenticate(username,password):
    #fails if empty username
    if username == "" or username == None:
        return False
    f = "data/story.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    #sees if there is a corresponding username in users
    q = "SELECT username,password FROM users WHERE username = \"%s\"" % (username)
    a = c.execute(q)
    b = c.fetchone()
    if b != None:
        #checks if passwords match
        if b[0] == username and b[1] == hashy(password):
            db.close()
            return True
    db.close()
    return False
    

def addUser(username,password):
    #fails if one of the fields if empty
    if password == "" or username == "":
        db.close()
        return 0
    f = "data/story.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    #checks if user already exists
    c.execute("SELECT username FROM users WHERE username = \"%s\"" % (username))
    a = c.fetchall()
    if len(a) > 0:
        db.close()
        return 1
    #if valid, adds username and password to the users
    q = "INSERT INTO users VALUES (\"%s\", \"%s\",\"\")" % (username,hashy(password))
    c.execute(q)
    db.commit()
    db.close()
    return 2

#Checks if the user is logged in by checking cookies
def userCooked(user):
    f = "data/story.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    a = c.execute("SELECT username FROM users")    
    for row in a:
        if session and row and user == row[0]:
            return True
    return False




