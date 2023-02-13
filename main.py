import tkinter as tk

def add():
    box.insert(tk.END, e.get())
    e.delete(0, tk.END)
def delete():
    if len(box.curselection()) > 0:
        index = box.curselection()[0]
        box.delete(index)
def save():
    f = open('save.txt', 'w', encoding='utf-8')
    tasks = box.get(0, tk.END)
    f.writelines('\n'.join(tasks))
    f.close()

window = tk.Tk()
window.title('To Do List')

f = tk.Frame(window)
f.pack()
box = tk.Listbox(f, width=100, height=20)
box.pack(side=tk.LEFT)
scroll = tk.Scrollbar(f, command=box.yview)
scroll.pack(side=tk.RIGHT, fill=tk.Y)
box.config(yscrollcommand=scroll.set)

tdl = tk.Label(window,text="**TO DO LIST**" ,font="courier 15 italic", width=30, justify="center", fg='purple')
tdl.place(x=120,y=300)
e = tk.Entry(window, width=40,bg='pink')
e.pack()
e.focus()
buttonadd=tk.Button(window, text='Add task', width=40, bg='purple', fg='white', font="courier 9 bold",command=add)
buttonadd.pack()
buttondelete=tk.Button(window, text='Delete task', width=40,bg='black', fg='white', font="courier 9 bold" ,command=delete)
buttondelete.pack()
buttonsave=tk.Button(window, text='Save task', width=40,bg='blue', fg='white', font="courier 9 bold" ,command=save)
buttonsave.pack()


window.mainloop()