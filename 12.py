from tkinter import*
from random import*

   
    
window = Tk()
window.geometry('485x550')
window.config(background= 'blue')
window.resizable(False, False)
Canvas(background = 'cyan', width = 460, height= 80).place(x= 10, y= 50)
computer = Label(text= 'Компьютер', font = 'Consolas 20', background = 'cyan', foreground = 'black')
computer.place(x= 200, y= 70)
pobeda = Label(text= 'победа', font = 'Consolas 20', background = 'cyan', foreground = 'black')
computer.place(x= 200, y= 200)
porashinie = Label(text= 'поражение', font = 'Consolas 20', background = 'cyan', foreground = 'black')
computer.place(x= 200, y= 200)
stone = Button(text= button, font = 'Consolas 20', background = 'orange', foreground = 'black', )
stone.place(x= 50, y= 400, width= 115, height= 80)
scissors = Button(text= button, font = 'Consolas 20', background = 'orange', foreground = 'black')
stone.place(x= 50, y= 400, width= 115, height= 80)
label1.place(x= 20, y= 70)


