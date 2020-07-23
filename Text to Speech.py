import pyttsx3
from tkinter import *

engine = pyttsx3.init()

def speak():
    text_to_speak=text_input.get()
    print(text_to_speak)
    engine.say(text_to_speak)
    engine.runAndWait()
    
    
root=Tk()
root.geometry('450x450')
root.title('Text to Speech Application')

Label(root,text='Welcome\nText to Speech\nApplication',font='Consolas 15 bold').pack()
myVar=StringVar()
myVar.set('Enter text below')
Label(root,textvariable=myVar,width=40).pack(pady=10)

text_input=StringVar()
Entry(root,textvariable=text_input,width=40).pack(pady=10)
print(text_input.get())

Button(root,text='Speak',command=speak).pack()
root.mainloop()