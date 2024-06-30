import tkinter as tk
from template_filler import *
from tkinter import messagebox

#initialise the GUI
root = tk.Tk()
#selecting the size
root.geometry("450x140")
#selecting the title
root.title("Report creator")
#selecting the type of
recordchoice = tk.IntVar()
#defining the function
def getrecord():
    recordid = recordchoice.get()
    filltemplatepdf(recordid)
    lenrecord=len(str(recordid))
    record_entry.delete(0,lenrecord)
    record_entry.insert(0,"")

#creating the GUI elements

#label for the selection of record ID
record_label = tk.Label(root, text="Record ID", font=('arial', 14, 'bold'))
record_label.grid(row=0, column=0, padx=20, pady=20)
#textbox for the record choice
record_entry = tk.Entry(root, textvariable=recordchoice, font=('arial', 14,'normal'))
record_entry.grid(row=0, column=1)
#button to submit and call the function
submitrecord_btn = tk.Button(root, text = 'Submit', command = getrecord, font=('arial', 12, 'normal'))
submitrecord_btn.grid(row=1, column=1)

root.mainloop()