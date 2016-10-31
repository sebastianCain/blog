import sqlite3

f = "../data/story.db"
db = sqlite3.connect(f)
c = db.cursor()

def newUpdate(sId,user,updateNo,text):
    q = "SELECT updateNo from updates WHERE storyID=%d" % (sID)
    c.execute(q)
    numbers = c.fetchAll()
    latest = numbers[len(numbers)-1]
    q = "INSERT INTO updates VALUES (%d, \"%s\", %d, \"%s\")" % (sId, user, latest+1, text)
    db.commit()
    db.close()



    
