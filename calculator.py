from tkinter import *
window = Tk()
window.title("calculator")
window.geometry("370x400")
window.resizable(False,False)
#===================defination here======================        
def clear():
    e1.delete(0,END)
    e2.delete(0,END)
def equal():
    e2.delete(0,END)
    x = e1.get()
    x = x.replace("x","*")
    result = eval(x)
    e2.insert(END,result)
def can_cel():
    x = e1.get()
    length = len(x)
    length-=1
    text = x[0:length]
    e1.delete(0,END)
    e1.insert(END,text)
    e2.delete(0,END)
    result = eval(text)
    e2.insert(END,result)
#=========create frame==================================
f_rame = Frame(window,bg="orange")
f_rame.pack(fill="both",expand=True)
#===================entry box=============================
e1 = Entry(f_rame,justify=CENTER,font=("arial,20"))
e1.place(x=50,y=20,height=40,width=250)
e2 = Entry(f_rame,justify=CENTER,font=("arial,20"))
e2.place(x=50,y=60,height=40,width=250)
#===================button here================================
C = Button(f_rame,text="C",font=("arial,20"),bg="red",fg="blue",command=clear)
C.place(x=10,y=120,width=80,height=40)
per = Button(f_rame,text="Mod",font=("arial,20"),bg="black",fg="white",command=lambda:e1.insert(END,"%"))
per.place(x=100,y=120,width=80,height=40)
cancel = Button(f_rame,text="x",font=("arial,20"),bg="black",fg="red",command=can_cel)
cancel.place(x=190,y=120,width=80,height=40)
div = Button(f_rame,text="/",font=("arial,20"),bg="black",fg="white",command=lambda:e1.insert(END,"/"))
div.place(x=280,y=120,width=80,height=40)
#=================second line button here=============================
b7 = Button(f_rame,text="7",font=("arial,20"),bg="black",fg="white",command=lambda:[e1.insert(END,"7"),equal()])
b7.place(x=10,y=170,width=80,height=40)
b8 = Button(f_rame,text="8",font=("arial,20"),bg="black",fg="white",command=lambda:[e1.insert(END,"8"),equal()])
b8.place(x=100,y=170,width=80,height=40)
b9 = Button(f_rame,text="9",font=("arial,20"),bg="black",fg="white",command=lambda:[e1.insert(END,"9"),equal()])
b9.place(x=190,y=170,width=80,height=40)
mul = Button(f_rame,text="X",font=("arial,20"),bg="black",fg="white",command=lambda:[e1.insert(END,"x"),mani()])
mul.place(x=280,y=170,width=80,height=40)
b4 = Button(f_rame,text="4",font=("arial,20"),bg="black",fg="white",command=lambda:[e1.insert(END,"4"),equal()])
b4.place(x=10,y=220,width=80,height=40)
b5 = Button(f_rame,text="5",font=("arial,20"),bg="black",fg="white",command=lambda:[e1.insert(END,"5"),equal()])
b5.place(x=100,y=220,width=80,height=40)
b6 = Button(f_rame,text="6",font=("arial,20"),bg="black",fg="white",command=lambda:[e1.insert(END,"6"),equal()])
b6.place(x=190,y=220,width=80,height=40)
plus = Button(f_rame,text="+",font=("arial,20"),bg="black",fg="white",command=lambda:e1.insert(END,"+"))
plus.place(x=280,y=220,width=80,height=40)
b1 = Button(f_rame,text="1",font=("arial,20"),bg="black",fg="white",command=lambda:[e1.insert(END,"1"),equal()])
b1.place(x=10,y=270,width=80,height=40)
b2 = Button(f_rame,text="2",font=("arial,20"),bg="black",fg="white",command=lambda:[e1.insert(END,"2"),equal()])
b2.place(x=100,y=270,width=80,height=40)
b3 = Button(f_rame,text="3",font=("arial,20"),bg="black",fg="white",command=lambda:[e1.insert(END,"3"),equal()])
b3.place(x=190,y=270,width=80,height=40)
minus = Button(f_rame,text="-",font=("arial,20"),bg="black",fg="white",command=lambda:[e1.insert(END,"-"),mani()])
minus.place(x=280,y=270,width=80,height=40)
#===============last button add==========================================
b0 = Button(f_rame,text="0",font=("arial,20"),bg="black",fg="white",command=lambda:[e1.insert(END,"0"),equal()])
b0.place(x=10,y=320,width=80,height=40)
b00 = Button(f_rame,text="00",font=("arial,20"),bg="black",fg="white",command=lambda:[e1.insert(END,"00"),equal()])
b00.place(x=100,y=320,width=80,height=40)
dec = Button(f_rame,text=".",font=("arial,20"),bg="black",fg="white",command=lambda:e1.insert(END,"."))
dec.place(x=190,y=320,width=80,height=40)
eq = Button(f_rame,text="=",font=("arial,20"),bg="black",fg="white",command=equal)
eq.place(x=280,y=320,width=80,height=40)










#==================this is my endloop===========================
window.mainloop()
