from flask import session
import sqlite3

def addStory(user,name,text):
    f = "data/story.db"
    db = sqlite3.connect(f)
    c = db.cursor()

    #print("adding story..")
    
    q = "SELECT storyName from openedPages WHERE storyName=\"%s\"" % (name)
    c.execute(q)
    x = c.fetchall()
    #print(x)
    if len(x) > 0:
        #print("already there")
        return False   #NO DUPLICATE TITLES
    
    a = c.execute("SELECT storyID FROM updates")
    bId = 0
    for num in a:
        if num[0] > bId:
            bId = num[0]
    #bId + 1 is the id of the story
    q = "INSERT INTO updates VALUES (%d, \"%s\", %d, \"%s\");" % (bId+1, user, 0, text)
    #print(q)
    c.execute(q)
    q = "INSERT INTO openedPages VALUES (%d, \"%s\", %r);" % (bId+1, name, 0)
    c.execute(q)
    db.commit()
    db.close()
    return True


