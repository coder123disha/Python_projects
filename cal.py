import tkinter as tk


def button_press(num):
    global equation_text
    equation_text=equation_text+str(num)
    equation_label.set(equation_text)

def equals():
    global equation_text
    try:

        total=str(eval(equation_text))

        equation_label.set(total)

        equation_text=total
    except SyntaxError:

        equation_label.set("syntax error")
        equation_text="" 

    except ZeroDivisionError:

        equation_label.set("arithmetic error")
        equation_text="" 


def clear():
    global equation_text

    equation_label.set("")
    equation_text=""
    

window=tk.Tk()

window.title("Calculator Program")
window.geometry('500x500')

equation_text=""
equation_label=tk.StringVar()

label=tk.Label(window,textvariable=equation_label,font=("consolas",20),bg="white",width=29,height=2)
label.pack()

frame=tk.Frame(window)
frame.pack()

button1=tk.Button(frame,text=1,height=2,width=9,font=35,command=lambda:button_press(1))
button1.grid(row=0,column=0)
button2=tk.Button(frame,text=2,height=2,width=9,font=35,command=lambda:button_press(2))
button2.grid(row=0,column=1)
button3=tk.Button(frame,text=3,height=2,width=9,font=35,command=lambda:button_press(3))
button3.grid(row=0,column=2)
button4=tk.Button(frame,text=4,height=2,width=9,font=35,command=lambda:button_press(4))
button4.grid(row=1,column=0)
button5=tk.Button(frame,text=5,height=2,width=9,font=35,command=lambda:button_press(5))
button5.grid(row=1,column=1)
button6=tk.Button(frame,text=6,height=2,width=9,font=35,command=lambda:button_press(6))
button6.grid(row=1,column=2)
button7=tk.Button(frame,text=7,height=2,width=9,font=35,command=lambda:button_press(7))
button7.grid(row=2,column=0)
button8=tk.Button(frame,text=8,height=2,width=9,font=35,command=lambda:button_press(8))
button8.grid(row=2,column=1)
button9=tk.Button(frame,text=9,height=2,width=9,font=35,command=lambda:button_press(9))
button9.grid(row=2,column=2)
button0=tk.Button(frame,text=0,height=2,width=9,font=35,command=lambda:button_press(0))
button0.grid(row=3,column=0)

plus=tk.Button(frame,text='+',height=2,width=9,font=35,command=lambda:button_press('+'))
plus.grid(row=0,column=3)

minus=tk.Button(frame,text='-',height=2,width=9,font=35,command=lambda:button_press('-'))
minus.grid(row=1,column=3)

multi=tk.Button(frame,text='*',height=2,width=9,font=35,command=lambda:button_press('*'))
multi.grid(row=2,column=3)

divide=tk.Button(frame,text='/',height=2,width=9,font=35,command=lambda:button_press('/'))
divide.grid(row=3,column=3)

equal=tk.Button(frame,text='=',height=2,width=9,font=35,command=equals)
equal.grid(row=3,column=2)

decimal=tk.Button(frame,text='.',height=2,width=9,font=35,command=lambda:button_press('.'))
decimal.grid(row=3,column=1)


Clear=tk.Button(window,text='Clear',height=2,width=9,font=35,command=clear)
Clear.pack()



window.mainloop()
