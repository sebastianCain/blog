import sqlite3

def getFeed(username):
    db = sqlite3.connect("data/story.db")
    cursor = db.cursor()

    query = "SELECT storyID FROM updates WHERE username!=\"" + name + "\""

    cursor.execute(query)
    fetch = cursor.fetchall()

    print(fetch)
