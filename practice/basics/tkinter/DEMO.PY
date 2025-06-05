import tkinter as tk

root = tk.Tk()
root.title("Demo GUI")
root.geometry("500x500")

# b1 = tk.Button(root, text="Button 1")
# b1.pack(side='top')

# b2 = tk.Button(root, text="Button 2")
# b2.pack(side='bottom')

# b3 = tk.Button(root, text="Button 3")
# b3.pack(side='left')

# b4 = tk.Button(root, text="Button 4")
# b4.pack(side='right')

# b1 = tk.Button(root, text="Button 1")
# b1.grid(row=0, column=0)

# b2 = tk.Button(root, text="Button 2")
# b2.grid(row=1, column=1)

# b3 = tk.Button(root, text="Button 3")
# b3.grid(row=2, column=2)

# b4 = tk.Button(root, text="Button 4")
# b4.grid(row=3, column=3)


b1 = tk.Button(root, text="Button 1")
b1.place(x=50, y=50)

b2 = tk.Button(root, text="Button 2")
b2.place(x=150, y=50)

b3 = tk.Button(root, text="Button 3")
b3.place(x=50, y=150)

b4 = tk.Button(root, text="Button 4")
b4.place(x=150, y=150)

root.mainloop()