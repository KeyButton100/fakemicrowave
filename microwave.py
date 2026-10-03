from tkinter import *
import time
from tkinter.ttk import *
root=Tk()
root.geometry("400x340")
root.title("Smart Microwave")
root.resizable(True, False)
Label(text="Set Time (Minutes):").pack(pady=20)
n=Spinbox(root, from_=0, to=60, state="readonly")
n.pack(pady=10)
def abc():
    data=n.get()
    print(n.get())
    result.config(text=data)
    p["value"]=data

Label(text="Cooking Progress:").pack(pady=20)
p=Progressbar(root, orient="horizontal", mode="indeterminate")
p.pack(pady=10)
Button(root, text="Start", width=10, command=abc).pack(pady=10)
result=Label(root, text="")
result.pack()
root.mainloop()