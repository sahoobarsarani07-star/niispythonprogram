import tkinter as tk
from tkinter import messagebox
import mysql.connector

# ---------- Database Connection ----------
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="employee"
    )

# ---------- Insert ----------
def insert_data():
    i = id_entry.get()
    n = name_entry.get()
    d = department_entry.get()
    s = salary_entry.get()
    c = city_entry.get()

    con = get_connection()
    cur = con.cursor()

    sql = "INSERT INTO employee VALUES(%s,%s,%s,%s,%s)"
    cur.execute(sql,(i,n,d,s,c))

    con.commit()
    con.close()

    messagebox.showinfo("Success","Record Inserted")

# ---------- Select ----------
def show_data():
    con = get_connection()
    cur = con.cursor()

    cur.execute("SELECT * FROM employee")

    rows = cur.fetchall()

    text_area.delete(1.0, tk.END)

    for r in rows:
        text_area.insert(tk.END,str(r)+"\n")

    con.close()

# ---------- Update ----------
def update_data():
    i = id_entry.get()
    n = name_entry.get()
    d = department_entry.get()
    s = salary_entry.get()
    c = city_entry.get()

    con = get_connection()
    cur = con.cursor()

    sql = "UPDATE employee SET name=%s, department=%s, salary=%s, city=%s WHERE id=%s"
    cur.execute(sql, (n, d, s, c, i))

    con.commit()
    con.close()

    messagebox.showinfo("Success","Record Updated")

# ---------- Delete ----------
def delete_data():
    i = id_entry.get()

    con = get_connection()
    cur = con.cursor()

    sql = "DELETE FROM employee WHERE id=%s"
    cur.execute(sql, (i,))

    con.commit()
    con.close()

    messagebox.showinfo("Success","Record Deleted")

# ---------- GUI ----------
root = tk.Tk()
root.title("Employee Management System")
root.geometry("500x400")

# Labels
tk.Label(root,text="Id").place(x=50,y=50)
tk.Label(root,text="Name").place(x=50,y=90)
tk.Label(root,text="Department").place(x=50,y=130)
tk.Label(root,text="Salary").place(x=50,y=170)
tk.Label(root,text="City").place(x=50,y=210)

# Entry boxes
id_entry = tk.Entry(root)
id_entry.place(x=150,y=50)

name_entry = tk.Entry(root)
name_entry.place(x=150,y=90)

department_entry = tk.Entry(root)
department_entry.place(x=150,y=130)

salary_entry = tk.Entry(root)
salary_entry.place(x=150,y=170)

city_entry = tk.Entry(root)
city_entry.place(x=150,y=210)

# Buttons
tk.Button(root,text="Insert",command=insert_data).place(x=50,y=260)

tk.Button(root,text="Show",command=show_data).place(x=120,y=260)

tk.Button(root,text="Update",command=update_data).place(x=190,y=260)

tk.Button(root,text="Delete",command=delete_data).place(x=260,y=260)

# Text area
text_area = tk.Text(root,width=50,height=10)
text_area.place(x=50,y=310)

root.mainloop()