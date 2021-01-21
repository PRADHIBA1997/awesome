from tkinter import *

root=Tk()
root.geometry("400x400")
root.title("hj")
def myDelete():
    
    myLabel.pack_forget()
    
def myClick(): 
    global myLabel 
    hello="Hello" +e.get()
    myLabel=Label(root,text=hello)
    e.delete(0,'end')
    myLabel.pack(pady=10)





    
e=Entry(root,width=50,font=("Bold",30))
e.pack(padx=10,pady=10)
myButton=Button(root,text="enter",command=myClick)
myButton.pack(pady=10)

mButton=Button(root,text="delete",command=myDelete)
mButton.pack(pady=10)




root.mainloop()    
