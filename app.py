from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3, hashlib, os
from utils import auth
app = Flask(__name__)
app.secret_key = os.urandom(32)

#----------------------------------
@app.route("/")

def route1():
    if auth.userCooked(session["user"]):
        return render_template("welcome.html") #change to home.html
    return render_template("login.html")

#--------------------------------
@app.route("/logout")

def logout():
    session.pop("user")
    return redirect("/")

#----------------------------------------
@app.route("/login", methods=['GET', 'POST'])

def route2():
    
    user = request.form["usr"]
    passwd = request.form["pw"]
    
    if auth.authenticate(user, passwd):
        session["user"] = user
        return redirect("/")
    return redirect("/") #something to show the failure maybe but it shows login

#-----------------------------------------
@app.route("/register", methods=['GET', 'POST'])

def route3():
    return render_template("register.html")

#------------------------------------------
@app.route("/registerauth", methods=['GET', 'POST'])

def route4():
    user = request.form["user"]
    passw = request.form["pass"]
    if (auth.addUser(user,passw) == "User successfully registered!"):
        return "register successful <a href='/'>back home</a>"
    return redirect("/")

if __name__ == "__main__":
    app.debug = True
    app.run()
