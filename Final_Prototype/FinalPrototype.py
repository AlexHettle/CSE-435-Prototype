
from tkinter import *

Distance_Selection=1
Speed_Selection=50
currently_parked=False
top_down_view=False

def Parked():
    global currently_parked
    global top_down_view
    currently_parked=True
    top_down_view=False
    the_canvas.create_rectangle(420,0,801,250,fill="#e8c79d")
    the_canvas.create_rectangle(440,150,500,250,fill="#d08b36")
    the_canvas.create_rectangle(540,50,600,110,fill="#1a9ae5")
    the_canvas.create_rectangle(640,50,700,110,fill="#1a9ae5")


def In_Traffic():
    global Distance_Selection
    global currently_parked
    global top_down_view
    currently_parked=False
    top_down_view=False
    the_canvas.create_rectangle(415,-10,811,250,width=0,fill="#BBF4F7")
    if(Distance_Selection==1):
            the_canvas.create_rectangle(420,110,801,250,fill="red")
            the_canvas.create_rectangle(420,220,480,250,fill="#b9330f")
            the_canvas.create_rectangle(781,220,801,250,fill="#b9330f")
            the_canvas.create_rectangle(480,120,781,200,fill="black")
    if(Distance_Selection==2):
             the_canvas.create_rectangle(420,110,801,250,fill="#BBF4F7",width=0)
             the_canvas.create_rectangle(500,130,701,250,fill="red")
             the_canvas.create_rectangle(500,230,530,250,fill="#b9330f")
             the_canvas.create_rectangle(671,230,701,250,fill="#b9330f")
             the_canvas.create_rectangle(530,140,670,190,fill="black")
 
    if(Distance_Selection==3):
             the_canvas.create_rectangle(420,110,801,250,fill="#BBF4F7",width=0)
             the_canvas.create_rectangle(550,200,631,250,fill="red")
             the_canvas.create_rectangle(551,235,561,250,fill="#b9330f")
             the_canvas.create_rectangle(560,205,621,225,fill="black")
             the_canvas.create_rectangle(621,235,631,250,fill="#b9330f")


def Top_Down_View():
    global Distance_Selection
    global currently_parked
    global top_down_view
    if(top_down_view==False):
        top_down_view=True
        the_canvas.create_rectangle(420,-1,801,250,fill="white")
        if(currently_parked==True):
            the_canvas.create_rectangle(580,185,640,245,fill="black")
            the_canvas.create_rectangle(430,-1,791,90,fill="#e8c79d")
        if(currently_parked==False):
            the_canvas.create_rectangle(580,10,640,40,fill="red")
            if(Distance_Selection==1):
                the_canvas.create_rectangle(580,100,640,160,fill="black")
            if(Distance_Selection==2):
                the_canvas.create_rectangle(580,160,640,220,fill="black")
            if(Distance_Selection==3):
                the_canvas.create_rectangle(580,220,640,260,fill="black")
    elif(top_down_view==True):
        if(currently_parked==True):
            Parked()
        if(currently_parked==False):
            In_Traffic()



        
    

def Distance_Increase():
    global currently_parked
    global Distance_Selection
    if(Distance_Selection<3):
        Distance_Selection+=1
        Distance_Label.configure(text="Current Distance: "+str(Distance_Selection)+" car length")
    if(currently_parked==False):
        if(top_down_view==False):
            if(Distance_Selection==2):
                    the_canvas.create_rectangle(420,110,801,250,fill="#BBF4F7",width=0)
                    the_canvas.create_rectangle(500,130,701,250,fill="red")
                    the_canvas.create_rectangle(500,230,530,250,fill="#b9330f")
                    the_canvas.create_rectangle(671,230,701,250,fill="#b9330f")
                    the_canvas.create_rectangle(530,140,670,190,fill="black")
        
            if(Distance_Selection==3):
                    the_canvas.create_rectangle(420,110,801,250,fill="#BBF4F7",width=0)
                    the_canvas.create_rectangle(550,200,631,250,fill="red")
                    the_canvas.create_rectangle(551,235,561,250,fill="#b9330f")
                    the_canvas.create_rectangle(560,205,621,225,fill="black")
                    the_canvas.create_rectangle(621,235,631,250,fill="#b9330f")
        if(top_down_view==True):
            the_canvas.create_rectangle(420,-1,801,250,fill="white")
            the_canvas.create_rectangle(580,10,640,40,fill="red")
            if(Distance_Selection==1):
                the_canvas.create_rectangle(580,100,640,160,fill="black")
            if(Distance_Selection==2):
                the_canvas.create_rectangle(580,160,640,220,fill="black")
            if(Distance_Selection==3):
                the_canvas.create_rectangle(580,220,640,260,fill="black")
        
        
