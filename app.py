from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3, hashlib, os
from utils import auth, newStory, addUpdate, posts
app = Flask(__name__)
app.secret_key = os.urandom(32)

#----------------------------------
@app.route("/")

def root():
    if session and auth.userCooked(session["user"]):
        return render_template("home.html") #change to home.html
    return render_template("login.html")

#--------------------------------
@app.route("/logout")

def logout():
    session.pop("user")
    return redirect("/")

#----------------------------------------
@app.route("/login", methods=['GET', 'POST'])

def login():
    
    user = request.form["usr"]
    passwd = request.form["pw"]
    
    if auth.authenticate(user, passwd):
        session["user"] = user
        return redirect("/feed")
    return redirect("/") #something to show the failure maybe but it shows login

#-----------------------------------------
@app.route("/register", methods=['GET', 'POST'])

def register():
    return render_template("register.html")

#------------------------------------------
@app.route("/registerauth", methods=['GET', 'POST'])

def registerauth():
    user = request.form["user"]
    passw = request.form["pass"]
    if (auth.addUser(user,passw) == 2):
        return redirect("/")
    return redirect("/")

#------------------------------------------
@app.route("/feed")

def feed():
    data = posts.getFeedData(session["user"])
    return render_template("home.html", data=data, user=session["user"])

#------------------------------------------
@app.route("/contributed")

def contributed():
    data = getContributedData(session["user"])
    return render_template("contributed.html", data=data)

#------------------------------------------
@app.route("/viewstory")

def viewstory():
    #grab data (title, text) here to enter into template as arg
    return render_template("viewstory.html")

#------------------------------------------
@app.route("/newstory")

def newstory():
    return render_template("newstory.html")

#------------------------------------------
@app.route("/updatestory")

def updatestory():
    return render_template("updatestory.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
