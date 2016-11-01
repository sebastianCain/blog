from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3, hashlib, os
from utils import auth

app = Flask(__name__)

#app.secret_key = "mwebfailusgdfaiweflauksbdflakjbsdfiquwe"
app.secret_key = os.urandom(32)

@app.route("/")

def route1():
    if "user" in session:
        return render_template("welcome.html", name= session["user"])
    return render_template("login.html")

@app.route("/logout")

def logout():
    session.pop("user")
    return redirect("/")

@app.route("/login", methods=['GET', 'POST'])

def login():
    return render_template("login.html")

@app.route("/loginauth", methods=['GET', 'POST'])

def route2():
    
    user = request.form["usr"]
    passwd = request.form["pw"]
    
    if auth.authenticate(user, passwd):
        return render_template("welcome.html")
    return redirect("/")


@app.route("/register", methods=['GET', 'POST'])

def route3():
    return render_template("register.html")


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
