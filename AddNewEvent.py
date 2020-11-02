import tkinter as tk
import Menu
import tkinter.ttk
import pymysql as mysql
import safety
import Prevent

def Add(windowToClose):
    windowToClose.destroy()
    root2 = tk.Tk()
    root2.geometry('+0+0')
    canvas=tk.Canvas(root2, height=500, width=500)
    canvas.pack()

    photo = tk.PhotoImage(file='return.png')
    photo1=photo.subsample(7,7)

    background_image=tk.PhotoImage(file='back.png')
    backgroundLabel=tk.Label(root2, image=background_image)
    backgroundLabel.place(relwidth=1,relheight=1)


    label1=tk.Label(root2,text='What is this event name?', bg='#288989')
    label1.place(relx=0.02,rely=0.1,relheight=0.1,relwidth=0.4, )
    entry1= tk.Entry(root2, font=15, bg="#E58C43")
    entry1.place(relx=0.42,rely=0.1,relheight=0.1,relwidth=0.4)

    button= tk.Button(root2, image=photo1, bg='grey', command=lambda: Menu.MainMenu(root2))
    button.place(relx=0.93,rely=0,relheight=0.07,relwidth=0.07)


    button1=tk.Button(root2, text='Accept',bg='#49bd37', command=lambda: Prevent.AddUser(entry1.get(),root2))
    button1.place(relx=0.4,rely=0.35,relheight=0.1, relwidth=0.2)

    root2.mainloop()

def eventSee(windowToClose):
    windowToClose.destroy()
    root5 = tk.Tk()
    root5.geometry('+0+0')

    photo = tk.PhotoImage(file='return.png')
    photo1=photo.subsample(7,7)

    canvas=tk.Canvas(root5, height=500, width=500)
    canvas.pack()

    background_image=tk.PhotoImage(file='back.png')
    backgroundLabel=tk.Label(root5, image=background_image, bg='#288989')
    backgroundLabel.place(relwidth=1,relheight=1)


    label4= tk.Label(root5, text = 'Which event would you like to see?', bg='#288989')
    label4.place(relx=0.25,rely=0,relheight=0.05,relwidth=0.6)



    button= tk.Button(backgroundLabel, image=photo1, bg='grey', command=lambda: Menu.MainMenu(root5))
    button.place(relx=0.93,rely=0,relheight=0.07,relwidth=0.07)


    listbox = tk.Listbox(root5)
    listbox.place(relx=0.2, rely=0.1,relwidth=0.6,relheight=0.3)
    scrollbar = tk.Scrollbar(root5)
    scrollbar.place(relx=0.8, rely=0.1,relwidth=0.1,relheight=0.3)
    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)

    con0 = mysql.connect(host='localhost', user='root', password='', database='splitwise')
    cursor0 = con0.cursor()
    cursor0.execute('select distinct userEvent from user ')
    rows = cursor0.fetchall()
    i=1
    for row in rows:
        insertData = row[0]
        listbox.insert(listbox.size()+1,insertData)
        i+=1
    con0.close()

    button1=tk.Button(root5, text='Accept',bg='#49bd37', command=lambda: viewEventMenu(listbox.get('anchor'),root5))
    button1.place(relx=0.4,rely=0.6,relheight=0.1, relwidth=0.2)



    root5.mainloop()

def eventUpdate(windowToClose):

    windowToClose.destroy()
    root4 = tk.Tk()
    root4.geometry('+0+0')

    photo = tk.PhotoImage(file='return.png')
    photo1=photo.subsample(7,7)

    canvas=tk.Canvas(root4, height=500, width=500)
    canvas.pack()

    background_image=tk.PhotoImage(file='back.png')
    backgroundLabel=tk.Label(root4, image=background_image)
    backgroundLabel.place(relwidth=1,relheight=1)

    label4= tk.Label(root4, text = 'Which event would you like to update?', bg='#288989')
    label4.place(relx=0.25,rely=0,relheight=0.05,relwidth=0.6)

    button= tk.Button(backgroundLabel, image = photo1, bg='grey', command=lambda: Menu.MainMenu(root4))
    button.place(relx=0.93,rely=0,relheight=0.07,relwidth=0.07)

    listbox = tk.Listbox(root4)
    listbox.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.3)
    scrollbar = tk.Scrollbar(root4)
    scrollbar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.3)
    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)

    con0 = mysql.connect(host='localhost', user='root', password='', database='splitwise')
    cursor0 = con0.cursor()
    cursor0.execute('select distinct userEvent from user ')
    rows = cursor0.fetchall()
    i = 1
    for row in rows:
        insertData = row[0]
        listbox.insert(listbox.size() + 1, insertData)
        i += 1
    con0.close()

    button1 = tk.Button(root4, text='Update', bg='#49bd37', command=lambda: updateEventMenu(listbox.get('anchor'), root4))
    button1.place(relx=0.3, rely=0.6, relheight=0.1, relwidth=0.4)

    root4.mainloop()

