from tkinter import *
from random import randint
def new_rand():
	# Clear the input/entry box
	pw_otpt.delete(0, END)
	# Getting the length lent of input
	pw_length = abs(int(float(entry.get())))
	# variable to hold pswd
	my_password = ''
	for x in range(pw_length):
		my_password += chr(randint(33,126))
	# Displaying Password Output
	pw_otpt.insert(0, my_password)

def clipper():
	# Clearing the clipboard
	pg.clipboard_clear()
	# Copying to clipboard
	pg.clipboard_append(pw_otpt.get())

pg=Tk()
pg.title('Password Generator')
pg.geometry('400x400')
password_gen=chr(randint(33,126))
#Input Label
lf=LabelFrame(pg,text='Enter the required length of the password(Positive integer or float):')
lf.pack(pady=20)
#Box for input
entry=Entry(lf,font='arial 24 bold')
entry.pack(padx=20,pady=20)
#Box for Output
pw_otpt=Entry(pg,text='',font='arial 24 bold')
pw_otpt.pack(pady=20)
#Frame for Buttons
frame=Frame(pg)
frame.pack(pady=20)
#Generate Pswd Button
button=Button(frame,text='Generate Random Password',font='arial 12 bold',command=new_rand)
button.pack(padx=10)
#Copy Pswd Button
copy=Button(frame,text='Copy Password to ClipBoard',font='arial 12 bold',command=clipper)
copy.pack(padx=10)

pg.mainloop()#For GUI Output