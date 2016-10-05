from flask import Flask, render_template, request
import hashlib

app = Flask(__name__)

@app.route("/")

def route1():
    return render_template("index.html")

@app.route("/login", methods=['GET', 'POST'])

def login():
    return render_template("login.html")

@app.route("/loginauth", methods=['GET', 'POST'])

def route2():
    print request.method
    
    occu = open("data/auth.csv", "r")
    streamy = occu.read()
    
    data = streamy.strip().split("\n")
    for i in data:
        line = i.split(",")
        user = request.form["user"]
        hashobject = hashlib.sha256(request.form["pass"])
        hexdig = hashobject.hexdigest()
        if user == line[0] and hexdig == line[1]:
            return "login successful"
    return "login unsuccessful. <a href='/login'>try again</a>"

@app.route("/register", methods=['GET', 'POST'])

def route3():
    return render_template("register.html")

@app.route("/registerauth", methods=['GET', 'POST'])

def route4():
    occu = open("data/auth.csv", "a")
    hashobject = hashlib.sha256(request.form["pass"])
    hexdig = hashobject.hexdigest()
    occu.write(request.form["user"] + "," + hexdig + "\n")

    return "register successful <a href='/'>back home</a>"

if __name__ == "__main__":
    app.debug = True
    app.run()
