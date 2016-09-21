from flask import Flask

app = Flask(__name__)

@app.route("/")

def init():
	return "this is the second route"

if __name__ == "__main__":
	app.run()