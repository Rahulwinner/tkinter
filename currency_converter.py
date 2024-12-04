from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("currency_changer...")
window.state("zoomed")
window.resizable(False,False)
#***************this is my function*****************************************************
def my_function(value):
    try:
        x = user_entry.get()
        inr = float(x)
        oc = float(value)
        result = float(inr * oc)
        val.config(text=result)
    except:
        messagebox.showinfo("Alert", "Please Input Valid Data")
    
    
    
#============i am creating header section ==============================================
heading = Label(window,text="Currency Converter in INR (2024)",bg="brown",font=("arial",25),fg="white")
heading.pack(fill=X,ipady=15)
#===========i am creating bottom section ===============================================
bottom = Label(window,text="Doveloped by Rahul winner",bg="blue",font=("arial",20),fg="white")
bottom.pack(side=BOTTOM,fill=X)
#=========== i am creating left side vertically frame ====================================
l_frame = Frame(window,bg="black")
l_frame.place(x=0,y=76,width=330,height=630)

#============ i am creating right side horizontal frame=====================================
r_frame = Frame(window,bg="black")
r_frame.place(x=1063,y=76,width=330,height=630)

#=============this is left side button================================================
usa = Button(l_frame,text="America",bg="green",fg="white",font=("arial",18),justify="center",command=lambda:my_function("0.012"))
usa.place(x=10,y=10,width=290,height=50)
Afghanistan = Button(l_frame,text="Afghanistan",bg="green",fg="white",font=("arial",18),justify="center",command=lambda:my_function("0.81"))
Afghanistan.place(x=10,y=80,width=290,height=50)
Bhutan = Button(l_frame,text="Bhutan",bg="green",fg="white",font=("arial",18),justify="center",command=lambda:my_function("1.0"))
Bhutan.place(x=10,y=150,width=290,height=50)
Bangladesh = Button(l_frame,text="Bangladesh",bg="green",fg="white",font=("arial",18),justify="center",command=lambda:my_function("1.41"))
Bangladesh.place(x=10,y=220,width=290,height=50)
Sri_Lanka = Button(l_frame,text="Sri Lanka",bg="green",fg="white",font=("arial",18),justify="center",command=lambda:my_function("3.43"))
Sri_Lanka.place(x=10,y=290,width=290,height=50)
Nepal = Button(l_frame,text="Nepal",bg="green",fg="white",font=("arial",18),justify="center",command=lambda:my_function("1.60"))
Nepal.place(x=10,y=360,width=290,height=50)
Pakistan = Button(l_frame,text="Pakistan",bg="green",fg="white",font=("arial",18),justify="center",command=lambda:my_function("3.28"))
Pakistan.place(x=10,y=430,width=290,height=50)
china = Button(l_frame,text="Chine",bg="green",fg="white",font=("arial",18),justify="center",command=lambda:my_function("0.09"))
china.place(x=10,y=500,width=290,height=50)
Thailand = Button(l_frame,text="Thailand",bg="green",fg="white",font=("arial",18),justify="center",command=lambda:my_function("0.40"))
Thailand.place(x=10,y=570,width=290,height=50)

#=============================this is right side button=======================
Cambodia = Button(r_frame,text="Cambodia",bg="green",fg="white",font=("arial",18),justify="center",command=lambda:my_function("47.56"))
Cambodia.place(x=10,y=10,width=290,height=50)
Laos = Button(r_frame,text="Laos",bg="green",fg="white",font=("arial",18),justify="center",command=lambda:my_function("258.87"))
Laos.place(x=10,y=80,width=290,height=50)
Vietnam = Button(r_frame,text="Vietnam",bg="green",fg="white",font=("arial",18),justify="center",command=lambda:my_function("300"))
Vietnam.place(x=10,y=150,width=290,height=50)
Indonesia = Button(r_frame,text="Indonesia",bg="green",fg="white",font=("arial",18),justify="center",command=lambda:my_function("188.00"))
Indonesia.place(x=10,y=220,width=290,height=50)
Malaysia = Button(r_frame,text="Malaysia",bg="green",fg="white",font=("arial",18),justify="center",command=lambda:my_function("0.05"))
Malaysia.place(x=10,y=290,width=290,height=50)
Singapore = Button(r_frame,text="Singapore",bg="green",fg="white",font=("arial",18),justify="center",command=lambda:my_function("0.02"))
Singapore.place(x=10,y=360,width=290,height=50)
Philippines = Button(r_frame,text="Philippines",bg="green",fg="white",font=("arial",18),justify="center",command=lambda:my_function("0.69"))
Philippines.place(x=10,y=430,width=290,height=50)
rusia = Button(r_frame,text="Rusia",bg="green",fg="white",font=("arial",18),justify="center",command=lambda:my_function("1.24"))
rusia.place(x=10,y=500,width=290,height=50)
japan = Button(r_frame,text="Japan",bg="green",fg="white",font=("arial",18),justify="center",command=lambda:my_function("2"))
japan.place(x=10,y=570,width=290,height=50)

#==============================================================
#======i am creating frame for user inpurt=====================
user_frame = Frame(window,bg="#FFC107")
user_frame.place(x=340,y=80,width=710,height=100)
user_lab = Label(user_frame,text="Enter Your Amount in Inr",bg="#2E4053",fg="white",font=("arial",18),justify="center")
user_lab.place(x=30,y=20,width=300,height=50)
user_entry = Entry(user_frame,font=("arial",18),justify="center")
user_entry.place(x=380,y=20,width=300,height=50)
#=============result section =========================================
val = Label(window,text="",bg="#F7DC6F",fg="red",font=("arial",58),justify="center")
val.place(x=340,y=200,width=710,height=500)


#=========end mainloop========================================
window.mainloop()
