

from tkinter import Tk
from tkinter import Label
import time
def timpul():
    timevar=time.strftime("%I:%M:%S %p")
    ceas.config(text=timevar)
    ceas.after(200,timpul)

mam=Tk()
mam.title("ceas digital")
ceas=Label(mam,font=('Arial',100),bg='black',fg='grey')
ceas.pack()
timpul()
mam.mainloop()
