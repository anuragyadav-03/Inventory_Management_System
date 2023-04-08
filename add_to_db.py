#import all the modules
from tkinter import *
import mysql.connector
from mysql.connector import Error
import tkinter.messagebox
import os

conn=mysql.connector.connect(host='localhost',
                                       database='inventory_system',
                                       user='root',
                                       password='')
mycursor = conn.cursor()
mycursor.execute("SELECT Max(id) from inventory")
result = mycursor.fetchall()
for r in result:
    id=r[0]

class Database:
    def __init__(self,master,*args,**kwargs):
         self.master=master
         self.heading=Label(master,text="Add in the database",font=('arial 40 bold'),fg='steelblue')
         self.heading.place(x=400,y=0)


         #lables for the window
         self.name_l=Label(master,text="Enter Product Name",font=('arial 18 bold'))
         self.name_l.place(x=10,y=100)

         self.stock_l=Label(master,text="Enter Stocks",font=('arial 18 bold'))
         self.stock_l.place(x=10,y=150)

         self.cp_l = Label(master, text="Enter Cost Price ", font=('arial 18 bold'))
         self.cp_l.place(x=10, y=200)


        #enteries for window

         self.name_e=Entry(master,width=25,font=('arial 18 bold'))
         self.name_e.place(x=380,y=100)

         self.stock_e = Entry(master, width=25, font=('arial 18 bold'))
         self.stock_e.place(x=380, y=150)

         self.cp_e = Entry(master, width=25, font=('arial 18 bold'))
         self.cp_e.place(x=380, y=200)

        # Defining Main Page
         def main_page():
            os.system('python D:\\Anurag-PC\\OneDrive\\Desktop\\Inventory-Management\\main.py')
            root.destroy()

        #button to add to the database
         self.btn_add=Button(master,text='Add to Database',width=22,height=2,bg='steelblue',fg='white',command=self.get_items)
         self.btn_add.place(x=550,y=270)

         self.btn_clear=Button(master,text="Clear All Fields",width=22,height=2,bg='red',fg='white',command=self.clear_all)
         self.btn_clear.place(x=370,y=270)

         self.new_btn = Button(master, text="Back to Main", width=48, height=2,fg='black',bg='lavender', command=main_page)
         self.new_btn.place(x=370, y=340)

        #text box for the log
         self.tbBox=Text(master,width=60,height=18)
         self.tbBox.place(x=750,y=100)
         self.tbBox.insert(END,"ID has reached up to:"+str(id))

         self.master.bind('<Return>', self.get_items)
         self.master.bind('<Up>', self.clear_all)

    def get_items(self, *args, **kwargs):
    # get from entries
       self.name = self.name_e.get()
       self.stock = self.stock_e.get()
       self.cp = self.cp_e.get()

    # dynamic entries
       if self.name == '' or self.stock == '' or self.cp == '':
        tkinter.messagebox.showinfo("Error", "Please Fill all the entries.")
       else:
        mycursor.execute("INSERT INTO inventory (name, stock, price) VALUES(%s,%s,%s)",[self.name,self.stock,self.cp])
        conn.commit()
        # textbox insert
        self.tbBox.insert(END, "\n\nAdded " + str(self.name) + " in the database with the quantity of " + str(self.stock))
        tkinter.messagebox.showinfo("Success", "Successfully added the data")


    def clear_all(self, *args, **kwargs):
       num = id + 1
       self.name_e.delete(0, END)
       self.stock_e.delete(0, END)
       self.cp_e.delete(0, END)

root=Tk()
b=Database(root)
root.geometry("1366x785+0+0")
root.title("Add in the database")
root.mainloop()