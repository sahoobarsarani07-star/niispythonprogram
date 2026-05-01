import sqlite3
conn = sqlite3.connect("student.db")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS student (roll INTEGER, name TEXT, mark REAL)")
cur.execute("INSERT INTO student VALUES (2, 'gita', 95)")
conn.commit()
conn.close()
print("Data inserted successfully")