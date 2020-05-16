from flask import Flask, render_template
from flask import request, redirect
import sqlite3

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

def get_all_students():
    conn = sqlite3.connect('student.db')

    c = conn.cursor()
    sql = "SELECT id, name, intro, avatar FROM students"
    c.execute(sql)
    #print(c.fetchall())
    sts = c.fetchall()
    #ps = [f"{id:<5}{name:<10}{intro:<20}{avatar:>5}"
        #for id, name, intro, avatar in sts]
    #print('\n'.join(ps))
    return sts

@app.route('/')
def school():
    students = get_all_students()
    return render_template('school.html', students = students)

@app.route('/student/<sid>')
def student(sid):
    student = students[sid]
    return render_template('student.html', student = student)