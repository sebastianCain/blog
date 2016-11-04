#To test out html files

from flask import Flask, render_template, request

runHtml=Flask(__name__)
@runHtml.route("/")
def story():
    return render_template("writeStory.html")

@runHtml.route("/home", methods=['POST'])
def home():
    story=request.form["story"]
    title=request.form["title"]
    print story + ", " + title
    return render_template("home.html",s=story, t=title)

if __name__ == "__main__":
    runHtml.debug = True
    runHtml.run()