def eventDelete(windowToClose):
    windowToClose.destroy()
    root5 = tk.Tk()
    root5.geometry('+0+0')

    photo = tk.PhotoImage(file='return.png')
    photo1=photo.subsample(7,7)

    canvas=tk.Canvas(root5, height=500, width=500)
    canvas.pack()

    background_image=tk.PhotoImage(file='back.png')
    backgroundLabel=tk.Label(root5, image=background_image)
    backgroundLabel.place(relwidth=1,relheight=1)


    label4= tk.Label(root5, text = 'Which event would you like to delete?', bg='#288989')
    label4.place(relx=0.25,rely=0,relheight=0.05,relwidth=0.6)



    button= tk.Button(backgroundLabel, image=photo1, bg='grey', command=lambda: Menu.MainMenu(root5))
    button.place(relx=0.93,rely=0,relheight=0.07,relwidth=0.07)


    listbox = tk.Listbox(root5)
    listbox.place(relx=0.2, rely=0.1,relwidth=0.6,relheight=0.3)
    scrollbar = tk.Scrollbar(root5)
    scrollbar.place(relx=0.8, rely=0.1,relwidth=0.1,relheight=0.3)
    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)

    con0 = mysql.connect(host='localhost', user='root', password='', database='splitwise')
    cursor0 = con0.cursor()
    cursor0.execute('select distinct userEvent from user ')
    rows = cursor0.fetchall()
    i=1
    for row in rows:
        insertData = row[0]
        listbox.insert(listbox.size()+1,insertData)
        i+=1
    con0.close()

    button1=tk.Button(root5, text='Accept',bg='#49bd37', command=lambda: DelEvent(listbox.get('anchor'),root5))
    button1.place(relx=0.4,rely=0.6,relheight=0.1, relwidth=0.2)



    root5.mainloop()

def DelEvent(names,whichEnd):

    con0 = mysql.connect(host='localhost', user='root', password='', database='splitwise')
    cursor0 = con0.cursor()
    cursor0.execute('delete from user where userEvent=("'+names+'")')
    cursor0.execute("commit")
    eventDelete(whichEnd)

    con0.close()

    con0 = mysql.connect(host='localhost', user='root', password='', database='splitwise')
    cursor0 = con0.cursor()
    cursor0.execute('delete from expense where event=("'+names+'")')
    cursor0.execute("commit")
    eventDelete(whichEnd)

    con0.close()

def updateEventMenu(nameOfEvent,windowToClose):

    windowToClose.destroy()


    window = tk.Tk()
    window.geometry('+0+0')
    photo = tk.PhotoImage(file='return.png')
    photo1=photo.subsample(7,7)

    canvas=tk.Canvas(window, height=300, width=300)
    canvas.pack()

    background_image=tk.PhotoImage(file='back.png')
    backgroundLabel=tk.Label(window, image=background_image)
    backgroundLabel.place(relwidth=1,relheight=1)

    label1=tk.Label(window,text=('What would you like to update?'), bg='#288989', font=20 )
    label1.place(relx=0.025,y=10,height=70,relwidth=0.9, )


    button1 = tk.Button(window, text='Users', bg='#49bd37', command=lambda: updateEventUser(nameOfEvent,window))
    button1.place(relx=0.05, y=180, height=40, relwidth=0.4)

    button2 = tk.Button(window, text='Expenses', bg='#49bd37', command=lambda: updateEventExpense(nameOfEvent,window))
    button2.place(relx=0.55, y=180, height=40, relwidth=0.4)

    button= tk.Button(window, image=photo1, bg='grey', command=lambda: Menu.MainMenu(window))
    button.place(relx=0.93,rely=0,relheight=0.07,relwidth=0.07)

    window.mainloop()

