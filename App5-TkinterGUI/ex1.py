from tkinter import *

# instantiate
window=Tk()

def kg_to_othermetrics():
    grams = float(e1_value.get())*1000
    pounds = float(e1_value.get())*2.20462
    ounces = float(e1_value.get())*35.274
    # delete is in order to clear the text
    t1.delete(1.0, END)
    t1.insert(END,grams)
    t2.delete(1.0, END)
    t2.insert(END, pounds)
    t3.delete(1.0, END)
    t3.insert(END, ounces)

# Label - KG
l1 = Label(window, text="Kg")
l1.grid(row=0, column=0)

#Entry
e1_value=StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

#Button
b1 = Button(window, text="Convert", command=kg_to_othermetrics)
b1.grid(row=0, column=2)

#Text - outputs
t1=Text(window,height=1, width=20)
t1.grid(row=1, column=0)

t2=Text(window,height=1, width=20)
t2.grid(row=1, column=1)

t3=Text(window,height=1, width=20)
t3.grid(row=1, column=2)
# shall be in the end of the code
window.mainloop()
