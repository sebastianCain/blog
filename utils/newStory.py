from flask import session
import sqlite3

def addStory(user,name,text):
    f = "data/story.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    a = c.execute("SELECT storyID FROM updates")
    bId = 0
    for num in a:
        if num[0] > bId:
            bId = num[0]
    print (bId)
    q = "INSERT INTO updates VALUES (%d, \"%s\", %d, \"%s\")" % (bId, user, 0, text)
    print (q)
    c.execute(q)
    db.commit()
    db.close()
    return True
