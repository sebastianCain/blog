from flask import session
import hashlib, sqlite3


def hashy(word):
    myHashObject = hashlib.sha256()
    w = word.encode('utf-8')
    myHashObject.update(w)
    return myHashObject.hexdigest()
       #returns hex string


def authenticate(username,password):
    f = "data/story.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    q = "SELECT username,password FROM users WHERE username = %s" % (username)
    a = c.execute(q)
    b = c.fetchone()
    if b != None:
        if b[0] == username and b[1] == hashy(password):
            db.close()
            return True
    db.close()
    return False
    

def addUser(username,password):
    f = "data/story.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    if password == "" or username == "":
        db.close()
        return "Registration invalid!"
    c.execute("SELECT username FROM users WHERE username = %s" % (username))
    a = c.fetchall()
    if len(a) > 0:
        db.close()
        return "User already registered!"
    q = "INSERT INTO users VALUES (\"%s\", \"%s\",\"\")" % (username,hashy(password))
    c.execute(q)
    db.commit()
    db.close()
    return "User successfully registered!"


def userCooked(user):
    f = "data/story.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    a = c.execute("SELECT username FROM users")    
    for row in a:
        if session and row and user == row[0]:
            return True
    return False




