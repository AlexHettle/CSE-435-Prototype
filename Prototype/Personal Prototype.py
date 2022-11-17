from tkinter import *

Distance_Selection=1
Speed_Selection=70


def Distance_Increase():
    global Distance_Selection
    if(Distance_Selection<3):
        Distance_Selection+=1
        Distance_Label.configure(text="Current Distance: "+str(Distance_Selection)+" car length")
        
def Distance_Decrease():
    global Distance_Selection
    if(Distance_Selection>1):
        Distance_Selection-=1
        Distance_Label.configure(text="Current Distance: "+str(Distance_Selection)+" car length")

def Speed_Increase():
    global Speed_Selection
    if(Speed_Selection<80):
        Speed_Selection+=1
        Speed_Label.configure(text="Current Speed: "+str(Speed_Selection))
def Speed_Decrease():
    global Speed_Selection
    if(Speed_Selection>70):
        Speed_Selection-=1
        Speed_Label.configure(text="Current Speed: "+str(Speed_Selection))
        
def Deactivate():
    Active_Label.configure(text="Current State: INACTIVE")
    
def Activate():
    Active_Label.configure(text="Current State: ACTIVE")

window=Tk()
window.title("Prototype")
window.geometry("800x500")
window.resizable(False, False)
the_canvas=Canvas(window,width=800,height=500, highlightthickness=0,bg="#BBF4F7")
the_canvas.place(x=0,y=0)
the_canvas.create_rectangle(-1,250,801,501,fill="black")
the_canvas.create_rectangle(450,275,801,470,outline = "grey",width=4,fill="#9098a6")
the_canvas.create_oval(70, 70,410 ,410,outline = "black", fill = "grey", width = 2)
the_canvas.create_oval(130, 130, 350, 350,outline = "black", fill = "#BBF4F7", width = 2)
the_canvas.create_arc(130, 120, 350, 350, start=180, extent=180, fill="grey")
the_canvas.create_arc(130, 140, 350, 350, start=180, extent=180, fill="black")

the_canvas.create_oval(170, 170,310 ,310, fill = "grey")




Button1 = PhotoImage(file = "ButtonOn.png")
img1 = Button(window, image = Button1,borderwidth = 0,bg="grey",fg="grey",activebackground="grey",command=Activate)
img1.place(x=350,y=250)

Button2 = PhotoImage(file = "ButtonOff.png")
img2 = Button(window, image = Button2,borderwidth = 0,bg="grey",fg="grey",activebackground="grey",command=Deactivate)
img2.place(x=377,y=250)

Button3 = PhotoImage(file = "ButtonStop.png")
img3 = Button(window, image = Button3,borderwidth = 0,bg="grey",fg="grey",activebackground="grey",command=Deactivate)
img3.place(x=345,y=275)

Button4 = PhotoImage(file = "ButtonResume.png")
img4 = Button(window, image = Button4,borderwidth = 0,bg="grey",fg="grey",activebackground="grey",command=Activate)
img4.place(x=370,y=275)

Button5 = PhotoImage(file = "ButtonCancel.png")
img5 = Button(window, image = Button5,borderwidth = 0,bg="grey",fg="grey",activebackground="grey",command=Deactivate)
img5.place(x=336,y=300)

Button6 = PhotoImage(file = "ButtonDistanceIncrease.png")
img6 = Button(window, image = Button6,borderwidth = 0,bg="black",fg="black",activebackground="black",command=Distance_Increase)
img6.place(x=390,y=350)

Button7 = PhotoImage(file = "ButtonSpeedIncrease.png")
img7 = Button(window, image = Button7,borderwidth = 0,bg="black",fg="black",activebackground="black",command=Speed_Increase)
img7.place(x=420,y=350)

Button8 = PhotoImage(file = "ButtonDistanceDecrease.png")
img8 = Button(window, image = Button8,borderwidth = 0,bg="black",fg="black",activebackground="black",command=Distance_Decrease)
img8.place(x=390,y=380)

Button9 = PhotoImage(file = "ButtonSpeedDecrease.png")
img9 = Button(window, image = Button9,borderwidth = 0,bg="black",fg="black",activebackground="black",command=Speed_Decrease)
img9.place(x=420,y=380)

Active_Label = Label(window,text = "Current State: ACTIVE",bg="#9098a6",font=("Times New Roman", 15))
Active_Label.place(x = 460,y = 285) 
Distance_Label = Label(window,text = "Current Distance: 1 car length",bg="#9098a6",font=("Times New Roman", 15))
Distance_Label.place(x = 460,y = 305) 
Speed_Label = Label(window,text = "Current Speed: 70",bg="#9098a6",font=("Times New Roman", 15))
Speed_Label.place(x = 460,y = 325) 


window.mainloop()