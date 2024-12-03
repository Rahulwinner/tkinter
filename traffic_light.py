from tkinter import *
import time
window = Tk()
window.title("Traffic light")
window.geometry("480x480")
window.resizable(False,False)
#=============defination is here================================================================
def change_color_red():
    canvas.itemconfig(oval1,fill="red")
    canvas.itemconfig(oval2,fill="grey")
    canvas.itemconfig(oval3,fill="grey")
    window.after(10000,change_color_yellow)
def change_color_yellow():
    canvas.itemconfig(oval2,fill="yellow")
    canvas.itemconfig(oval1,fill="grey")
    canvas.itemconfig(oval3,fill="grey")
    window.after(5000,change_color_green)
def change_color_green():
    canvas.itemconfig(oval3,fill="green")
    canvas.itemconfig(oval1,fill="grey")
    canvas.itemconfig(oval2,fill="grey")
    window.after(10000,change_color_red)    
#=============create infinite loop================================================================
#***************create canvas*************
canvas = Canvas(window,bg="black",width=150,height=350)
canvas.place(x=10,y=20)
#=============create red light============================================================
oval1 = canvas.create_oval(30,10,120,100,fill="grey")
# window.after(5000,change_color)
#=============create yellow light=========================================================
oval2 = canvas.create_oval(30,110,120,200,fill="grey")
#=============create green light==========================================================
oval3 = canvas.create_oval(30,210,120,300,fill="grey")
#=================time duration ==========================================================
change_color_red()


window.mainloop()