#import all the modules
from tkinter import *
from tkinter import messagebox
import os
import mysql.connector
from mysql.connector import Error
import tkinter.messagebox
import datetime
import math
import subprocess

date=datetime.datetime.now().date()
#temporary list like sessions
products_list=[]
product_price=[]
product_quantity=[]
product_id=[]
r = []

class Application():
    
    def __init__(self,master,*args,**kwargs):
        self.master=master

        self.left=Frame(master,width=700,height=768, bg='alice blue')
        self.left.pack(side=LEFT)

        self.right = Frame(master, width=666, height=768, bg='lightblue' )
        self.right.pack(side=RIGHT)

        # Add_to_db function
        def database_page():
          os.system('python D:\\Anurag-PC\\OneDrive\\Desktop\\Inventory-Management\\add_to_db.py')
          root.destroy()

        # Update the Database function
        def update_page():
          os.system('python D:\\Anurag-PC\\OneDrive\\Desktop\\Inventory-Management\\update.py')
          root.destroy()

        # Back to LoginPage function
        def logout_page():
          os.system('python D:\\Anurag-PC\\OneDrive\\Desktop\\Inventory-Management\\login.py')
          root.destroy()


        #components
        self.heading=Label(self.left,text="Inventory Management System",font=('arial 30 bold'),bg='alice blue',fg='black')
        self.heading.place(x=45,y=0)

        self.date_l=Label(self.right,text="Today's Date : "+str(date),font=('arial 16 bold'),bg='lightblue',fg='black')
        self.date_l.place(x=0,y=10)

        #table invoice=======================================================
        self.tproduct=Label(self.right,text="Product Name",font=('arial 18 bold'),bg='lightblue',fg='black')
        self.tproduct.place(x=5,y=70)

        self.tquantity = Label(self.right, text="Quantity", font=('arial 18 bold'),bg='lightblue', fg='black')
        self.tquantity.place(x=300, y=70)

        self.tamount = Label(self.right, text="Amount", font=('arial 18 bold'),bg='lightblue', fg='black')
        self.tamount.place(x=500, y=70)

        #enter stuff
        self.enterid=Label(self.left,text="Enter Product ID",font=('arial 18 bold'),bg='alice blue',fg='black')
        self.enterid.place(x=0,y=100)


        self.enteride=Entry(self.left,width=25,font=('arial 18 bold'))
        self.enteride.place(x=200,y=100)
        self.enteride.focus()

        #button
        self.search_btn=Button(self.left,text="Search",width=22,height=2,bg='lavender',command=self.ajax)
        self.search_btn.place(x=360,y=140)

        self.new_btn = Button(self.left, text="Register New Products", width=22, height=2,fg='black',bg='lavender',command=database_page)
        self.new_btn.place(x=60, y=710)

        self.new_btn = Button(self.left, text="Update the Database", width=22, height=2,fg='black',bg='lavender',command=update_page)
        self.new_btn.place(x=270, y=710)

        self.new_btn = Button(self.left, text="Logout the System", width=22, height=2,fg='black',bg='lavender',command=logout_page)
        self.new_btn.place(x=480, y=710)

        #fill it later by the fuction ajax

        self.productname=Label(self.left,text="",font=('arial 21 bold '),bg='alice blue',fg='grey32')
        self.productname.place(x=170,y=210)

        self.pprice = Label(self.left, text="", font=('arial 21 bold '),bg='alice blue', fg='grey32')
        self.pprice.place(x=170, y=240)

        #total label
        self.total_l=Label(self.right,text="",font=('arial 30 bold'),bg='lightblue')
        self.total_l.place(x=0,y=600)
    def ajax(self,*args,**kwargs):
        self.conn = mysql.connector.connect(host='localhost',
                                       database='inventory_system',
                                       user='root',
                                       password='')
        self.get_id=self.enteride.get()


        #get the product info with that id and fill i the labels above
        self.mycursor = self.conn.cursor()
        self.mycursor.execute("SELECT * FROM inventory WHERE id= %s",[self.get_id])
        self.pc = self.mycursor.fetchall()
        if self.pc:
          for self.r in self.pc:
            self.get_id=self.r[0]
            self.get_name=self.r[1]
            self.get_price=self.r[3]
            self.get_stock=self.r[2]
          self.productname.configure(text="Product Name: " +str(self.get_name),fg='lightblue')
          self.pprice.configure(text="Price : ₹ "+str(self.get_price),fg='lightblue')


        #create the quantity and the discount label
          self.quantityl=Label(self.left,text="Enter Quantity",font=('arial 18 bold'),bg='alice blue',fg='black')
          self.quantityl.place(x=0,y=320)

          self.quantity_e=Entry(self.left,width=25,font=('arial 18 bold'))
          self.quantity_e.place(x=190,y=320)
          self.quantity_e.focus()

        #discount
          self.discount_l = Label(self.left, text="Enter Discount", font=('arial 18 bold'),bg='alice blue',fg='black')
          self.discount_l.place(x=0, y=360)


          self.discount_e = Entry(self.left, width=25, font=('arial 18 bold'))
          self.discount_e.place(x=190, y=360)
          self.discount_e.insert(END,0)


        #add to cart button
          self.add_to_cart_btn = Button(self.left, text="Add to Cart", width=22, height=2,bg='lavender',command=self.add_to_cart)
          self.add_to_cart_btn.place(x=350, y=400)

        #generate bill and change
          self.change_l=Label(self.left,text="Cash Received ",font=('arial 18 bold'),bg='alice blue',fg='black')
          self.change_l.place(x=0,y=550)

          self.change_e=Entry(self.left,width=25,font=('arial 18 bold'))
          self.change_e.place(x=190,y=550)

          self.change_btn= Button(self.left, text="Calculate Change", width=22, height=2,bg='lavender', command=self.change_func)
          self.change_btn.place(x=350, y=590)

          def onClick():
            tkinter.messagebox.showinfo("success", "Generated the Bill")

          #Message Button
          self.msg_btn = Button(self.left, text="Print the Bill", width=96, height=2,fg='black',bg='lavender',command=onClick)
          self.msg_btn.place(x=10, y=650)


          # Add_to_db function

          def database_page():
            os.system('python D:\\Anurag-PC\\OneDrive\\Desktop\\Inventory-Management\\add_to_db.py')
            root.destroy()

          self.new_btn = Button(self.left, text="Register New Products", width=22, height=2,fg='black',bg='lavender',command=database_page)
          self.new_btn.place(x=60, y=710)


          # Update the Database function

          def update_page():
            os.system('python D:\\Anurag-PC\\OneDrive\\Desktop\\Inventory-Management\\update.py')
            root.destroy()

          self.new_btn = Button(self.left, text="Update the Database", width=22, height=2,fg='black',bg='lavender',command=update_page)
          self.new_btn.place(x=270, y=710)


          # Back to LoginPage function

          def logout_page():
            os.system('python D:\\Anurag-PC\\OneDrive\\Desktop\\Inventory-Management\\login.py')
            root.destroy()

          self.new_btn = Button(self.left, text="Logout the System", width=22, height=2,fg='black',bg='lavender',command=logout_page)
          self.new_btn.place(x=480, y=710)

        #generate bill button
          self.bill_btn = Button(self.left, text="Enter in the database", width=22, height=2,fg='black',bg='lavender',command=self.generate_bill)
          self.bill_btn.place(x=350, y=450)
        else:
             messagebox.showinfo("success", "Generated the Bill Successfully")

             
    def add_to_cart(self,*args,**kwargs):
        self.quantity_value=int(self.quantity_e.get())

        if  self .quantity_value >int(self.get_stock):
            tkinter.messagebox.showinfo("Error","We do not have enought products in our stock.")
        else:
            #calculate the price first
            self.final_price=(float(self.quantity_value) * float(self.get_price))-(float(self.discount_e.get()))
            products_list.append(self.get_name)
            product_price.append(self.final_price)
            product_quantity.append(self.quantity_value)
            product_id.append(self.get_id)

            self.x_index=0
            self.y_index=100
            self.counter=0
            for self.p in products_list:
                self.tempname=Label(self.right,text=str(products_list[self.counter]),font=('arial 18 '),bg='lightblue',fg='black')
                self.tempname.place(x=40,y=self.y_index)
                self.tempqt = Label(self.right, text=str(product_quantity[self.counter]), font=('arial 18 '),bg='lightblue', fg='black')
                self.tempqt.place(x=350, y=self.y_index)
                self.tempprice = Label(self.right, text=str(product_price[self.counter]), font=('arial 18 '),bg='lightblue',  fg='black')
                self.tempprice.place(x=520, y=self.y_index)

                self.y_index+=40
                self.counter+=1


                #total confugure
                self.total_l.configure(text="Total Amount is ₹ "+str(sum(product_price)),bg='lightblue', fg='black')
                self.total_l.place(x=110,)

                #delete
                '''self.quantity_e.place_forget()
                self.discount_l.place_forget()
                self.discount_e.place_forget()
                self.productname.configure(text="")
                self.pprice.configure(text="")
                self.quantityl.destroy()
                self.add_to_cart_btn.destroy()
                #autofocus to the enter id
                self.enteride.focus()
                self.quantityl.focus()
                self.enteride.delete(0,END)'''

    def change_func(self,*args,**kwargs):
        self.amount_given=float(self.change_e.get())
        self.our_total=float(sum(product_price))

        self.to_give=self.amount_given-self.our_total

        #label change
        self.c_amount=Label(self.left,text="Amount to be returned : ₹ "+str(self.to_give),font=('arial 12 bold'),bg='alice blue',fg='red')
        self.c_amount.place(x=0 ,y=610)

    def generate_bill(self,*args,**kwargs):
        self.mycursor.execute("SELECT * FROM inventory WHERE id=%s",[self.get_id])
        self.pc = self.mycursor.fetchall()
        for r in self.pc:
            self.old_stock=r[2]
        for i in products_list:
            for r in self.pc:
                self.old_stock = r[2]
            self.new_stock=int(self.old_stock) - int(self.quantity_value)
            
            #updating the stock
            self.mycursor.execute("UPDATE inventory SET stock=%s WHERE id=%s",[self.new_stock,self.get_id])
            self.conn.commit()

            #insert into transaction
        self.mycursor.execute("INSERT INTO transaction (product_name,quantity,amount,date) VALUES(%s,%s,%s,%s)",[self.get_name,self.quantity_value,self.get_price,date])
        self.conn.commit()
        print("Decreased")

        
        #tkinter.messagebox.showinfo("success","Done everything smoothly")


root=Tk()
Application(root)
root.geometry("1366x785+0+0")
root.title("Inventory Management System by Group no 8")
root.mainloop()