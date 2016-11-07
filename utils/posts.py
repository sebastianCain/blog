from flask import session
import sqlite3


def getFeedData(username):
    #connect to database
    db = sqlite3.connect("data/story.db")
    cursor = db.cursor()
    
    query = "SELECT * FROM updates "
    contributedIDs = getContributedIDs(username)

    #construct query with indeterminate # of ids to exclude
    isFirst = True
    if contributedIDs:
        query += "WHERE"
    for i in contributedIDs:
        if isFirst == False:
            query += " AND"
        else:
            isFirst = False
        query += " storyID != " + str(i)

    cursor.execute(query)
    fetch = cursor.fetchall()
    
    recentUpdates = []
    
    for update in fetch:
        storyID = update[0]
        updateNum = update[2]

        #check if story already exists
        replaced = False
        for i in range(len(recentUpdates)):
            diffupdate = recentUpdates[i]
            if storyID == diffupdate[0]:

                #if update is more recent, replace
                if updateNum > diffupdate[2]:
                    recentUpdates.pop(i)
                    recentUpdates.append(update)
                    replaced = True
                    break
                
        if replaced == False:
            recentUpdates.append(update)

    data = []
    
    for update in recentUpdates:
        query = "SELECT title FROM stories WHERE storyID=\"" + str(update[0]) + "\""
        cursor.execute(query)
        fetch = cursor.fetchall()

        #data is array of dicts with one entry for each story
        data.append({"storyID": update[0], "title": fetch[0][0], "text": update[3]})

    return data
    

def getContributedIDs(username):

    #connect to database
    db = sqlite3.connect("data/story.db")
    cursor = db.cursor()
    
    query = "SELECT storyID FROM updates WHERE username=\"" + username + "\""
    cursor.execute(query)
    fetch = cursor.fetchall()

    #extract storyID from tuple
    data = []
    for i in fetch:
        data.append(i[0])
        
    return data


def getContributedData(username):

    #connect to database
    db = sqlite3.connect("data/story.db")
    cursor = db.cursor()
    
    query = "SELECT * FROM updates WHERE"
    contributedIDs = getContributedIDs(username)

    if len(contributedIDs) <= 0:
        data = []
        return data

    #construct query from indetermintate # of contributed ids
    isFirst = True
    for i in contributedIDs:
        if isFirst == False:
            query += " OR"
        else:
            isFirst = False
        query += " storyID = " + str(i)
    print(query)

    cursor.execute(query)
    fetch = cursor.fetchall()

    #set up empty array for each set of updates to be distributed into
    updates = {}
    for id in contributedIDs:
        updates[id] = [""]*10
    
    for update in fetch:
        storyID = update[0]
        user = update[1]
        updateNum = update[2]
        text = update[3]

        #change text to bold if it is by the current user
        if user == username:
            updates[storyID][updateNum] = "<b>" + text + "</b>"
        else:
            updates[storyID][updateNum] = text

    data = []
    
    for storyID in updates.keys():
        query = "SELECT title FROM stories WHERE storyID=\"" + str(storyID) + "\""
        cursor.execute(query)
        fetch = cursor.fetchall()

        #join all updates into one cohesive story
        text = " ".join(updates[storyID]).strip()
        data.append({"storyID": storyID, "title": fetch[0][0], "text": text})

    return data



def getStoryInfo(username, ide):

    #connect to database
    ide = int(ide)
    db = sqlite3.connect("data/story.db")
    cursor = db.cursor()
    
    data = {}

    cursor.execute("SELECT text,username from updates WHERE storyID=%d" % (ide))
    updates = cursor.fetchall()

    text = updates[len(updates)-1][0]
        
    cursor.execute("SELECT title,isOpen from stories WHERE storyID=%d" % (ide))
    t = cursor.fetchone()

    title = t[0]

    #throw info for story into one dict
    data["title"] = title
    data["text"] = text
    
    return data
    
