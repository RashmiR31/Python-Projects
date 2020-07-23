import requests
from bs4 import BeautifulSoup
from tkinter import *

def weather_check():
    place=text_input.get()
    search='Weather in '+place
    url=f'https://www.google.com/search?&q={search}'
    r=requests.get(url)
    s=BeautifulSoup(r.text,'html.parser')
    update_weather = s.find('div',class_='BNeawe').text
    place_weather.set(update_weather)
    

root=Tk()
root.geometry('450x450')
root.title('Current Weather Application')
Label(root,text='Welcome\nCurrent Weather\nApplication',font='Consolas 15 bold').pack()

myVar=StringVar()
myVar.set('Enter place below')
Label(root,textvariable=myVar,width=40).pack(pady=10)

text_input=StringVar()
Entry(root,textvariable=text_input,width=40).pack(pady=10)

Button(root,text='Check',command=weather_check).pack()

place_weather=StringVar()
Entry(root,textvariable=place_weather,width=40).pack(pady=10)

root.mainloop()

#place=input('Enter Place:')
#search='Weather in '+place
#url=f'https://www.google.com/search?&q={search}'
#
#r=requests.get(url)
#s=BeautifulSoup(r.text,'html.parser')
#
#update = s.find('div',class_='BNeawe').text
#print(update)