from tkinter import *
from tkinter import messagebox
tasks=[]
count=1
def inpterr():
    if enterTaskField.get()=='':
        messagebox.showerror('Input Error')
        return 0
    return 1
def clear_taskField():
    enterTaskField.delete(0,END)

def insertTask():
    global count
    value=inpterr()
    if value==0:
        return 
    
    content=enterTaskField.get() + '\n'
    tasks.append(content)
    TextArea.insert('end -1 chars','['+str(count)+']'+ content)
    count+=1

    clear_taskField()
def delete():
    global count
    if len(tasks)==0:
         messagebox.showerror("No task")
         return
    number=taskNumberField.get(1.0,END)
    if number=='\n':
        messagebox.showerror('Input Error')
        return
    else:
        task_no=int(number)
    clear_taskField()
    tasks.pop(task_no - 1)
    count-=1
    TextArea.delete(1.0,END)
    for i in range(len(tasks)):
        TextArea.insert('end -1 chars', "[ " + str(i + 1) + " ] " + tasks[i])
    
if __name__=='__main__':
    todo=Tk()
    todo.configure(background='light blue')
    todo.title('To-Do List')#Titile
    todo.geometry('300x300')
    #Label
    enterTask = Label(todo, text = "Enter Your Task", bg = "green")
    #Entry Box for input
    enterTaskField=Entry(todo)
    #Submit Button
    Submit=Button(todo,text='Submit',fg='white',bg='black',command=insertTask)
    #Text Box for List
    TextArea = Text(todo, height = 5, width = 25, font = "arial 13")
    #Delete Task Button
    taskNumber = Label(todo, text = "Delete Task Number", bg = "Red")                  
    taskNumberField = Text(todo, height = 1, width = 2, font = "arial 13")
    Delete=Button(todo,text='Delete',fg='white',bg='black',command=delete)
    #Exit button
    Exit=Button(todo,text='Exit',fg='white',bg='black',command=exit)
    enterTask.grid(row=0,column=2)
    enterTaskField.grid(row=1,column=2,ipadx=50)
    Submit.grid(row=2,column=2)
    TextArea.grid(row=3,column=2,padx=10,sticky=W)
    #Box Position for Task Number input
    taskNumber.grid(row=4,column=2,pady=5)
    taskNumberField.grid(row=5,column=2)
    #Position for Delete Button
    Delete.grid(row = 6, column = 2, pady = 5)                  
    Exit.grid(row = 7, column = 2)
    todo.mainloop()
