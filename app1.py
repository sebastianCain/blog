
from flask import Flask

app = Flask(__name__)

@app.route("/")

def init():
	return "this is the first route"

if __name__ == "__main__":
	app.run()