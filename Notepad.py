from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import os

# functions
def nfile():
    global file
    root.title("untitled - Notepad")
    file = None
    textarea.delete(1.0, END)
def ofile():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files","*.*"),("Text Docments","*.txt")] )
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file)+ "-NotePad")
        textarea.delete(1.0, END)
        f = open(file, "r")
        textarea.insert(1.0, f.read())
        f.close()
    
def sfile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt", filetypes=[("All Files","*.*"),("Text Docments","*.txt")])
        if file =="":
            file = None
        else:
            f = open(file, "w")
            f.write(textarea.get(1.0, END))
            f.close()
            
            root.title(os.path.basename(file) + "-NotePad")
            print("file saved")
            
    else:
            f = open(file, "w")
            f.write(textarea.get(1.0, END))
            f.close()
            
def lfile():
    showinfo("notepad","the function will add later on")
def xtext():
    textarea.event_generate(("<<Cut>>"))
def ctext():
    textarea.event_generate(("<<Copy>>"))
def ptext():
    textarea.event_generate(("<<Paste>>"))
def shelp():
    pass
def fhelp():
    pass
def lab():
    showinfo("Notepad","this notepad is license to 505 company owner kamesh")
def scab():
    showinfo("socure code","the socure code in github'path'")
# functions

if __name__ == '__main__':
    #basic tkinter setup
    root = Tk()
    root.title("Untitled - Notepad")
    #root.wm_iconbitmap("1.ico") # your can add icon to notepad (should be in .ico file, icon)
    root.geometry("1000x680")
    
    #add textarea
    textarea = Text(root, font="lucida 12 ")
    file = None
    textarea.pack(expand=True,fill=BOTH)
    #menubar
    menubar = Menu(root)
    # filemenu starts
    filemenu = Menu(menubar, tearoff=0)
    # open new file
    filemenu.add_command(label="New", command = nfile)
    
    # to open alrasdy existing file
    filemenu.add_command(label="Open", command = ofile)
    
    # to save file
    filemenu.add_command(label="save", command = sfile)
    filemenu.add_command(label="Save As", command = lfile)
    
    filemenu.add_command(label="Print", command = lfile)
    
    filemenu.add_command(label="Close", command = lfile)
    
    
    menubar.add_cascade(label = "File", menu=filemenu)
    # filemenu ends
    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label = "Cut", command = xtext)
    editmenu.add_command(label = "Copy", command = ctext)
    editmenu.add_command(label = "Paste", command = ptext)
    editmenu.add_command(label = "Find", command = lfile)
    
    menubar.add_cascade(label = "Edit", menu=editmenu)
    # eidt munu starts
    
    #format starts
    formenu = Menu(menubar, tearoff=0)
    formenu.add_command(label = "Font", command = lfile)
    formenu.add_command(label = "Font size", command = lfile)
    
    menubar.add_cascade(label = "Format", menu = formenu)
    # format menu ends
    
    # help starts
    hemenu = Menu(menubar, tearoff=0)
    hemenu.add_command(label = "Shortcuts", command = shelp)
    hemenu.add_command(label = "Fonts", command = fhelp)
    
    menubar.add_cascade(label = "Help", menu = hemenu)
    #help ends
    
    # about us starts
    abmenu = Menu(menubar, tearoff=0)
    abmenu.add_command(label = "lisces", command = lab)
    abmenu.add_command(label = "Source code", command = scab)
    
    menubar.add_cascade(label = "About Us", menu = abmenu)
    #about us ends
    
    #scroll bar
    scroll = Scrollbar(textarea)
    scroll.pack(side=RIGHT,fill = "y")
    scroll.config(command=textarea.yview)
    textarea.config(yscrollcommand = scroll.set)
    #scroll bar ends
    
    # status bar start
    statusvar = StringVar()
    statusvar.set("Notepad                                                                                                                   |Window 100%|   |UFT-8|")
    sbar = Label(root, textvariable=statusvar, relief=SUNKEN, anchor=W)
    sbar.pack(side=BOTTOM, fill=BOTH)
    root.config(menu = menubar)
    
    textarea.pack()
    
    root.mainloop()
