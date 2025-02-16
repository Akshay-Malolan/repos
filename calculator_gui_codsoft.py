from tkinter import *
def click(event):
    global scvalue #Setting Global Variable of scvalue
    text=event.widget.cget('text')
    print(text)
    if text=='=':
        if scvalue.get().isdigit():#Check if the inputs are digits
            value=int(scvalue.get())
        else:
            try:
                value=eval(screen.get())
            except Exception as e:#Exception Handling
                print(e)
                scvalue.set('Error')
                screen.update()
        scvalue.set(value)#Setting Calculated Value
        screen.update()#Updating Frame for output
    elif text=='C':#Defining C for Clear button
        scvalue.set('')
        screen.update()
    elif text == 'Bs':#Defining Bs for backspace
        scvalue.set(scvalue.get()[:-1])
        screen.update()
    elif text == '1/x':#Definig for 1/x value of input 
        try:
            value = 1 / float(scvalue.get())
            scvalue.set(value)
        except ZeroDivisionError:#Handling Zero Division Error
            scvalue.set('Error') 
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()

cal=Tk()
cal.geometry('1000x900')
cal.title('Calculator Application')
scvalue=StringVar()
scvalue.set('')
screen=Entry(cal,textvar=scvalue,font='arial 40 bold')#For input
screen.pack(fill=X,ipadx=8,pady=10,padx=10)

#Creating the Buttons 
#Frame 1
f=Frame(cal,bg='grey')
b=Button(f,text='(',padx=26,pady=18,font='arial 30 bold')# ( bracket open
b.pack(side=LEFT,padx=18,pady=5)
b.bind('<Button-1>',click)
b=Button(f,text=')',padx=26,pady=18,font='arial 30 bold')# ) bracket close
b.pack(side=LEFT,padx=18,pady=5)
b.bind('<Button-1>',click)
b=Button(f,text='%',padx=26,pady=18,font='arial 30 bold')# % to find remainder
b.pack(side=LEFT,padx=18,pady=5)
b.bind('<Button-1>',click)
b=Button(f,text='.',padx=26,pady=18,font='arial 30 bold')# . for decimal
b.pack(side=LEFT,padx=18,pady=5)
b.bind('<Button-1>',click)
b=Button(f,text='Bs',padx=26,pady=18,font='arial 30 bold')# Backspace
b.pack(side=LEFT,padx=18,pady=5)
b.bind('<Button-1>',click)
f.pack()
#Frame 2
f=Frame(cal,bg='grey')
b=Button(f,text='6',padx=26,pady=18,font='arial 30 bold')# Number 6
b.pack(side=LEFT,padx=18,pady=5)
b.bind('<Button-1>',click)
b=Button(f,text='7',padx=26,pady=18,font='arial 30 bold')# Number 7
b.pack(side=LEFT,padx=18,pady=5)
b.bind('<Button-1>',click)
b=Button(f,text='8',padx=26,pady=18,font='arial 30 bold')# Number 8
b.pack(side=LEFT,padx=18,pady=5)
b.bind('<Button-1>',click)
b=Button(f,text='9',padx=26,pady=18,font='arial 30 bold')# Number 9
b.pack(side=LEFT,padx=18,pady=5)
b.bind('<Button-1>',click)
b=Button(f,text='/',padx=26,pady=18,font='arial 30 bold')# / for division
b.pack(side=LEFT,padx=18,pady=5)
b.bind('<Button-1>',click)
f.pack()
#Frame 3
f=Frame(cal,bg='grey')
b=Button(f,text='2',padx=26,pady=18,font='arial 30 bold')# Number 2
b.pack(side=LEFT,padx=18,pady=5)
b.bind('<Button-1>',click)
b=Button(f,text='3',padx=26,pady=18,font='arial 30 bold')# Number 3
b.pack(side=LEFT,padx=18,pady=5)
b.bind('<Button-1>',click)
b=Button(f,text='4',padx=26,pady=18,font='arial 30 bold')# Number 4
b.pack(side=LEFT,padx=18,pady=5)
b.bind('<Button-1>',click)
b=Button(f,text='5',padx=26,pady=18,font='arial 30 bold')# Number 5
b.pack(side=LEFT,padx=18,pady=5)
b.bind('<Button-1>',click)
b=Button(f,text='*',padx=26,pady=18,font='arial 30 bold')# * for multiplication
b.pack(side=LEFT,padx=18,pady=5)
b.bind('<Button-1>',click)
f.pack()
#Frame 4
f=Frame(cal,bg='grey')
b=Button(f,text='0',padx=26,pady=18,font='arial 30 bold')# Number 0
b.pack(side=LEFT,padx=18,pady=5)
b.bind('<Button-1>',click)
b=Button(f,text='1',padx=26,pady=18,font='arial 30 bold')# Number 1
b.pack(side=LEFT,padx=18,pady=5)
b.bind('<Button-1>',click)
b=Button(f,text='**',padx=26,pady=18,font='arial 30 bold')# ** for exponentiating or Power
b.pack(side=LEFT,padx=18,pady=5)
b.bind('<Button-1>',click)
b=Button(f,text='+',padx=26,pady=18,font='arial 30 bold')# + for addition
b.pack(side=LEFT,padx=18,pady=5)
b.bind('<Button-1>',click)
b=Button(f,text='-',padx=26,pady=18,font='arial 30 bold')# - for subtraction
b.pack(side=LEFT,padx=18,pady=5)
b.bind('<Button-1>',click)
f.pack()
#Frame 5
f=Frame(cal,bg='grey')
b=Button(f,text='C',padx=26,pady=18,font='arial 30 bold')# For Clear All
b.pack(side=LEFT,padx=18,pady=5)
b.bind('<Button-1>',click)
b=Button(f,text='//',padx=26,pady=18,font='arial 30 bold')# For Floor Division
b.pack(side=LEFT,padx=18,pady=5)
b.bind('<Button-1>',click)
b = Button(f, text='1/x', padx=24, pady=24, font='arial 30 bold')# For getting 1/x value
b.pack(side=LEFT, padx=15, pady=10)
b.bind('<Button-1>', click)
b=Button(f,text='=',padx=26,pady=18,font='arial 30 bold')#Enter/ Equal to 
b.pack(side=LEFT,padx=18,pady=5)
b.bind('<Button-1>',click)
f.pack()

cal.mainloop()#Output with GUI
