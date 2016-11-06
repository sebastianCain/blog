#To test out html files

from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3, hashlib, os
from utils import auth
runHtml = Flask(__name__)
runHtml.secret_key = os.urandom(32)

data=[]
for x in range(0,20):
    dict={'title': x, 'text':"something"+str(x), 'storyID':x}
    data.append(dict)
    print dict

#----------------------------------
@runHtml.route("/")

def root():
    if session and auth.userCooked(session["user"]):
        return render_template("home.html") #change to home.html
    return render_template("login.html")

#--------------------------------
@runHtml.route("/logout")

def logout():
    session.pop("user")
    return redirect("/")

#----------------------------------------
@runHtml.route("/login", methods=['GET', 'POST'])

def login():
    
    user = request.form["usr"]
    passwd = request.form["pw"]
    
    if auth.authenticate(user, passwd):
        session["user"] = user
        return render_template("home.html",data=data)
    return redirect("/") #something to show the failure maybe but it shows login

#-----------------------------------------
@runHtml.route("/register", methods=['GET', 'POST'])

def register():
    return render_template("register.html")

#------------------------------------------
@runHtml.route("/registerauth", methods=['GET', 'POST'])

def registerauth():
    user = request.form["user"]
    passw = request.form["pass"]
    if (auth.addUser(user,passw) == 2):
        return redirect("/")
    return redirect("/")


if __name__ == "__main__":
    runHtml.debug = True
    runHtml.run()
