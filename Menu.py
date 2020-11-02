import tkinter as tk
import tkinter.ttk
import tkinter.messagebox
import pymysql as mysql
import safety
import AddNewEvent

def MainMenu(whichRootToDestroy):
    if whichRootToDestroy != None:
        whichRootToDestroy.destroy()
    root = tk.Tk()
    root.geometry('+0+0')
    background_image=tk.PhotoImage(file='back.png')


    canvas=tk.Canvas(root, height=500, width=500)
    canvas.pack()

    frame = tk.Label(root, image=background_image)
    frame.place(x=0,y=0,relheight=1,relwidth=1)

    button1= tk.Button(frame,text = 'Add new event',  bg='#49bd37',  command=lambda: AddNewEvent.Add(root))
    button1.place(relx=0.2,rely=0.2,relheight=0.25,relwidth=0.25)

    button2= tk.Button(frame, text = 'Check list of events', bg='#49bd37', command =lambda: AddNewEvent.eventSee(root))
    button2.place(relx=0.55,rely=0.2,relheight=0.25,relwidth=0.25)

    button3= tk.Button(frame, text = 'Update event', bg='#49bd37', command =lambda: AddNewEvent.eventUpdate(root))
    button3.place(relx=0.2,rely=0.55,relheight=0.25,relwidth=0.25)

    button4= tk.Button(frame, text = 'Delete event', bg='#49bd37', command =lambda: AddNewEvent.eventDelete(root))
    button4.place(relx=0.55,rely=0.55,relheight=0.25,relwidth=0.25)

    root.mainloop()

MainMenu(None)









