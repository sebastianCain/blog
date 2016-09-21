from flask import Flask

app = Flask(__name__)

@app.route("/")

def route1():
	return render_template("index.html", title = "lmaoaml")

@app.route("/two")

def route2():
	return "this is the second route."

@app.route("/three")

def route3():
	return "this is the third route"

if __name__ == "__main__":
    app.debug = True
    app.run()