def updateEventExpense(eventName,windowToClose):

    windowToClose.destroy()


    window = tk.Tk()
    window.geometry('+0+0')
    photo = tk.PhotoImage(file='return.png')
    photo1=photo.subsample(7,7)

    canvas=tk.Canvas(window, height=300, width=300)
    canvas.pack()

    background_image=tk.PhotoImage(file='back.png')
    backgroundLabel=tk.Label(window, image=background_image)
    backgroundLabel.place(relwidth=1,relheight=1)

    label1=tk.Label(window,text=('What would you like to do?'), bg='#288989', font=20 )
    label1.place(relx=0.025,y=10,height=70,relwidth=0.9, )


    button1 = tk.Button(window, text='Add expense', bg='#49bd37', command=lambda: Prevent.addExpenseMenuToSpecificEvent(window,eventName))
    button1.place(relx=0.05, y=180, height=40, relwidth=0.4)

    button2 = tk.Button(window, text='Delete expense', bg='#49bd37', command=lambda: updateEventExpenseDelete(eventName,window))
    button2.place(relx=0.55, y=180, height=40, relwidth=0.4)

    button= tk.Button(window, image=photo1, bg='grey', command=lambda: Menu.MainMenu(window))
    button.place(relx=0.93,rely=0,relheight=0.07,relwidth=0.07)

    window.mainloop()

def updateEventUser(eventName,windowToClose):

    windowToClose.destroy()


    window = tk.Tk()
    window.geometry('+0+0')
    photo = tk.PhotoImage(file='return.png')
    photo1=photo.subsample(7,7)

    canvas=tk.Canvas(window, height=300, width=300)
    canvas.pack()

    background_image=tk.PhotoImage(file='back.png')
    backgroundLabel=tk.Label(window, image=background_image)
    backgroundLabel.place(relwidth=1,relheight=1)

    label1=tk.Label(window,text=('What would you like to do?'), bg='#288989', font=20 )
    label1.place(relx=0.025,y=10,height=70,relwidth=0.9, )


    button1 = tk.Button(window, text='Add user', bg='#49bd37', command=lambda: Prevent.AddUser(eventName,window))
    button1.place(relx=0.05, y=180, height=40, relwidth=0.4)

    button2 = tk.Button(window, text='Delete user', bg='#49bd37', command=lambda: updateEventUserDelete(eventName,window))
    button2.place(relx=0.55, y=180, height=40, relwidth=0.4)

    button= tk.Button(window, image=photo1, bg='grey', command=lambda: Menu.MainMenu(window))
    button.place(relx=0.93,rely=0,relheight=0.07,relwidth=0.07)

    window.mainloop()

def specificSplit(nameOfExpense,Value, names,payer,windowToClose):
    windowToClose.destroy()
    con0 = mysql.connect(host='localhost', user='root', password='', database='splitwise')
    cursor0 = con0.cursor()
    cursor0.execute('select * from user where userEvent = '+names+' ')
    rows = cursor0.fetchall()
    listOfUsers=[]
    balanceOfUsers=[]
    for row in rows:
        nameOfUser = row[1]
        balanceOfUser=row[4]



        root4 = tk.Tk()
        root4.geometry('+0+0')

        photo = tk.PhotoImage(file='return.png')
        photo1=photo.subsample(7,7)

        canvas=tk.Canvas(root4, height=500, width=500)
        canvas.pack()

        background_image=tk.PhotoImage(file='back.png')
        backgroundLabel=tk.Label(root4, image=background_image)
        backgroundLabel.place(relwidth=1,relheight=1)

        label1 = tk.Label(root4, text=('How much does user: ',nameOfUser, ' pay?'), bg='#288989', font=20)
        label1.place(relx=0.05, y=10, height=70, relwidth=0.9)

        entry2 = tk.Entry(root4, font=20, bg="#E58C43")
        entry2.place(relx=0.05, y=(100), height=80, relwidth=0.475)

        button1 = tk.Button(root4, text='Accept', bg='#49bd37', command=lambda: addingValueToUser((float(entry2.get())), root4,nameOfUser,balanceOfUser,names,payer,Value))
        button1.place(relx=0.55, y=100, relheight=0.1, relwidth=0.475)

        root4.mainloop()
    con0.close()
    addExpenseMenuToSpecificEvent(None, names)

