from tkinter import *
import random
comp=0
user=0


def des():
    w.destroy()

def res():
    b4.grid_forget()
    b5.grid_forget()
    global comp
    global user
    comp=0
    user=0
    l=Label(text="ROCK  PAPER  SCISSOR",font=('Segoe UI Black',36),bg="gray10",fg="gray69",pady="20")
    la1.configure(text="\n\nMax points: 5\n\n", font=('Segoe Script', 12, 'bold'), bg="gray10", fg="white")
    la2.configure(text=f'\n\nUser points: {user}\t\t\tComputer points: {comp}\n', font=(
    'Segoe Script', 12, 'bold'), bg="gray10", fg="white")
    la1.grid(column=0, row=1, columnspan=6)
    b1.grid(column=0, row=4, columnspan=2)
    b2.grid(column=2, row=4, columnspan=2)
    b3.grid(column=4, row=4, columnspan=2)
    la2.grid(column=0, row=5, columnspan=6)
    l.grid(column=0, row=0, columnspan=6)

def rk():
    global comp
    global user
    cout = random.randint(1,4)
    if cout==1:
        la1.configure(font=('Segoe Script', 12, 'bold'), bg="gray10", fg="white",
            text="\nUser's move: Rock\t\t\tComputer's move: Rock\n\nTIE!\n")
    elif cout==2:
        comp = comp+1
        la1.configure(bg="gray10", fg="white",font=('Segoe Script', 12, 'bold'), text="\nUser's move: Rock\t\t\tComputer's move: Paper\n\nComputer gets a point.\n")
    elif cout==3:
        user=user+1
        la1.configure(font=('Segoe Script', 12, 'bold'), bg="gray10", fg="white",
            text="\nUser's move: Rock\t\t\tComputer's move: Paper\n\nUser gets a point!\n")
    la2.configure(text=f'\n\nUser points: {user}\t\t\tComputer points: {comp}\n', font=(
        'Segoe Script', 12, 'bold'), bg="gray10", fg="white")
    if user==5:
        b1.grid_forget()
        b2.grid_forget()
        b3.grid_forget()
        la1.configure(font=('Segoe Script', 16, 'bold'), bg="gray10", fg="hotpink1",
                      text="\nUser wins!!\nCongratulations!!\n")
        b4.grid(column=3, row=8, columnspan=3)
        b5.grid(column=0, row=8, columnspan=3)

    elif comp==5:
        b1.grid_forget()
        b2.grid_forget()
        b3.grid_forget()
        la1.configure(font=('Segoe Script', 16, 'bold'), bg="gray10", fg="tomato",
                      text="\nComputer wins!!\nBetter Luck Next time!!\n")
        b4.grid(column=3, row=8, columnspan=3)
        b5.grid(column=0, row=8, columnspan=3)




def pp():
    global comp
    global user
    cout = random.randint(1, 3)
    if(cout == 1):
        la1.configure(font=('Segoe Script',12,'bold'), bg="gray10", fg="white",
            text="\nUser's move: Paper\t\t\tComputer's move: Paper\n\nTIE!\n")
    elif(cout == 2):
        comp = comp+1
        la1.configure(font=('Segoe Script',12,'bold'), bg="gray10", fg="white",
            text="\nUser's move: Paper\t\t\tComputer's move: Scissor\n\nComputer gets a point!\n")
    elif(cout == 3):
        user = user+1
        la1.configure(font=('Segoe Script',12,'bold'), bg="gray10", fg="white",
            text="\nUser's move: Paper\t\t\tComputer's move: Rock\n\nUser gets a point!\n")
    la2.configure(text=f'\n\nUser points: {user}\t\t\tComputer points: {comp}\n', font=(
        'Segoe Script', 12, 'bold'), bg="gray10", fg="white")
    if user == 5:
        b1.grid_forget()
        b2.grid_forget()
        b3.grid_forget()
        la1.configure(font=('Segoe Script', 16, 'bold'), bg="gray10", fg="hotpink1",
                      text="\nUser wins!!\nCongratulations!!\n")
        b4.grid(column=3,row=8,columnspan=3)
        b5.grid(column=0, row=8, columnspan=3)

    elif comp == 5:
        b1.grid_forget()
        b2.grid_forget()
        b3.grid_forget()
        la1.configure(font=('Segoe Script', 16, 'bold'), bg="gray10", fg="tomato",
                      text="\nComputer wins!!\nBetter Luck Next time!!\n")
        b4.grid(column=3, row=8, columnspan=3)
        b5.grid(column=0, row=8, columnspan=3)

