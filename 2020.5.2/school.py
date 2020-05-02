from flask import Flask, render_template
from flask import request, redirect

app = Flask(__name__)

students = {
    's01': {'name': 'leuk', 'intro': "Hi I'm the first son of a female dog in this school",
    'avatar': '/static/img/Acute-Dog-Diarrhea-47066074.jpg'},
    's02': {'name': 'leuk2.0', 'intro': "Hi I'm the second son of a female dog in this school",
    'avatar': '/static/img/file-20200309-118956-1cqvm6j.jpg'},
    's03': {'name': 'leuk3.0', 'intro': "Hi I'm the third son of a female dog in this school",
    'avatar': '/static/img/weblogo.png'},
    's04': {'name': 'leuk4.0', 'intro': "Hi I'm the fourth son of a female dog in this school",
    'avatar': '/static/img/1708575.jpg'},
    's05': {'name': 'leuk5.0', 'intro': "Hi I'm the fifth son of a female dog in this school",
    'avatar': '/static/img/s-l300.jpg'},
}

@app.route('/')
def school():
    return render_template('school.html', students = students)

@app.route('/student/<sid>')
def student(sid):
    student = students[sid]
    return render_template('student.html', student = student)