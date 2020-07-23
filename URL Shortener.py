from tkinter import *
import pyshorteners as srt
import pyperclip

root=Tk()
root.geometry('450x350')
root.title('URL Shortener application')

def shorten():
    
    short_url=srt.Shortener().tinyurl.short(link.get())
    link.set(short_url)
    pyperclip.copy(short_url)
    clip.set('Copied to Clipboard')

    

Label(root,text='Welcome to URL Shortener application',font='Consolas 15 bold').pack()
myVar=StringVar()
myVar.set('Enter the link below')
Label(root,textvariable=myVar,width=40).pack(pady=10)

link=StringVar()
Entry(root,textvariable=link,width=40).pack(pady=10)

Button(root,text='Shorten',command=shorten).pack()
clip=StringVar()
Label(root,textvariable=clip,width=40).pack(pady=10)

root.mainloop()
