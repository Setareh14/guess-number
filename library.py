from tkinter import *
from tkinter import ttk
from tkinter import messagebox
# import database

#======================
win = Tk()
win.geometry('550x450')
win.title("مدیریت کتابخانه")
# db1= database.Database('c:/class/mydata.db')
#============

def watch_all():
   records= db1.select()
   for rec in records:
      lst_box.insert(END,rec)
      
def insert():
   name=ent_name.get()
   lname=ent_lname.get()
   password=ent_password.get()
   term=ent_term.get()
   lst_box.insert(name,lname,password,term)
   db1.insert(name,lname,password,term)
   
def select_item(event):
   global data
   clear()
   index=lst_box.curselection()
   data=lst_box.get(index)
   ent_name.insert(END,data[1])
   ent_lname.insert(END,data[2])
   ent_password.insert(END,data[3])
   ent_term.insert(END,data[4])
   
def clear():
   ent_name.delete(0,END)
   ent_lname.delete(0,END)
   ent_password.delete(0,END)
   ent_term.delete(0,END)
   
def delete():
   global data
   result=messagebox.askquestion("Attention","are you sure to delete")
   if result=="yes":
       lst_box.delete(END,data[0])
       
def openpassword():
   openpassword=ent_openpassword.get()
   if openpassword=="admin":
     win2=Tk()
     win2.geometry("200x200")
     lbl_welcom=Label(win2,text="خوش امدید",font="arial").place(x=20,y=100)

def exit():
   win.destroy()

#============== view

lbl_name=Label(win,text=":نام",font="Calibri 15").place(x=510,y=10)
ent_name=Entry(win,font="Calibri 15")
ent_name.place(x=310,y=15)

lbl_lname=Label(win,text=":نام خانوادگی",font="Calibri 15").place(x=210,y=10)
ent_lname=Entry(win,font="Calibri 15")
ent_lname.place(x=10,y=15)

lbl_password=Label(win,text=":رمز ورود",font="Calibri 15").place(x=480,y=70)
ent_password=Entry(win,font="Calibri 15")
ent_password.place(x=280,y=75)

lbl_term=Label(win,text=":نام دوره",font="Calibri 15").place(x=210,y=70)
ent_term=Entry(win,font="Calibri 15")
ent_term.place(x=10,y=75)


lst_box=Listbox(win,height=12,width=40)
lst_box.place(x=10,y=140)

sc_rol=Scrollbar(win)
sc_rol.place(x=260,y=190)


btn_watch=Button(win,text="مشاهده همه",font="arial",width=10,command=watch_all)
btn_watch.place(x=300,y=120)

btn_insert=Button(win,text="اضافه کردن",font="arial",width=10,command=insert)
btn_insert.place(x=300,y=170)

btn_clear=Button(win,text="خالی کردن ورودیها",font="arial",width=10,command=clear)
btn_clear.place(x=300,y=220)

btn_delete=Button(win,text="حذف کردن",font="arial",width=10,command=delete)
btn_delete.place(x=300,y=270)

btn_exit=Button(win,text="خروج",font="arial",width=10,command=exit)
btn_exit.place(x=300,y=320)

btn_openpassword=Button(win,text="ورود به سامانه",font="arial",width=10,command=openpassword)
btn_openpassword.place(x=300,y=370)

ent_openpassword=Entry(win,text="",font="arial")
ent_openpassword.place(x=20,y=400)

lbl_openpassword=Label(win,text="رمز ورود",font="arial")
lbl_openpassword.place(x=200,y=400)

lst_box.bind('<<ListboxSelect>>', select_item)

win.mainloop()