from flask import Flask, render_template, request
import hashlib

app = Flask(__name__)

@app.route("/")

def route1():
    return render_template("index.html")

@app.route("/login", methods=['POST'])

def login():
    return render_template("login.html")

@app.route("/loginauth", methods=['POST'])

def route2():
    print request.method
    if request.form["user"] == "tester" and request.form["pass"] == "pass":
        return "login successful"
    return "login unsuccessful. try again"

@app.route("/register")

def route3():
    return render_template("login.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
