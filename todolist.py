from tkinter import *
from tkinter import ttk

dic = {}
dic['row_val'] = 3
    
def decrease_row_val():
    dic['row_val'] -= 1


def getnote(*args):
    try:
        task = str(note.get())
        l = ttk.Label(frm, text=task)
        l.grid(column=1, row = dic['row_val'])
        note_entry.delete(0, END)
        a = ttk.Button(frm, text="Remove note")
        a.grid(column=2, row = dic['row_val'])
        a['command'] = lambda: [l.destroy(), a.destroy(), decrease_row_val()]
        dic['row_val'] +=1
    except ValueError:
        pass

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Todolist").grid(column=1, row=0)
a = ttk.Label(frm, text="Enter task:").grid(column=0, row=1)
note = StringVar()
note_entry = ttk.Entry(frm,  textvariable=note)
note_entry.grid(column=1,row=1)
ttk.Button(frm, text="Add task", command=getnote).grid(column=2, row=1)

root.mainloop()
