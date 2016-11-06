import sqlite3

db = sqlite3.connect("data/story.db")
cursor = db.cursor()

def getFeedData(username):

    query = "SELECT * FROM updates WHERE"
    contributedIDs = getContributedIDs(username)
    
    isFirst = True
    for i in contributedIDs:
        if isFirst == False:
            query += " AND"
        else:
            isFirst = False
        query += " storyID != " + str(i)
    #print(query)

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
                if updateNum > diffupdate[2]:
                    recentUpdates.pop(i)
                    recentUpdates.append(update)
                    replaced = True
                    break
                
        if replaced == False:
            recentUpdates.append(update)

    data = []
    
    for update in recentUpdates:
        query = "SELECT storyName FROM openedPages WHERE storyID=\"" + str(update[0]) + "\""
        cursor.execute(query)
        fetch = cursor.fetchall()
        data.append({"storyID": update[0], "title": fetch[0][0], "text": update[3]})

    return data
    

def getContributedIDs(username):
    
    query = "SELECT storyID FROM updates WHERE username=\"" + username + "\""
    cursor.execute(query)
    fetch = cursor.fetchall()

    data = []
    for i in fetch:
        data.append(i[0])
        
    return data


def getContributedData(username):
    
    query = "SELECT * FROM updates WHERE"
    contributedIDs = getContributedIDs(username)
    
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

    updates = {}
    for id in contributedIDs:
        updates[id] = [""]*10
    
    for update in fetch:
        storyID = update[0]
        user = update[1]
        updateNum = update[2]
        text = update[3]
    
        #print("storyid: " + str(storyID))
        #print("updateNum: " + str(updateNum))
        #print("user: " + user)
        if user == username:
            updates[storyID][updateNum] = "<b>" + text + "</b>"
        else:
            updates[storyID][updateNum] = text

    data = []
    
    for storyID in updates.keys():
        query = "SELECT storyName FROM openedPages WHERE storyID=\"" + str(storyID) + "\""
        cursor.execute(query)
        fetch = cursor.fetchall()
        
        text = " ".join(updates[storyID]).strip()
        data.append({"storyID": storyID, "title": fetch[0][0], "text": text})

    return data
