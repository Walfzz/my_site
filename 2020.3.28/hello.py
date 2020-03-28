from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    title = 'My Flask Website'
    subtitle = 'Header 3 font!!!'
    return render_template("hello.html", title=title, subtitle = subtitle)