def percentageSplit(nameOfExpense,Value, names,payer,windowToClose):
    namesToSQL = "'"+names+"'"
    windowToClose.destroy()
    con0 = mysql.connect(host='localhost', user='root', password='', database='splitwise')
    cursor0 = con0.cursor()
    cursor0.execute('select * from user where userEvent = '+namesToSQL+' ')
    rows = cursor0.fetchall()
    listOfUsers=[]
    balanceOfUsers=[]
    for row in rows:
        nameOfUser = row[1]
        balanceOfUser=row[4]



        root4 = tk.Tk()
        root4.geometry('+0+0')

        photo = tk.PhotoImage(file='return.png')
        photo1=photo.subsample(7,7)

        canvas=tk.Canvas(root4, height=500, width=500)
        canvas.pack()

        background_image=tk.PhotoImage(file='back.png')
        backgroundLabel=tk.Label(root4, image=background_image)
        backgroundLabel.place(relwidth=1,relheight=1)

        label1 = tk.Label(root4, text=('How many % should user: ',nameOfUser, ' pay?'), bg='#288989', font=20)
        label1.place(relx=0.05, y=10, height=70, relwidth=0.9)

        entry2 = tk.Entry(root4, font=20, bg="#E58C43")
        entry2.place(relx=0.05, y=(100), height=80, relwidth=0.475)

        button1 = tk.Button(root4, text='Accept', bg='#49bd37', command=lambda: addingValueToUser((float(entry2.get())/float(100))*float(Value), root4,nameOfUser,balanceOfUser,names,payer,Value))
        button1.place(relx=0.55, y=100, relheight=0.1, relwidth=0.475)

        root4.mainloop()
    con0.close()
    Prevent.addExpenseMenuToSpecificEvent(None, names)

def addingValueToUser(amountToUser, windowToClose,userName,userBalance,eventName,payer,Value):

    windowToClose.destroy()
    if(userBalance==None):
        userBalance=0.0
    amountToUser=float(amountToUser)
    Value=float(Value)
    if(userName != payer):

        userBalance=str(userBalance-amountToUser)
        connection = mysql.connect(host='localhost',
                               database='splitwise',
                               user='root',
                               password='')
        cursor = connection.cursor()
        mySql_insert_query = """UPDATE user SET userBalance =(%s) WHERE userName=(%s) """

        recordTuple = (userBalance,userName)
        cursor.execute(mySql_insert_query, recordTuple)
        connection.commit()
    else:
        userBalance=str(float(userBalance+(Value-amountToUser)))
        connection = mysql.connect(host='localhost',
                               database='splitwise',
                               user='root',
                               password='')
        cursor = connection.cursor()
        mySql_insert_query = """UPDATE user SET userBalance =(%s) WHERE userName=(%s) """


        recordTuple = (userBalance,userName)
        cursor.execute(mySql_insert_query, recordTuple)
        connection.commit()

def sendValuesToExpense(name,value,event,payer):
    connection = mysql.connect(host='localhost',
                               database='splitwise',
                               user='root',
                               password='')
    cursor = connection.cursor()
    mySql_insert_query = """INSERT INTO expense (name, value, event,payer) 
                                    VALUES (%s, %s, %s,%s ) """

    recordTuple = (name, value, event,payer)
    cursor.execute(mySql_insert_query, recordTuple)
    connection.commit()

def updateEventUserDelete(nameOfEvent,windowToClose):

    nameOfEvent="'"+nameOfEvent+"'"
    windowToClose.destroy()
    root5 = tk.Tk()
    root5.geometry('+0+0')

    photo = tk.PhotoImage(file='return.png')
    photo1=photo.subsample(7,7)

    canvas=tk.Canvas(root5, height=500, width=500)
    canvas.pack()

    background_image=tk.PhotoImage(file='back.png')
    backgroundLabel=tk.Label(root5, image=background_image)
    backgroundLabel.place(relwidth=1,relheight=1)

    label4= tk.Label(root5, text = 'Which user would you like to delete?', bg='#288989')
    label4.place(relx=0.25,rely=0,relheight=0.05,relwidth=0.6)

    button= tk.Button(backgroundLabel, image=photo1, bg='grey', command=lambda: Menu.MainMenu(root5))
    button.place(relx=0.93,rely=0,relheight=0.07,relwidth=0.07)

    listbox = tk.Listbox(root5)
    listbox.place(relx=0.2, rely=0.1,relwidth=0.6,relheight=0.3)
    scrollbar = tk.Scrollbar(root5)
    scrollbar.place(relx=0.8, rely=0.1,relwidth=0.1,relheight=0.3)
    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)

    con0 = mysql.connect(host='localhost', user='root', password='', database='splitwise')
    cursor0 = con0.cursor()
    cursor0.execute('select userName from user where ''userEvent'' = '+nameOfEvent+' ')
    rows = cursor0.fetchall()
    i=1
    for row in rows:
        insertData = row[0]
        listbox.insert(listbox.size()+1,insertData)
        i+=1
    con0.close()

    button1=tk.Button(root5, text='Delete',bg='#49bd37', command=lambda: delUser(listbox.get('anchor'),nameOfEvent,root5))
    button1.place(relx=0.4,rely=0.6,relheight=0.1, relwidth=0.2)
    root5.mainloop()

