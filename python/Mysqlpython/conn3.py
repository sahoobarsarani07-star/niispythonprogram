import mysql.connector
con = mysql.connector.connect(
	host="localhost",
	user="root",
	password="root",
	database="employee"
)
if con:
	print("connected")
else:
	print("not connected")
cur = con.cursor()
cur.execute("SELECT * FROM employee")
rows = cur.fetchall()
print("\nEmployee Records:\n")
for r in rows:
    print("Id:", r[0])
    print("Name   :", r[1])
    print("Department :", r[2])
    print("Salary :", r[3])
    print("City :", r[4])
    print("-------------------")
con.close()