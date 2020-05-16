import sqlite3  
conn = sqlite3.connect('student.db')

c = conn.cursor()
sql = "SELECT id, name, intro, avatar FROM students"
c.execute(sql)
#print(c.fetchall())
sts = c.fetchall()
ps = [f"{id:<5}{name:<10}{intro:<20}{avatar:>5}"
      for id, name, intro, avatar in sts]
print('\n'.join(ps))