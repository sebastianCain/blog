import sqlite3


#need to check if user has already contributed

def newUpdate(sId,user,text):
    #SETUP
    f = "data/story.db"
    db = sqlite3.connect(f)
    c = db.cursor()

    #CHECK IF USER HAS CONTRIBUTED
    q = "SELECT storyID from updates WHERE storyID=%d AND username=\"%s\"" % (sId,user)
    c.execute(q)
    a = c.fetchall()
    if len(a) > 0:
        print ("Already added")
        return False   #User has a update with the same story number

    #ADD THE UPDATE AFTER DETERMINING UPDATE NO
    q = "SELECT updateNo from updates WHERE storyID=%d" % (sId)
    c.execute(q)
    numbers = c.fetchall()
    latest = 0
    if len(numbers) > 0:
        latest = int((numbers[len(numbers)-1])[0])
    q = "INSERT INTO updates VALUES (%d, \"%s\", %d, \"%s\")" % (sId, user, latest+1, text)
    c.execute(q)
    print ("new update added")
    db.commit()
    db.close()
    return True



    
