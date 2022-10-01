from cProfile import label
import time
from tkinter import *
from tkinter import font
def start():
    text=time.strftime("%H:%M:%S")
    label.config(text=text)
    label.after(200,start)

root=Tk()
root.geometry("359x150+0+0")
root.configure(background="black")
root.resizable(0,0)
root.overrideredirect(1)

label=Label(root,font=("ds-digital",50,'bold'),bg='black',fg='red',bd=50)
label.grid(row=0,column=1)
start()
print("Done")
root.mainloop()