def updateEventExpenseDelete(nameOfEvent,windowToClose):

    nameOfEvent="'"+nameOfEvent+"'"
    windowToClose.destroy()
    root5 = tk.Tk()
    root5.geometry('+0+0')

    photo = tk.PhotoImage(file='return.png')
    photo1=photo.subsample(7,7)

    canvas=tk.Canvas(root5, height=500, width=500)
    canvas.pack()

    background_image=tk.PhotoImage(file='back.png')
    backgroundLabel=tk.Label(root5, image=background_image)
    backgroundLabel.place(relwidth=1,relheight=1)

    label4= tk.Label(root5, text = 'Which expense would you like to delete?', bg='#288989')
    label4.place(relx=0.25,rely=0,relheight=0.05,relwidth=0.6)

    button= tk.Button(backgroundLabel, image=photo1, bg='grey', command=lambda: Menu.MainMenu(root5))
    button.place(relx=0.93,rely=0,relheight=0.07,relwidth=0.07)

    listbox = tk.Listbox(root5)
    listbox.place(relx=0.2, rely=0.1,relwidth=0.6,relheight=0.3)
    scrollbar = tk.Scrollbar(root5)
    scrollbar.place(relx=0.8, rely=0.1,relwidth=0.1,relheight=0.3)
    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)

    con0 = mysql.connect(host='localhost', user='root', password='', database='splitwise')
    cursor0 = con0.cursor()
    cursor0.execute('select * from expense where ''event'' = '+nameOfEvent+' ')
    rows = cursor0.fetchall()
    i=1
    for row in rows:
        insertData = "expense"+row[1]+"worth"+row[2]
        listbox.insert(listbox.size()+1,insertData)
        i+=1
    con0.close()

    button1=tk.Button(root5, text='Delete',bg='#49bd37', command=lambda: delExpense(listbox.get('anchor'),nameOfEvent,root5))
    button1.place(relx=0.4,rely=0.6,relheight=0.1, relwidth=0.2)
    root5.mainloop()

def delUser(userName,eventName,windowToClose):
    userName=str(userName)
    eventName=str(eventName)
    userName="'"+userName+"'"
    #eventName = "'" + eventName + "'"
    con0 = mysql.connect(host='localhost', user='root', password='', database='splitwise')
    cursor0 = con0.cursor()
    cursor0.execute('delete from user where userName='+userName+' and userEvent='+eventName+'')
    cursor0.execute("commit")
    Menu.MainMenu(windowToClose)

    con0.close()

def delExpense(nameOfExpense,eventName,windowToClose):
    nameOfExpense=str(nameOfExpense)
    eventName=str(eventName)
    nameOfExpense="'"+nameOfExpense+"'"
    #eventName = "'" + eventName + "'"
    con0 = mysql.connect(host='localhost', user='root', password='', database='splitwise')
    cursor0 = con0.cursor()
    cursor0.execute('delete from expense where name='+nameOfExpense+' and event='+eventName+'')
    cursor0.execute("commit")
    Menu.MainMenu(windowToClose)

    con0.close()

