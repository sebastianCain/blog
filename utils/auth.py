import hashlib, sqlite3

f = "../data/story.db"
db = sqlite3.connect(f)
c = db.cursor()

def hashy(word):
    myHashObject = hashlib.sha256()
    w = word.encode('utf-8')
    myHashObject.update(w)
    return myHashObject.hexdigest()
       #returns hex string


def authenticate(username,password):
    q = "SELECT username,password FROM users WHERE username = %s" % (username)
    a = c.execute(q)
    if len(a) == 0:
        db.close()
        return False #NOT FOUND
    for user in a:
        if username == user[0]:
            if hashy(password) == user[1]:
                db.close()
                return True
    db.close()
    return False
    

def addUser(username,password):
    if password == "" or username == "":
        db.close()
        return "Registration invalid!"
    q = "SELECT username FROM users WHERE username = %s" % (username)
    a = c.execute(q)
    if len(a) > 0:
        db.close()
        return "User already registered!"
    q = "INSERT INTO users VALUES (\"%s\", \"%s\")" % (username,hashy(password))
    db.commit()
    db.close()
    return "User successfully registered!"

