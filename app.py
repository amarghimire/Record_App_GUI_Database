from os import remove
from tkinter import *
from tkinter import messagebox
from db import Database
from cv2 import add



#part=item
#create the window project

app=Tk()
app.title('Business Record')
app.geometry('1200x680')


#window Title
title = Label(app, text = '  Ghimire Fruit and Vegetable Center  ',font=('bold',25), anchor = CENTER, justify = CENTER)
title.grid(row = 0, columnspan = 20, sticky = N+S+E+W)


#Retailer
user=StringVar()
user_lb=Label(app,text='     User_Name     ',font=('bold',14))
user_lb.grid(row=1, column=0)

user_entry=Entry(app, textvariable=user)
user_entry.grid(row=2,column=0)


#write together
# together_text=StringVar()
# together_label=Label(app,text='       Together_Name      ',font=('bold',14),pady=20)
# together_label.grid(row=1,column=1)

# together_entry=Entry(app,textvariable=user)
# together_entry.grid(row=2,column=1)

#customer_ID
customer_ID=StringVar()
customer_lb=Label(app,text='Customer ID',font=('bold',14))
customer_lb.grid(row=1,column=1,sticky=W)

cusID_entry=Entry(app,textvariable=customer_ID)
cusID_entry.grid(row=2,column=1)

#Customer 
customer=StringVar()
customer_lb=Label(app,text='         Customer Name',font=('bold',14))
customer_lb.grid(row=1,column=2,sticky=W)

cus_entry=Entry(app,textvariable=customer)
cus_entry.grid(row=2,column=2)

#item 
item=StringVar()
item_lb=Label(app,text='    item Name  ',font=('bold',14),pady=20)
item_lb.grid(row=3,column=0)
item_entry=Entry(app,textvariable=item)
item_entry.grid(row=4,column=0)

#price
price=StringVar()
price_lb=Label(app,text='     item     price      ',font=('bold',14),pady=20)
price_lb.grid(row=3,column=1)

price_entry=Entry(app,textvariable=price)
price_entry.grid(row=4,column=1)
#Quantitiy
quantity=IntVar()
quantity_lb=Label(app,text='   Quantity      ',font=('bold',14),pady=20)
quantity_lb.grid(row=3,column=2)

quantity_entry=Entry(app,textvariable=quantity)
quantity_entry.grid(row=4,column=2)
############ button function #####

db= Database('store.db')

def populate_list():
    items_list.delete(0,END) #dont allow to repeat the data even if you call this function more than 1 time
    for any_r in db.fetching_data():
        items_list.insert(END, any_r)
def add_item():
    if user.get()=='' or customer.get()=='' or item.get()=='' or price.get()=='':
        messagebox.showerror('Required to fullfill all Details')
    else:
        db.insert(user.get(),customer.get(),item.get(),price.get())
        items_list.delete(0,END)
        items_list.insert(END,(user.get(),customer.get(),item.get(),price.get()))
        clear_entry()
        populate_list()

def select_item(event):
    #run each time when you select it on canvas
    try:
        global selected_item
        index = items_list.curselection()[0]
        selected_item=items_list.get(index)
        print(type(selected_item))

        user_entry.delete(0,END)
        user_entry.insert(END,selected_item[1])

        cus_entry.delete(0,END)
        cus_entry.insert(END,selected_item[2])

        item_entry.delete(0,END)
        item_entry.insert(END,selected_item[3])

        price_entry.delete(0,END)
        price_entry.insert(END,selected_item[4])
        print('hello')

    except IndexError:
        pass

def remove_item():
    db.remove(selected_item[0])
    clear_entry()
    populate_list()
    print('remove')
def update_item():
    db.update(selected_item[0],user.get(),customer.get(),item.get(),price.get())
    populate_list()
    print('update')
def clear_entry():
    item_entry.delete(0,END)
    cus_entry.delete(0,END)
    price_entry.delete(0,END)
    user_entry.delete(0,END)
    print('clear')

################button##########

#Buttons
add_btn=Button(app,text='Add items',width=12,command=add_item)
add_btn.grid(row=5,column=1,pady=20)

update_btn=Button(app,text='Update items',width=12,command=update_item)
update_btn.grid(row=13,column=0,pady=20)

remove_btn=Button(app,text='Remove items',width=12,command=remove_item)
remove_btn.grid(row=12,column=0,pady=20)

clear_btn=Button(app,text=' Clear Input',width=12,command=clear_entry)
clear_btn.grid(row=5,column=2,pady=20)


# items list Box
items_list=Listbox(app,height=20,width=70,border=1)
items_list.grid(row=6,column=0,columnspan=10,rowspan=10,pady=20,padx=200)

#scrollbar
scrollbar=Scrollbar(app)
scrollbar.grid(row=12,column=6,pady=20)

#Bind Select
items_list.bind('<<ListboxSelect>>',select_item)

#set scroll to listbox
items_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=items_list.yview)

#populate_data
populate_list()

#start program
app.mainloop()
