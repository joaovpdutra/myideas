import tkinter as tk
from template_filler import *
from tkinter import messagebox

root = tk.Tk()

root.geometry("450x140")

root.title("Report creator")

recordchoice = tk.StringVar()

def getrecord():
    recordid = recordchoice.get()
    filltemplatepdf(recordid)


record_label = tk.Label(root, text="Record ID", font=('arial', 14, 'bold'))

record_entry = tk.Entry(root, textvariable=recordchoice, font=('arial', 14,'normal'))

submitrecord_btn = tk.Button(root, text = 'Submit', command = getrecord, font=('arial', 12, 'normal'))

record_label.grid(row=0, column=0, padx=20, pady=20)
record_entry.grid(row=0, column=1)
submitrecord_btn.grid(row=1, column=1)


root.mainloop()