def sc():
    global comp
    global user
    cout = random.randint(1, 3)
    if(cout == 1):
        la1.configure(font=('Segoe Script', 12, 'bold'), bg="gray10", fg="white",
            text="\nUser's move: Scissor\t\t\tComputer's move: Scissor\n\nTIE!\n")
    elif(cout == 2):
        comp = comp+1
        la1.configure(font=('Segoe Script', 12, 'bold'), bg="gray10", fg="white",
            text="\nUser's move: Scissor\t\t\tComputer's move: Rock\n\nComputer gets a point!\n")
    elif(cout == 3):
        user = user+1
        la1.configure(font=('Segoe Script', 12, 'bold'), bg="gray10", fg="white",
            text="\nUser's move: Scissor\t\t\tComputer's move: Paper\n\nUser gets a point!\n")
    la2.configure(text=f'\n\nUser points: {user}\t\t\tComputer points: {comp}\n', font=(
        'Segoe Script', 12, 'bold'), bg="gray10", fg="white")
    if user == 5:
        b1.grid_forget()
        b2.grid_forget()
        b3.grid_forget()
        la1.configure(font=('Segoe Script', 16, 'bold'), bg="gray10", fg="hotpink1",
                      text="\nUser wins!!\nCongratulations!!\n")
        b4.grid(column=3, row=8, columnspan=3)
        b5.grid(column=0, row=8, columnspan=3)
    elif comp == 5:
        b1.grid_forget()
        b2.grid_forget()
        b3.grid_forget()
        la1.configure(font=('Segoe Script', 16, 'bold'), bg="gray10", fg="tomato",
                      text="\nComputer wins!!\nBetter Luck Next time!!\n")
        b4.grid(column=3, row=8, columnspan=3)
        b5.grid(column=0, row=8, columnspan=3)


w=Tk()
w.minsize(840,500)
w.title("rock-paper-scissor-game")
w.configure(bg="gray10")

l=Label(text="ROCK  PAPER  SCISSOR",font=('Segoe UI Black',36),bg="gray10",fg="gray69",pady="20")

la1 = Label(text="\n\nMax points: 5\n\n", font=(
    'Segoe Script', 12, 'bold'), bg="gray10", fg="white")
la2 = Label(text=f'\n\nUser points: {user}\t\t\tComputer points: {comp}\n', font=(
    'Segoe Script', 12, 'bold'), bg="gray10", fg="white")
b1 = Button(w, text="ROCK", command=rk, pady="20", font=('Segoe UI Black', 20, 'bold'),
            padx="32", bd=0, bg="black", fg="gray69", activebackground="tomato", activeforeground="white")
b2 = Button(w, text="PAPER", command=pp, pady="20", font=('Segoe UI Black', 20, 'bold'), padx="32",
            bd=0, bg="black", fg="gray69",activebackground="gold", activeforeground="white")
b3 = Button(w, text="SCISSOR", command=sc, pady="20", padx="32", bd=0, bg="black",
            fg="gray69", font=('Segoe UI Black', 20, 'bold'), activebackground="turquoise1", activeforeground="white")
b4 = Button(w, text="END", command=des, pady="14", padx="30", bd=0, bg="black",
            fg="gray69", font=('Segoe UI Black', 13, 'bold'), activebackground="IndianRed1", activeforeground="white")
b5 = Button(w, text="RESTART", command=res, pady="14", padx="20", bd=0, bg="black",
            fg="gray69", font=('Segoe UI Black', 13, 'bold'), activebackground="forest green", activeforeground="white")
l.grid(column=0,row=0,columnspan=6)
la1.grid(column=0,row=1,columnspan=6)
b1.grid(column=0,row=4,columnspan=2)
b2.grid(column=2,row=4,columnspan=2)
b3.grid(column=4,row=4,columnspan=2)
la2.grid(column=0,row=5,columnspan=6)


def oe(e):
    b1.config(background='red4',fg="white")


def ol(e):
    b1.config(background='black',fg="gray69")

b1.bind('<Enter>', oe)
b1.bind('<Leave>', ol)


def oe(e):
    b2.config(background='dark goldenrod',fg="white")


def ol(e):
    b2.config(background='black',fg="gray69")


b2.bind('<Enter>', oe)
b2.bind('<Leave>', ol)


def oe(e):
    b3.config(background='turquoise4',fg="white")


def ol(e):
    b3.config(background='black',fg="gray69")


b3.bind('<Enter>', oe)
b3.bind('<Leave>', ol)


def oe(e):
    b4.config(background='orangered2')


def ol(e):
    b4.config(background='black')


b4.bind('<Enter>', oe)
b4.bind('<Leave>', ol)


def oe(e):
    b5.config(background='spring green')


def ol(e):
    b5.config(background='black')


b5.bind('<Enter>', oe)
b5.bind('<Leave>', ol)


w.grid_rowconfigure(0, weight=1)
w.grid_rowconfigure(1, weight=1)
w.grid_rowconfigure(2, weight=1)
w.grid_rowconfigure(3, weight=1)
w.grid_rowconfigure(4, weight=1)
w.grid_rowconfigure(5, weight=1)
w.grid_rowconfigure(6, weight=1)
w.grid_rowconfigure(7, weight=1)
w.grid_rowconfigure(8, weight=1)
w.grid_columnconfigure(0, weight=1)
w.grid_columnconfigure(1, weight=1)
w.grid_columnconfigure(2, weight=1)
w.grid_columnconfigure(3, weight=1)
w.grid_columnconfigure(4, weight=1)
w.grid_columnconfigure(5, weight=1)

w.mainloop()
