# Calculator

# import tkinter
from tkinter import *
from tkinter.ttk import *


root = Tk()
root.title("Roy Calculator")

expression = ""
default_value = 0

# Add function ...
def add(value):
    global expression
    expression += value
    label_result.config(text=expression)
    # expression = value
    # calculate()

# Clear function to clear     
def clear():
    global expression
    expression = ""
    label_result.config(text=expression)
    
def calculate():
    global expression
    result = ""
    if expression != "":
        try:
            result = eval(expression)
        except:
            result = "error"
            expression = ""
    label_result.config(text=result)
    label_Expresult.config(text=expression)
            
def cal_sum(value):
    global expression 
    global default_value
    sum_result = default_value + value
    return sum_result




# Create buttons ........

label_result = Label(root, text="", width=20, background="black", foreground="cyan", anchor="e", font="Arial 20 bold")
label_result.grid(row=0, column=0, columnspan=4)

label_Expresult = Label(root, text=expression, width=40, background="black", foreground="cyan", anchor="e", font="Arial 10 bold italic")
label_Expresult.grid(row=1, column=0, columnspan=4)

button_1 = Button(root, text="1", command=lambda: add("1"))
button_1.grid(row=2, column=0)

button_2 = Button(root, text="2", command=lambda: add("2"))
button_2.grid(row=2, column=1)

button_3 = Button(root, text="3", command=lambda: add("3"))
button_3.grid(row=2, column=2)

button_divide = Button(root, text="/", command=lambda: add("/"))
button_divide.grid(row=2, column=3)

button_4 = Button(root, text="4", command=lambda: add("4"))
button_4.grid(row=3, column=0)

button_5 = Button(root, text="5", command=lambda: add("5"))
button_5.grid(row=3, column=1)

button_6 = Button(root, text="6", command=lambda: add("6"))
button_6.grid(row=3, column=2)

button_multiply = Button(root, text="*", command=lambda: add("*"))
button_multiply.grid(row=3, column=3)

button_7 = Button(root, text="7", command=lambda: add("7"))
button_7.grid(row=4, column=0)

button_8 = Button(root, text="8", command=lambda: add("8"))
button_8.grid(row=4, column=1)

button_9 = Button(root, text="9", command=lambda: add("9"))
button_9.grid(row=4, column=2)

button_subtract = Button(root, text="-", command=lambda: add("-"))
button_subtract.grid(row=4, column=3)

button_clear = Button(root, text="C", command=lambda: clear())
button_clear.grid(row=5, column=0)

button_0 = Button(root, text="0", command=lambda: add("0"))
button_0.grid(row=5, column=1)

button_dot = Button(root, text=".", command=lambda: add("."))
button_dot.grid(row=5, column=2)

button_add = Button(root, text="+", command=lambda: cal_sum(int(label_result)))
button_add.grid(row=5, column=3)

button_equals = Button(root, text="=", width=50, command=lambda: calculate())
button_equals.grid(row=6, column=0, columnspan=4)

root.mainloop()