from flask import session
import sqlite3

#reminder to add a name column to ispageopen
def addStory(user,name,text):
    f = "data/story.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    q = "SELECT storyID FROM stories"
    c.execute(q)
    bID = c.fetchone()
    a = c.fetchall()
    for num in a:
        if num > bID:
            bID = num
    q = "INSERT INTO stories VALUES (%d, \"%s\", %d, \"%s\")" % (bId, user, 0, text)
