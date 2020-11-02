import tkinter as tk
import tkinter.messagebox
import pymysql as mysql
import tkinter.ttk
import Menu
import safety
import AddNewEvent

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

def insertUser(name, mail, eventDate, windowToClose):
    connection = mysql.connect(host='localhost',
                                   database='splitwise',
                                   user='root',
                                   password='')
    cursor = connection.cursor()
    mySql_insert_query = """INSERT INTO user (userName, userMail, userEvent) 
                                VALUES (%s, %s, %s ) """

    recordTuple = (name, mail, eventDate)
    cursor.execute(mySql_insert_query, recordTuple)
    connection.commit()
    AddUser(eventDate, windowToClose)

def addExpenseMenuToSpecificEvent(windowToClose,names):


    namesToSQL = "'"+names+"'"

    if windowToClose != None:
        windowToClose.destroy()


    window = tk.Tk()
    window.geometry('+0+0')
    photo = tk.PhotoImage(file='return.png')
    photo1=photo.subsample(7,7)

    canvas=tk.Canvas(window, height=500, width=500)
    canvas.pack()

    background_image=tk.PhotoImage(file='back.png')
    backgroundLabel=tk.Label(window, image=background_image)
    backgroundLabel.place(relwidth=1,relheight=1)

    label1=tk.Label(window,text=('Add name and value of the expense to event!'), bg='#288989', font=20 )
    label1.place(relx=0.025,y=10,height=70,relwidth=0.9, )

    label2 = tk.Label(window, text=('Name'), bg='#288989', font=10)
    label2.place(relx=0.05, y=(90), height=40, relwidth=0.2)
    entry = tk.Entry(window, font=20, bg="#E58C43")
    entry.place(relx=0.3, y=(90), height=40, relwidth=0.3)

    label3 = tk.Label(window, text=('value'), bg='#288989', font=10)
    label3.place(relx=0.05, y=(130), height=40, relwidth=0.2)
    entry2 = tk.Entry(window, font=20, bg="#E58C43")
    entry2.place(relx=0.3, y=(130), height=40, relwidth=0.3)

    label4 = tk.Label(window, text=('Choose a payer'), bg='#288989', font=10)
    label4.place(relx=0.05, y=(180), height=40, relwidth=0.4)

    listbox = tk.Listbox(window, bg="#E58C43")
    listbox.place(relx=0.5, y=(180), relheight=0.3, relwidth=0.3)
    scrollbar = tk.Scrollbar(window)
    scrollbar.place(relx=0.8, y=180,relwidth=0.05,relheight=0.3)
    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)

    con0 = mysql.connect(host='localhost', user='root', password='', database='splitwise')
    cursor0 = con0.cursor()
    cursor0.execute('select * from user where userEvent='+namesToSQL+' ')
    rows = cursor0.fetchall()
    for row in rows:
        insertData = row[1]
        listbox.insert(listbox.size()+1,insertData)
    con0.close()

    amountOfPeople=listbox.size()


    button1 = tk.Button(window, text='Split equally', bg='#49bd37', command=lambda: equalSplit(entry.get(),entry2.get(),window,names,listbox.get('anchor'),amountOfPeople))
    button1.place(relx=0.25, rely=0.8, height=40, relwidth=0.2)

    button2 = tk.Button(window, text='Split unequally', bg='#49bd37', command=lambda: unequalSplit(entry.get(),entry2.get(),window,names,listbox.get('anchor'),amountOfPeople))
    button2.place(relx=0.55, rely=0.8, height=40, relwidth=0.2)

    button= tk.Button(window, image=photo1, bg='grey', command=lambda: Menu.MainMenu(window))
    button.place(relx=0.93,rely=0,relheight=0.07,relwidth=0.07)

    window.mainloop()

def equalSplit(nameOfExpense, value,windowToClose, names,payer,howManyPeople):

    namesToSQL = "'"+names+"'"
    AddNewEvent.sendValuesToExpense(nameOfExpense,value,names,payer)
    con0 = mysql.connect(host='localhost', user='root', password='', database='splitwise')
    cursor0 = con0.cursor()
    cursor0.execute('select * from user where userEvent = '+namesToSQL+' ')
    rows = cursor0.fetchall()
    listOfUsers=[]
    balanceOfUsers=[]
    valuePerPerson= float(value)/float(howManyPeople)

    for row in rows:
        nameOfUser = row[1]
        userBalance=row[4]

        if (userBalance == None):
            userBalance = 0.0
        value = float(value)
        if (nameOfUser != payer):

            userBalance = str(userBalance - valuePerPerson)
            connection = mysql.connect(host='localhost',
                                       database='splitwise',
                                       user='root',
                                       password='')
            cursor = connection.cursor()
            mySql_insert_query = """UPDATE user SET userBalance =(%s) WHERE userName=(%s) """

            recordTuple = (userBalance, nameOfUser)
            cursor.execute(mySql_insert_query, recordTuple)
            connection.commit()
        else:
            userBalance = str(float(userBalance + (value - valuePerPerson)))
            connection = mysql.connect(host='localhost',
                                       database='splitwise',
                                       user='root',
                                       password='')
            cursor = connection.cursor()
            mySql_insert_query = """UPDATE user SET userBalance =(%s) WHERE userName=(%s) """

            recordTuple = (userBalance, nameOfUser)
            cursor.execute(mySql_insert_query, recordTuple)
            connection.commit()
        addExpenseMenuToSpecificEvent(windowToClose,names)

def unequalSplit(nameOfExpense, value, windowToClose, names,payer,howManyPeople):
    AddNewEvent.sendValuesToExpense(nameOfExpense, value, names, payer)

    windowToClose.destroy()
    expenseName=nameOfExpense
    valueOfExpense=value

    window = tk.Tk()
    window.geometry('+0+0')
    photo = tk.PhotoImage(file='return.png')
    photo1=photo.subsample(7,7)

    canvas=tk.Canvas(window, height=300, width=300)
    canvas.pack()

    background_image=tk.PhotoImage(file='back.png')
    backgroundLabel=tk.Label(window, image=background_image)
    backgroundLabel.place(relwidth=1,relheight=1)

    label1=tk.Label(window,text=('How do you want to split it?'), bg='#288989', font=20 )
    label1.place(relx=0.025,y=10,height=70,relwidth=0.9, )


    button1 = tk.Button(window, text='By Percentage', bg='#49bd37', command=lambda: AddNewEvent.percentageSplit(expenseName,valueOfExpense,names,payer,window))
    button1.place(relx=0.05, y=180, height=40, relwidth=0.4)

    button2 = tk.Button(window, text='By specific values', bg='#49bd37', command=lambda: AddNewEvent.specificSplit(expenseName,valueOfExpense,names,payer,window))
    button2.place(relx=0.55, y=180, height=40, relwidth=0.4)

    button= tk.Button(window, image=photo1, bg='grey', command=lambda: Menu.MainMenu(window))
    button.place(relx=0.93,rely=0,relheight=0.07,relwidth=0.07)

    window.mainloop()