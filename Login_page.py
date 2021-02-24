import mysql.connector
from tkinter import *
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="jamo"
)

mycursor = mydb.cursor()


def cleanButton(self):
    self.nameEntry.delete()
    self.AddressEntry.delete()


class register:
    def __init__(self):

        self.cleanButton = None
        self.windowDemo = Tk()
        self.windowDemo.title("RegistrationDemo")
        self.windowDemo.configure(background = "dodgerblue")
        self.windowDemo.geometry("400x450")


        label1 = Label(self.windowDemo, text="name", font="times 15 bold")
        label1.place(x=20, y=10)
        self.nameEntry = Entry(self.windowDemo)
        self.nameEntry.place(x=100, y=10)

        label2 = Label(self.windowDemo, text="address", font="times 15 bold")
        label2.place(x=20, y=50)
        self.AddressEntry = Entry(self.windowDemo)
        self.AddressEntry.place(x=100, y=50)

        btn1 = Button(self.windowDemo, text="submit", font="times 10 bold", command=self.submitComm)
        btn1.place(x=50, y=300)

        btn2 = Button(self.windowDemo, text="clear", font="times 10 bold", command=self.cleanButton)
        btn2.place(x=200, y=300)


    def submitComm(self):
        username = self.nameEntry.get()
        address = self.AddressEntry.get()

        myquerry = "INSERT INTO cust (name, address) VALUES(%s, %s)"
        val = (username, address)

        mycursor.execute(myquerry, val)
        mydb.commit()

        print(mycursor.rowcount, "record inserted")



wind = register()
wind.windowDemo.mainloop()