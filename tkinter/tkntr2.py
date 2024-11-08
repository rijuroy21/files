import tkinter

win=tkinter.Tk()
win.title("Page")
win.geometry('300x300')
win.minsize(200,200)
win.maxsize(400,400)
win.config(background="green")


def data():
    res=tkinter.Tk()
    res.title("Page")
    res.geometry('300x300')
    res.config(background="black")
    l2=tkinter.Label(res)
    l2.pack()
    text=e1.get()
    l2.config(text=text)
l1=tkinter.Label(win,text='welcome')
l1.pack()
e1=tkinter.Entry(win,background='white',foreground='black')
e1.pack()
b1=tkinter.Button(win,text='submit',background='blue',foreground='white',padx=2,pady=2,command=data)
b1.pack()
win.mainloop()