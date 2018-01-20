from tkinter import *

# instantiate
window=Tk()

def km_to_miles():
    miles = float(e1_value.get())*1.6
    t1.insert(END,miles)

b1 = Button(window, text="Execute", command=km_to_miles)
# adding some attributes to the button
b1.grid(row=0, column=0)

e1_value=StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

t1=Text(window,height=1, width=20)
t1.grid(row=0, column=2)
# shall be in the end of the code
window.mainloop()
