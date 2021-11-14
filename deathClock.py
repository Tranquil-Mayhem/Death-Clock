# importing whole module
from tkinter import *
from tkinter.ttk import *
 
# importing strftime function to
# retrieve system's time
from time import strftime
import datetime
# creating tkinter window
root = Tk()
root.title('Death Clock')
root.geometry("1500x900")
root.configure(background='black')
       

img = PhotoImage(file="smile.png")
label = Label(
    root,
    image=img,
    borderwidth=0
)
label.pack(anchor = 'center')



def time():
    
    before = datetime.datetime.now()
    deathday = datetime.datetime(2081, 12, 25)
    lbl.config(text = '             DAWN OF A NEW DAY\n'  + str(deathday - before) + ' remain\n\n')
    lbl.after(50, time)
 
# Styling the label widget so that clock
# will look more attractive
lbl = Label(root, font = ('calibri', 40, 'bold'),
            background = 'black',
            foreground = 'red')
 
# Placing clock at the center
# of the tkinter window
lbl.pack(anchor = 'center')
lbl.pack(side = 'bottom')

time()
 
mainloop()
