import tkinter as tk
import tkinter.messagebox
import pymysql as mysql
import tkinter.ttk
import Menu


def AddUser(names,windowToClose):
    windowToClose.destroy()
    newName=names

    window = tk.Tk()
    window.geometry('+0+0')
    photo = tk.PhotoImage(file='return.png')
    photo1=photo.subsample(7,7)

    canvas=tk.Canvas(window, height=500, width=500)
    canvas.pack()

    background_image=tk.PhotoImage(file='back.png')
    backgroundLabel=tk.Label(window, image=background_image)
    backgroundLabel.place(relwidth=1,relheight=1)

    label1=tk.Label(window,text=('Add name and email of users to event '+names), bg='#288989', font=20 )
    label1.place(relx=0.025,y=10,height=70,relwidth=0.9, )

    label2 = tk.Label(window, text=('Name'), bg='#288989', font=10)
    label2.place(relx=0.05, y=(90), height=40, relwidth=0.2)
    entry = tk.Entry(window, font=20, bg="#E58C43")
    entry.place(relx=0.3, y=(90), height=40, relwidth=0.3)

    label3 = tk.Label(window, text=('email'), bg='#288989', font=10)
    label3.place(relx=0.05, y=(130), height=40, relwidth=0.2)
    entry2 = tk.Entry(window, font=20, bg="#E58C43")
    entry2.place(relx=0.3, y=(130), height=40, relwidth=0.3)

    button1 = tk.Button(window, text='Add User', bg='#49bd37', command=lambda: insertUser(entry.get(),entry2.get(),names,window) )
    button1.place(relx=0.05, y=180, height=40, relwidth=0.2)

    button= tk.Button(window, image=photo1, bg='grey', command=lambda: Menu.MainMenu(window))
    button.place(relx=0.93,rely=0,relheight=0.07,relwidth=0.07)

    button2 = tk.Button(window, text='Move forward and add expenses', bg='red', command=lambda: addExpenseMenuToSpecificEvent(window,newName) )
    button2.place(relx=0.05, y=300, height=40, relwidth=0.6)

    window.mainloop()