def Distance_Decrease():
    global currently_parked
    global Distance_Selection
    if(Distance_Selection>1):
        Distance_Selection-=1
        Distance_Label.configure(text="Current Distance: "+str(Distance_Selection)+" car length")
    if(currently_parked==False):
        if(top_down_view==False):
            if(Distance_Selection==2):
                    the_canvas.create_rectangle(420,110,801,250,fill="#BBF4F7",width=0)
                    the_canvas.create_rectangle(500,130,701,250,fill="red")
                    the_canvas.create_rectangle(500,230,530,250,fill="#b9330f")
                    the_canvas.create_rectangle(671,230,701,250,fill="#b9330f")
                    the_canvas.create_rectangle(530,140,670,190,fill="black")
            if(Distance_Selection==1):
                    the_canvas.create_rectangle(420,110,801,250,fill="red")
                    the_canvas.create_rectangle(420,220,480,250,fill="#b9330f")
                    the_canvas.create_rectangle(781,220,801,250,fill="#b9330f")
                    the_canvas.create_rectangle(480,120,781,200,fill="black")
        if(top_down_view==True):
            the_canvas.create_rectangle(420,-1,801,250,fill="white")
            the_canvas.create_rectangle(580,10,640,40,fill="red")
            if(Distance_Selection==1):
                the_canvas.create_rectangle(580,100,640,160,fill="black")
            if(Distance_Selection==2):
                the_canvas.create_rectangle(580,160,640,220,fill="black")
            if(Distance_Selection==3):
                the_canvas.create_rectangle(580,220,640,260,fill="black")

def Speed_Increase():
    global Speed_Selection
    if(Speed_Selection<80):
        Speed_Selection+=5
        Speed_Label.configure(text="Max Speed: "+str(Speed_Selection))
        the_canvas.create_oval(630, 365,760 ,495,fill = "grey")
        the_canvas.create_arc(630, 365,760 ,495, start=0, extent=180,fill = "black")
        the_canvas.create_arc(630, 365,760 ,495, start=(75-Speed_Selection+50)*1.2, extent=5,fill = "red",width=0)
def Speed_Decrease():
    global Speed_Selection
    if(Speed_Selection>0):
        Speed_Selection-=5
        Speed_Label.configure(text="Max Speed: "+str(Speed_Selection))
        the_canvas.create_oval(630, 365,760 ,495,fill = "grey")
        the_canvas.create_arc(630, 365,760 ,495, start=0, extent=180,fill = "black")
        the_canvas.create_arc(630, 365,760 ,495, start=(75-Speed_Selection+50)*1.2, extent=5,fill = "red",width=0)
        
def Deactivate():
    Active_Label.configure(text="Current State: INACTIVE")

def Cancel():
    global currently_parked
    global Distance_Selection
    global Speed_Selection
    global top_down_view
    Distance_Selection=1
    Speed_Selection=50
    Active_Label.configure(text="Current State: INACTIVE")
    Speed_Label.configure(text="Max Speed: "+str(Speed_Selection))
    Distance_Label.configure(text="Current Distance: "+str(Distance_Selection)+" car length")
    the_canvas.create_oval(630, 365,760 ,495,fill = "grey")
    the_canvas.create_arc(630, 365,760 ,495, start=0, extent=180,fill = "black")
    the_canvas.create_arc(630, 365,760 ,495, start=90, extent=5,fill = "red",width=0)
    if(currently_parked==False):
        if(top_down_view==False):
            the_canvas.create_rectangle(420,110,801,250,fill="red")
            the_canvas.create_rectangle(420,220,480,250,fill="#b9330f")
            the_canvas.create_rectangle(781,220,801,250,fill="#b9330f")
            the_canvas.create_rectangle(480,120,781,200,fill="black")
        if(top_down_view==True):
            the_canvas.create_rectangle(420,-1,801,250,fill="white")
            the_canvas.create_rectangle(580,10,640,40,fill="red")
            the_canvas.create_rectangle(580,100,640,160,fill="black")
            
def Activate():
    Active_Label.configure(text="Current State: ACTIVE")
    
    
def On():
    global currently_parked
    if(currently_parked==True):
        Activate()
def Off():
    global currently_parked
    if(currently_parked==True):
        Deactivate()