def viewEventMenu(nameOfEvent,windowToClose):

    windowToClose.destroy()


    window = tk.Tk()
    window.geometry('+0+0')
    photo = tk.PhotoImage(file='return.png')
    photo1=photo.subsample(7,7)

    canvas=tk.Canvas(window, height=300, width=300)
    canvas.pack()

    background_image=tk.PhotoImage(file='back.png')
    backgroundLabel=tk.Label(window, image=background_image)
    backgroundLabel.place(relwidth=1,relheight=1)

    label1=tk.Label(window,text=('What would you like to do?'), bg='#288989', font=20 )
    label1.place(relx=0.025,y=10,height=70,relwidth=0.9, )


    button1 = tk.Button(window, text='View users balance', bg='#49bd37', command=lambda: viewEventBalance(nameOfEvent,window))
    button1.place(relx=0.05, y=180, height=40, relwidth=0.4)

    button2 = tk.Button(window, text='View expense history', bg='#49bd37', command=lambda: viewEventHistory(nameOfEvent,window))
    button2.place(relx=0.55, y=180, height=40, relwidth=0.4)

    button= tk.Button(window, image=photo1, bg='grey', command=lambda: Menu.MainMenu(window))
    button.place(relx=0.93,rely=0,relheight=0.07,relwidth=0.07)

    window.mainloop()

def viewEventBalance(nameOfEvent, windowToClose):

    nameOfEvent="'"+nameOfEvent+"'"
    windowToClose.destroy()
    root5 = tk.Tk()
    root5.geometry('+0+0')

    photo = tk.PhotoImage(file='return.png')
    photo1=photo.subsample(7,7)

    canvas=tk.Canvas(root5, height=500, width=500)
    canvas.pack()

    background_image=tk.PhotoImage(file='back.png')
    backgroundLabel=tk.Label(root5, image=background_image)
    backgroundLabel.place(relwidth=1,relheight=1)

    label4= tk.Label(root5, text = 'Balance of users from this event', bg='#288989')
    label4.place(relx=0.25,rely=0,relheight=0.05,relwidth=0.6)

    button= tk.Button(backgroundLabel, image=photo1, bg='grey', command=lambda: Menu.MainMenu(root5))
    button.place(relx=0.93,rely=0,relheight=0.07,relwidth=0.07)

    listbox = tk.Listbox(root5)
    listbox.place(relx=0.2, rely=0.1,relwidth=0.6,relheight=0.3)
    scrollbar = tk.Scrollbar(root5)
    scrollbar.place(relx=0.8, rely=0.1,relwidth=0.1,relheight=0.3)
    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)

    con0 = mysql.connect(host='localhost', user='root', password='', database='splitwise')
    cursor0 = con0.cursor()
    cursor0.execute('select * from user where ''userEvent'' = '+nameOfEvent+' ')
    rows = cursor0.fetchall()
    i=1
    for row in rows:
        insertData = "User: "+str(row[1])+" has balance of "+str(row[4])
        listbox.insert(listbox.size()+1,insertData)
        i+=1
    con0.close()
    root5.mainloop()

def viewEventHistory(nameOfEvent, windowToClose):

    nameOfEvent="'"+nameOfEvent+"'"
    windowToClose.destroy()
    root5 = tk.Tk()
    root5.geometry('+0+0')

    photo = tk.PhotoImage(file='return.png')
    photo1=photo.subsample(7,7)

    canvas=tk.Canvas(root5, height=500, width=500)
    canvas.pack()

    background_image=tk.PhotoImage(file='back.png')
    backgroundLabel=tk.Label(root5, image=background_image)
    backgroundLabel.place(relwidth=1,relheight=1)

    label4= tk.Label(root5, text = 'History of expenses', bg='#288989')
    label4.place(relx=0.25,rely=0,relheight=0.05,relwidth=0.6)

    button= tk.Button(backgroundLabel, image=photo1, bg='grey', command=lambda: Menu.MainMenu(root5))
    button.place(relx=0.93,rely=0,relheight=0.07,relwidth=0.07)

    listbox = tk.Listbox(root5)
    listbox.place(relx=0.2, rely=0.1,relwidth=0.6,relheight=0.3)
    scrollbar = tk.Scrollbar(root5)
    scrollbar.place(relx=0.8, rely=0.1,relwidth=0.1,relheight=0.3)
    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)

    con0 = mysql.connect(host='localhost', user='root', password='', database='splitwise')
    cursor0 = con0.cursor()
    cursor0.execute('select * from expense where ''event'' = '+nameOfEvent+' ')
    rows = cursor0.fetchall()
    i=1
    for row in rows:
        insertData = "Expense: "+str(row[1])+" worth "+str(row[2])+"paid by: "+str(row[4])
        listbox.insert(listbox.size()+1,insertData)
        i+=1
    con0.close()
    root5.mainloop()