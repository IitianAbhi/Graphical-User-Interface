from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
#import openpyxl
import math
root=Tk()
h1=1100
w1=600

root.geometry(f"{h1}x{w1}")
#root.maxsize(h1,w1)
#root.minsize(h1,w1)
root.title("GUI Abhisek Sharma")
#command
def click():
    statusvar.set("Working")
    sbar.update()
    import time
    time.sleep(2)
    statusvar.set("Ready Now")
    global I1val,I2val,I3val,I4val,o1val,o2val
    a=int(I1val.get())
    b=int(I2val.get())
    c=int(I3val.get())
    d=int(I4val.get())
    o1val.set(a+3*b)
    o2val.set(c+8*d)
    
     # plt.plot(x, y)
     #print(o1val,o2val)



    # the figure that will contain the plot
    fig = Figure(figsize = (5, 5),
                 dpi = 50)
  
    # list of squares
    
    y = [math.sin(math.radians(a*i*i*i+b*i*i+c*i+d)) for i in range(-10,10)]
    for i in range(-10,10):
     with open("record.txt","a") as f:
        f.write(f"{I1val.get(), I2val.get(), I3val.get(), I4val.get(),y[i]}\n")
    
    # adding the subplot
    plot1 = fig.add_subplot(111)
  
    # plotting the graph
    plot1.plot(y)
  
    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig,
                               master = root)  
    canvas.draw()
  
    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().grid(row=5,column=4)
    toolbar = NavigationToolbar2Tk(canvas,
                                  root)
    toolbar.update()
  
    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().grid(row=5,column=4)

    pass
#background
#root.config(bg="grey")
#status bar
statusvar=StringVar()
statusvar.set("          ")

sbar=Label(root,textvariable=statusvar,relief=SUNKEN,anchor=W)
sbar.grid(row=8,column=2)
#Frame formation
F1=Frame(root,borderwidth=10,relief=GROOVE)
F1.grid(row=0,column=3)
head=Label(F1,text="Graph Equation Calculator",font="lucida 20 bold")
head.pack(fill=X)

#Text input
input1=Label(text="Input 1=", font="comicstan 14 bold",padx=20,pady=15).grid(row=1,column=1)
input2=Label(text="Input 2=", font="comicstan 14 bold",padx=20,pady=15).grid(row=2,column=1)
input3=Label(text="Input 3=", font="comicstan 14 bold",padx=20,pady=15).grid(row=3,column=1)
input4=Label(text="Input 4=", font="comicstan 14 bold",padx=20,pady=15).grid(row=4,column=1)

#rectangle formation
fig = Figure(figsize = (5, 5),
                 dpi = 50)
y1=[0 for i in range (-101,101)]
plot2 = fig.add_subplot(111)
plot2.plot(y1)                 
canvas = FigureCanvasTkAgg(fig,
                               master = root)  
canvas.draw()
  
    # placing the canvas on the Tkinter window
canvas.get_tk_widget().grid(row=5,column=4)

#Entry Widget
#entry var=stringvar
I1val=StringVar()
I2val=StringVar()
I3val=StringVar()
I4val=StringVar()

#creating a entry widget
I1entry=Entry(root,textvariable=I1val,font="lucida 14 bold").grid(row=1, column=2)
I2entry=Entry(root,textvariable=I2val,font="lucida 14 bold").grid(row=2, column=2)
I3entry=Entry(root,textvariable=I3val,font="lucida 14 bold").grid(row=3, column=2)
I4entry=Entry(root,textvariable=I4val,font="lucida 14 bold").grid(row=4, column=2)

#Button to Apply
b1=Button(root, text="Submit",fg="blue",font="lucida 14 bold",command=click).grid(row=5, column=2)
#Button to quit
b2=Button(root,text="Exit",font="lucida 10 bold",bg="red",command=quit).grid(row=8,column=6)
#Output File
output1=Label(text="Output 1=", font="comicstan 14 bold",padx=25,pady=15).grid(row=1,column=3)
output2=Label(text="Output 2=", font="comicstan 14 bold",padx=25,pady=15).grid(row=2,column=3)

#Output value
o1val=IntVar()
o2val=IntVar()

o1entry=Entry(root,textvariable=o1val,font="lucida 14 bold").grid(row=1, column=4)
o2entry=Entry(root,textvariable=o2val,font="lucida 14 bold").grid(row=2, column=4)

#Equation part
Equation=Label(text="Equation:", font="comicstan 14 bold",padx=20,pady=15).grid(row=3,column=3)
Equation=Label(text="y=sin(ax3+bx2+cx+d)", font="comicstan 14 italic",pady=15).grid(row=3,column=4)


root.mainloop()