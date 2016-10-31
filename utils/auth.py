import hashlib, sqlite3

def hashy(word):
    myHashObject = hashlib.sha256()
    w = word.encode('utf-8')
    myHashObject.update(w)
    return myHashObject.hexdigest()
       #returns hex string


def authenticate(username,password):
    f = "/data/story.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    q = "SELECT username,password FROM users WHERE username = %s" % (username)
    a = c.execute(q)
    if (len(a) == 0):
        return False #NOT FOUND
    for user in a:
        if username == user[0]:
            if hashy(password) == user[1]:
                return True
    return False
    

