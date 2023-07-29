'''
from tkinter import* #importing all classes from tkinter
root=Tk() #creating istantance of window
root.title("my window") #name of window
root.geometry('500x500+250+50') #width X height + x and+y position to display 
root.mainloop() # most imp to start window
'''
'''
from tkinter import*
root=Tk() 
root.title("SOUMA")
root.geometry('400x200+100+100')
root.mainloop()
'''
'''
from tkinter import*
def clicked():
    print("go corona go")
root=Tk() 
root.title("SOUMA")
B=Button(root,text='click me',command=clicked)#cerated the control
#root=ref of screen ---- text=is to show on button
B.pack()
root.geometry('400x200+100+100')
root.mainloop()
'''
'''
#question click me me clicked click you you clicked
from tkinter import*
def clicked():
    print("me clicked")
def  click():
    print("you clciked")
root=Tk() 
root.title("SOUMA")
B=Button(root,text='click me',command=clicked)
B.pack() # sequence of pack typed decides the sequence to show on 
B1=Button(root,text='click you',command=click)
B1.pack()
root.geometry('300x100+100+100')
root.mainloop()

'''
