from flask import Flask, session, render_template, request, redirect, g

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')