window=Tk()
window.title("Prototype")
window.geometry("800x500")
window.resizable(False, False)
the_canvas=Canvas(window,width=800,height=500, highlightthickness=0,bg="#BBF4F7")
the_canvas.place(x=0,y=0)
the_canvas.create_rectangle(-1,250,801,501,fill="black")
the_canvas.create_rectangle(450,275,801,520,outline = "grey",width=4,fill="#9098a6")
the_canvas.create_oval(70, 70,410 ,410,outline = "black", fill = "grey", width = 2)
the_canvas.create_oval(130, 130, 350, 350,outline = "black", fill = "#BBF4F7", width = 2)
the_canvas.create_arc(130, 120, 350, 350, start=180, extent=180, fill="grey")
the_canvas.create_arc(130, 140, 350, 350, start=180, extent=180, fill="black")

the_canvas.create_oval(170, 170,310 ,310, fill = "grey")



the_canvas.create_oval(630, 365,760 ,495,fill = "grey")
the_canvas.create_arc(630, 365,760 ,495, start=0, extent=180,fill = "black")
the_canvas.create_arc(630, 365,760 ,495, start=90, extent=5,fill = "red",width=0)
the_canvas.create_rectangle(420,110,801,250,fill="red")
the_canvas.create_rectangle(420,220,480,250,fill="#b9330f")
the_canvas.create_rectangle(781,220,801,250,fill="#b9330f")
the_canvas.create_rectangle(480,120,781,200,fill="black")




Button1 = PhotoImage(file = "Prototype/ButtonOn.png")
img1 = Button(window, image = Button1,borderwidth = 0,bg="grey",fg="grey",activebackground="grey",command=On,bd=0,activeforeground="grey",highlightcolor="grey",highlightthickness=0)
img1.place(x=350,y=250)

Button2 = PhotoImage(file = "Prototype/ButtonOff.png")
img2 = Button(window, image = Button2,borderwidth = 0,bg="grey",fg="grey",activebackground="grey",command=Off,highlightthickness=0)
img2.place(x=373,y=250)

Button3 = PhotoImage(file = "Prototype/ButtonStop.png")
img3 = Button(window, image = Button3,borderwidth = 0,bg="grey",fg="grey",activebackground="grey",command=Deactivate,highlightthickness=0)
img3.place(x=345,y=275)

Button4 = PhotoImage(file = "Prototype/ButtonResume.png")
img4 = Button(window, image = Button4,borderwidth = 0,bg="grey",fg="grey",activebackground="grey",command=Activate,highlightthickness=0)
img4.place(x=370,y=275)

Button5 = PhotoImage(file = "Prototype/ButtonCancel.png")
img5 = Button(window, image = Button5,borderwidth = 0,bg="grey",fg="grey",activebackground="grey",command=Cancel,highlightthickness=0)
img5.place(x=336,y=300)

Button6 = PhotoImage(file = "Prototype/ButtonDistanceIncrease.png")
img6 = Button(window, image = Button6,borderwidth = 0,bg="black",fg="black",activebackground="black",command=Distance_Increase,highlightthickness=0)
img6.place(x=390,y=350)

Button7 = PhotoImage(file = "Prototype/ButtonSpeedIncrease.png")
img7 = Button(window, image = Button7,borderwidth = 0,bg="black",fg="black",activebackground="black",command=Speed_Increase,highlightthickness=0)
img7.place(x=420,y=350)

Button8 = PhotoImage(file = "Prototype/ButtonDistanceDecrease.png")
img8 = Button(window, image = Button8,borderwidth = 0,bg="black",fg="black",activebackground="black",command=Distance_Decrease,highlightthickness=0)
img8.place(x=390,y=380)

Button9 = PhotoImage(file = "Prototype/ButtonSpeedDecrease.png")
img9 = Button(window, image = Button9,borderwidth = 0,bg="black",fg="black",activebackground="black",command=Speed_Decrease,highlightthickness=0)
img9.place(x=420,y=380)

Active_Label = Label(window,text = "Current State: ACTIVE",bg="#9098a6",font=("Times New Roman", 15))
Active_Label.place(x = 460,y = 285) 
Distance_Label = Label(window,text = "Current Distance: 1 car length",bg="#9098a6",font=("Times New Roman", 15))
Distance_Label.place(x = 460,y = 315) 
Speed_Label = Label(window,text = "Max Speed: 50",bg="#9098a6",font=("Times New Roman", 15))
Speed_Label.place(x = 460,y = 345) 

Parked_Button=Button(window,text="Parked",padx=6,command=Parked)
Parked_Button.place(x=20,y=50)
In_Traffic_Button=Button(window,text="In Traffic",command=In_Traffic)
In_Traffic_Button.place(x=20,y=20)
Parked_Button=Button(window,text="Top-Down View",padx=6,command=Top_Down_View)
Parked_Button.place(x=20,y=80)


window.mainloop()