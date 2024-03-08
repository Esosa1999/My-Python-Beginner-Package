from tkinter import *
win = Tk()
win.title('Calculator')  
win.geometry('515x365')
win.resizable(0,0)

# function to input
def button_click(item):
    global Expression
    Expression = Expression + str(item)
    input_text.set(Expression)

#function to clear
def button_clear():
    global Expression
    Expression= ''
    input_text.set('')

 # function to equal
def button_equal():
    global Expression
    result= str(eval(Expression))   
    input_text.set(result)




Expression = ''
input_text = StringVar()

#input field frame
input_frame= Frame(win, width=312, height=50)
input_frame.pack(side=TOP)
input_field= Entry(input_frame, font=('arial', 18, 'bold'), width=45, justify=LEFT, textvariable=input_text)
input_field.grid(row=0 , column=0)

#increase the height of the input field
input_field.pack(ipady=10)

#button frame
button_frame= Frame(win, width=310, height=270)
button_frame.pack()

#button for the first row
Clear= Button(button_frame, text='C', width=10, height=3, command=lambda: button_clear()).grid(row=0 , column=0, padx=1 , pady=1)
Open_Bracket= Button(button_frame, text='(', width=10 , height=3, command= lambda: button_click('(')).grid(row=0, column=1, padx=1, pady=1)
Close_Bracket= Button(button_frame, text=')', width=10 , height=3,command=lambda: button_click(')')).grid(row=0, column=2, padx=1, pady=1)
Divide= Button(button_frame, text='/', width=10, height=3, command=lambda: button_click('/')).grid(row=0, column=3, padx=1 ,pady=1)

#button for the second row
Seven= Button(button_frame, text=7, width=10 , height=3,command=lambda: button_click(7)).grid(row=1, column=0, padx=1, pady=1)
Eight= Button(button_frame, text=8, width=10 , height=3,command=lambda: button_click(8)).grid(row=1, column=1, padx=1, pady=1)
Nine= Button(button_frame, text=9, width=10 , height=3, command=lambda: button_click(9)).grid(row=1, column=2, padx=1, pady=1)
Multiplication= Button(button_frame, text='*', width=10 , height=3,command=lambda: button_click('*')).grid(row=1, column=3, padx=1, pady=1)

#button for the third row
four= Button(button_frame, text=4, width=10 , height=3,command=lambda: button_click(4)).grid(row=2, column=0, padx=1, pady=1)
five= Button(button_frame, text=5, width=10 , height=3,command=lambda: button_click(5)).grid(row=2, column=1, padx=1, pady=1)
six= Button(button_frame, text=6, width=10 , height=3, command=lambda: button_click(6)).grid(row=2, column=2, padx=1, pady=1)
Negative= Button(button_frame, text='-', width=10 , height=3,command=lambda: button_click('-') ).grid(row=2, column=3, padx=1, pady=1)

#button for the fourth row
one= Button(button_frame, text=1, width=10 , height=3,command=lambda: button_click(1)).grid(row=3, column=0, padx=1, pady=1)
two= Button(button_frame, text=2, width=10 , height=3,command=lambda: button_click(2)).grid(row=3, column=1, padx=1, pady=1)
Three= Button(button_frame, text=3, width=10 , height=3,command=lambda: button_click(3)).grid(row=3, column=2, padx=1, pady=1) 
plus= Button(button_frame, text='+', width=10 , height=3, command=lambda: button_click('+')).grid(row=3, column=3, padx=1, pady=1)

#button for the fifth row
plus_minus= Button(button_frame, text='+/-', width=10 , height=3, command=lambda: button_click('(-')).grid(row=4, column=0, padx=1, pady=1)
Zero= Button(button_frame, text=0, width=10 , height=3,command=lambda: button_click(0)).grid(row=4, column=1, padx=1, pady=1)
dot= Button(button_frame, text='.', width=10 , height=3, command=lambda: button_click('.')).grid(row=4, column=2, padx=1, pady=1)
equals= Button(button_frame, text='=', width=10 , height=3,command=lambda: button_equal()).grid(row=4, column=3, padx=1, pady=1)

    

win.mainloop()
