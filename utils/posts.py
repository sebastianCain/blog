import sqlite3

def getFeed(username):
    db = sqlite3.connect("data/story.db")
    cursor = db.cursor()

    query = "SELECT * FROM updates WHERE username!=\"" + username + "\""

    cursor.execute(query)
    fetch = cursor.fetchall()

    dict = {}
    
    for i in fetch:
        print(fetch)

