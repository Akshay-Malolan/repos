from tkinter import *
def clear():
    principal_field.delete(0,END)
    rate_field.delete(0,END)
    time_field.delete(0,END)
    compound_field.delete(0,END)
    simple_field.delete(0,END)
    principal_field.focus_set()

def calculate():
    principal=int(principal_field.get())
    rate=float(rate_field.get())
    time=int(time_field.get())
    simple=principal*(rate*time)/100
    ci=principal*(pow((1 + (rate/100)),time))
    simple_field.insert(10,simple)
    compound_field.insert(10,ci)

if __name__=='__main__':

    cicalc=Tk()
    cicalc.configure(background='light blue')
    cicalc.geometry('500x500')
    cicalc.title('Compound Interest Calculator')

    label1 = Label(cicalc, text = "Principal Amount(Rs) : ", fg = 'white', bg = 'black')
    label2 = Label(cicalc, text = "Rate : ", fg = 'white', bg = 'black')
    label3 = Label(cicalc, text = "Time : ", fg = 'white', bg = 'black')
    label4 = Label(cicalc, text = "Simple Interest (Rs) : ", fg = 'white', bg = 'black')
    label5= Label(cicalc, text = "Compound Interest (Rs) : ", fg = 'white', bg = 'black')
    
    label1.grid(row = 1, column = 0, padx = 10, pady = 10)  
    label2.grid(row = 2, column = 0, padx = 10, pady = 10)  
    label3.grid(row = 3, column = 0, padx = 10, pady = 10)
    label4.grid(row = 5, column = 0, padx = 10, pady = 10)
    label5.grid(row = 7, column = 0, padx = 10, pady = 10)

    principal_field = Entry(cicalc)  
    rate_field = Entry(cicalc)  
    time_field = Entry(cicalc)
    simple_field=Entry(cicalc)
    compound_field = Entry(cicalc)

    principal_field.grid(row = 1, column = 1, padx = 10, pady = 10)  
    rate_field.grid(row = 2, column = 1, padx = 10, pady = 10)  
    time_field.grid(row = 3, column = 1, padx = 10, pady = 10)
    simple_field.grid(row = 5, column = 1, padx = 10, pady = 10)
    compound_field.grid(row = 7, column=1, padx=10, pady=10)

    button1 = Button(cicalc, text = "Submit", bg = "blue", fg = "white", command = calculate)  
    button2 = Button(cicalc, text = "Clear", bg = "blue", fg = "white", command = clear)
    button1.grid(row = 4, column = 1, pady = 10) 
    button2.grid(row = 9, column = 1, pady = 10)

    cicalc.mainloop()
