import sqlite3  
conn = sqlite3.connect('student.db')


c = conn.cursor()
sql = """
  INSERT INTO students (name, intro, avatar)
  VALUES (?, ?, ?)
"""
c.execute(sql, ('leuk1.0', "I'm leuk1.0", '/static/img/Acute-Dog-Diarrhea-47066074.jpg'))
c.execute(sql, ('leuk2.0', "I'm leuk2.0", '/static/img/file-20200309-118956-1cqvm6j.jpg'))
c.execute(sql, ('leuk3.0', "I'm leuk3.0", '/static/img/weblogo.png'))

conn.commit()
conn.close()
