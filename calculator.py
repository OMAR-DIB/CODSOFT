from tkinter import *

def press(num):
    global text
    text=text+str(num)
    equation_label.set(text)

def equals():
    global text
    try:
        total=str(eval(text))
        equation_label.set(total)
        text=total
    except SyntaxError:
        equation_label.set('syntax error')
        text=""
    except ZeroDivisionError:
        equation_label.set('arithmetic error')
        text=""

def clear():
    global text
    equation_label.set('')
    text=""

window=Tk()
window.title("Calculator")
window.geometry("500x500")

text=""
equation_label=StringVar()
label=Label(window,textvariable=equation_label,font=("sans serif",20),bg="white",
            width=23)
label.pack()


buttons=Frame()
buttons.pack()

button1=Button(buttons,text=1,width=9,height=4,font=35,
               command=lambda:press(1))
button1.grid(row=0,column=0)
button2=Button(buttons,text=2,width=9,height=4,font=35,
               command=lambda:press(2))
button2.grid(row=0,column=1)
button3=Button(buttons,text=3,width=9,height=4,font=35,
               command=lambda:press(3))
button3.grid(row=0,column=2)
button4=Button(buttons,text=4,width=9,height=4,font=35,
               command=lambda:press(4))
button4.grid(row=1,column=0)
button5=Button(buttons,text=5,width=9,height=4,font=35,
               command=lambda:press(5))
button5.grid(row=1,column=1)
button6=Button(buttons,text=6,width=9,height=4,font=35,
               command=lambda:press(6))
button6.grid(row=1,column=2)
button7=Button(buttons,text=7,width=9,height=4,font=35,
               command=lambda:press(7))
button7.grid(row=2,column=0)
button8=Button(buttons,text=8,width=9,height=4,font=35,
               command=lambda:press(8))
button8.grid(row=2,column=1)
button9=Button(buttons,text=9,width=9,height=4,font=35,
               command=lambda:press(9))
button9.grid(row=2,column=2)
button0=Button(buttons,text=0,width=9,height=4,font=35,
               command=lambda:press(0))
button0.grid(row=3,column=0)

plus=Button(buttons,text='+',width=9,height=4,font=35,
               command=lambda:press('+'))
plus.grid(row=0,column=3)
minus=Button(buttons,text='-',width=9,height=4,font=35,
               command=lambda:press('-'))
minus.grid(row=1,column=3)
multiply=Button(buttons,text='*',width=9,height=4,font=35,
               command=lambda:press('*'))
multiply.grid(row=2,column=3)
division=Button(buttons,text='/',width=9,height=4,font=35,
               command=lambda:press('/'))
division.grid(row=3,column=3)
equal=Button(buttons,text='=',width=9,height=4,font=35,
               command=equals)
equal.grid(row=3,column=2)
dote=Button(buttons,text='.',width=9,height=4,font=35,
               command=lambda:press('.'))
dote.grid(row=3,column=1)
clean=Button(window,text='Clear',width=15,height=4,font=35,
               command=clear)
clean.pack()
window.mainloop()