from tkinter import*
from tkinter import messagebox

def maliat() :
    salary = ent_h.get()
    if salary.isdigit():
        text = int(salary) * 0.1
        messagebox.showinfo('مالیات', f"مالیات از حقوق دریافتی : {text} تومان")
    else:
        messagebox.showwarning("!خطا"," مقدار صحیح وارد کنید ")
        

win = Tk()
win.geometry('450x200')
win.title('<< فرم اطلاعات  >>')

lbl_n = Label(win,text=":نام" , font='Badr 15').place(x=400,y=10)
ent_n = Entry(win)
ent_n.place(x=220,y=15)

lbl_ln = Label(win,text=':نام خانوادگی ', font='Badr 15').place(x=340,y=40)
ent_ln = Entry(win)
ent_ln.place(x=220,y=50)

lbl_c = Label(win,text=':کد پرسنلی', font='Badr 15').place(x=130,y=5)
ent_c = Entry(win)
ent_c.place(x=5,y=15)

lbl_h = Label(win,text=':حقوق', font='Badr 15').place(x=160,y=40)
ent_h = Entry(win)
ent_h.place(x=6,y=50)

btn_ = Button(win,text='مالیات',command=maliat).place(x=180,y=120,width=100)

win.mainloop()