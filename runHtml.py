#To test out html files

from flask import Flask, render_template

runHtml=Flask(__name__)

@runHtml.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    runHtml.debug = True
    runHtml.run()
