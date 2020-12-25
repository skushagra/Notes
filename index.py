import tkinter
from tkinter import *

import tkinter.filedialog

import tkinter.messagebox

from tkinter.colorchooser import askcolor

import datetime

import webbrowser

from tkinter.filedialog import askopenfilename, asksaveasfilename





def line():

    lin = "_" * 60

    text.insert(INSERT,lin)

    

def date():

    data = datetime.date.today()

    text.insert(INSERT,data)

   

def normal():

    text.config(font = ("Arial", 10))



def bold():

    text.config(font = ("Arial", 10, "bold"))



def underline():

    text.config(font = ("Arial", 10, "underline"))



def italic():

    text.config(font = ("Arial",10,"italic"))

    

def font():

    (triple,color) = askcolor()

    if color:

       text.config(foreground=color)



def kill():

    root.destroy()



def about():

    pass



def opn():

    text.delete(1.0 , END)

    file = open(askopenfilename() , 'r')

    if file != '':

        txt = file.read()

        text.insert(INSERT,txt)

    else:

        pass

    

def save():

    filename = asksaveasfilename()

    if filename:

        alltext = text.get(1.0, END)                      

        open(filename, 'w').write(alltext) 



def copy():

    text.clipboard_clear()

    text.clipboard_append(text.selection_get()) 



def paste():

    try:

        teext = text.selection_get(selection='CLIPBOARD')

        text.insert(INSERT, teext)

    except:

        tkMessageBox.showerror("Error","Your clipboard is empty!")



def clear():

    sel = text.get(SEL_FIRST, SEL_LAST)

    text.delete(SEL_FIRST, SEL_LAST)



def clearall():

    text.delete(1.0 , END)



def background():

    (triple,color) = askcolor()

    if color:

       text.config(background=color)

       

def about():

    ab = Toplevel(root)

    txt = "KS Notes\n(C) This application is licensed under Apache License v2.0\n https://sites.google.com/view/kushagras/applications "

    la = Label(ab,text=txt,foreground='black')

    la.pack()

    

def web():

    webbrowser.open('http://sites.google.com/view/siliconsys')





root = tkinter.Tk()

root.title("KS Notes")
root.geometry('900x900+300+300')

menu = Menu(root)
root.config(bg='#000000', menu=menu)
photo = PhotoImage(file='D:\\Kushagra\\Appliocation Icons\\Notes.png')
root.iconphoto(True, photo)

filemenu = Menu(root)

root.config(menu = menu)

menu.add_cascade(label="File", menu=filemenu)

filemenu.add_command(label="Open", command=opn)

filemenu.add_command(label="Save", command=save)


filemenu.add_command(label="Exit", command=kill)



modmenu = Menu(root)

menu.add_cascade(label="Edit",menu = modmenu)

modmenu.add_command(label="Copy", command = copy)

modmenu.add_command(label="Paste", command=paste)

modmenu.add_command(label = "Clear All", command = clear)

modmenu.add_command(label = "Erase All", command = clearall)







insmenu = Menu(root)

menu.add_cascade(label="Insert",menu= insmenu)

insmenu.add_command(label="Date",command=date)

insmenu.add_command(label="Line",command=line)







        

formatmenu = Menu(menu)

menu.add_cascade(label="Format",menu = formatmenu)

formatmenu.add_cascade(label="Color", command = font)

formatmenu.add_separator()

formatmenu.add_radiobutton(label='Normal',command=normal)

formatmenu.add_radiobutton(label='Bold',command=bold)

formatmenu.add_radiobutton(label='Italic',command=italic)

formatmenu.add_radiobutton(label='Underline Text',command=underline)



persomenu = Menu(root)

menu.add_cascade(label="Customize",menu=persomenu)

persomenu.add_command(label="Background", command=background)

                 

helpmenu = Menu(menu)

menu.add_cascade(label="More", menu=helpmenu)

helpmenu.add_command(label="About", command=about)

helpmenu.add_command(label="Website", command = web)

text = Text(root, height=30, width=60, font = ("Arial", 10))









scroll = Scrollbar(root, command=text.yview)

scroll.config(command=text.yview)                  

text.config(yscrollcommand=scroll.set)           

scroll.pack(side=RIGHT, fill=Y)

text.pack(expand=True, fill = 'both')

text.bind('Ctrl+s', save)
text.bind('Ctrl+o', opn)
text.bind('Ctrl+q', kill)
text.bind('Ctrl+c', copy)
text.bind('Ctrl+v', paste)


# root.resizable(0,0)

root.mainloop()
