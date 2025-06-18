
import tkinter as tk
import mysql.connector
root  = tk.Tk()
def submit_form():
    name = name_entry.get()
    email = email_entry.get()
    db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="DARAKSHA",
    port=3306
    )
    cursor = db.cursor()
    cursor.execute("ALTER TABLE reg MODIFY id INT AUTO_INCREMENT")
    cursor.execute("INSERT INTO reg (name, email) VALUES (%s, %s)", (name, email))
    db.commit()
    cursor.close()
    db.close()
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    print("Form submitted successfully!")
    print(f"Name : {name} \n Email : {email}")
root.configure(bg="lightblue")    
root.title("Form Example")
root.geometry("500x500")

tk.Label(root, text="Name:").place(x=20, y=20)
name_entry = tk.Entry(root)
name_entry.place(x=100, y=20)

tk.Label(root, text="Email:").place(x=20 , y=60)
email_entry = tk.Entry(root)
email_entry.place(x=100, y=60)

button = tk.Button(root, text="Submit",  command=submit_form)
button.place(x=100, y=100)

root.mainloop()
