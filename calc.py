import tkinter as tk

mainWindow = tk.Tk()
mainWindow.title("CALCULATOR")

heading_label1 = tk.Label(mainWindow, text="Enter First Number",pady=(10),padx=(10))
heading_label1.pack()

name_field = tk.Entry(mainWindow)
name_field.pack()

heading_label2 = tk.Label(mainWindow, text="Enter Second Number",pady=(10),padx=(10))
heading_label2.pack()

name_field2 = tk.Entry(mainWindow)
name_field2.pack()

# def takeValueInput():
#     name = name_field.get()
#     name2 = name_field2.get()
#     print(name)
#     print(name2)

def Addition():
    x = int(name_field.get())
    y = int(name_field2.get())
    # return x+y
    heading_label3.config(text="" +str(x+y))


def Subtraction():
    x = int(name_field.get())
    y = int(name_field2.get())
    # print(x-y)
    # return x-y
    heading_label3.config(text="" +str(x-y))

def Division():
    x = int(name_field.get())
    y = int(name_field2.get())
    # print(x/y)
    # return x/y
    heading_label3.config(text="" + str(x / y))

def Multiplication():
    x = int(name_field.get())
    y = int(name_field2.get())
    # print(x*y)
    # return x*y
    heading_label3.config(text="" + str(x * y))


button = tk.Button(mainWindow, text="+", command=lambda: Addition(),pady=(10),padx=(10))
button.pack()

button1 = tk.Button(mainWindow, text="-", command=lambda: Subtraction(),pady=(10),padx=(10))
button1.pack()

button2 = tk.Button(mainWindow, text="/", command=lambda: Division(),pady=(10),padx=(10))
button2.pack()

button3 = tk.Button(mainWindow, text="*", command=lambda: Multiplication(),pady=(10),padx=(10))
button3.pack()

heading_label3 = tk.Label(mainWindow, text="Result is:")
heading_label3.pack()

mainWindow.mainloop()