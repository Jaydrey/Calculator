from tkinter import Tk
from tkinter import Entry
from tkinter import Button


root = Tk()
root.title("Simple Calculator")
root.configure(bg="#111421")
root.geometry('411x630')
root.resizable(0, 0)
entry = Entry(root, width=45, font=4, bg='#111524', fg='#fff')
entry.config(highlightbackground='#111524', highlightcolor='#111524', highlightthickness=2)
entry.grid(row=0, column=0, columnspan=4, pady=40, ipady=40)

END = "end"

def btnClick(value):
    if value=='clear': return entry.delete(0, END)
    #out=0
    num1 = entry.get()
    entry.delete(0, END)
    entry.insert(0, num1 + str(value))
    #output()
def btnAdd():
    num1 = entry.get()
    global f_num
    global op
    op = "add"
    f_num = num1
    entry.delete(0, END)
def btnsub():
    num1 = entry.get()
    global f_num
    global op
    op = "sub"
    f_num = num1
    entry.delete(0, END)
def btnmult():
    num1 = entry.get()
    global f_num
    global op
    op = "mult"
    f_num = num1
    entry.delete(0, END)
def btndiv():
    num1 = entry.get()
    global f_num
    global op
    op = "div"
    f_num = num1
    entry.delete(0, END)
def btnmod():
    num1 = entry.get()
    global f_num
    global op
    op = "mod"
    f_num = num1
    entry.delete(0, END)
def btnEqual():
    num2 = entry.get()
    entry.delete(0, END)
    if op=="add": entry.insert(0, int(f_num) + int(num2))
    elif op=="sub": entry.insert(0, int(f_num) - int(num2))
    elif op=="div": entry.insert(0, int(f_num) / int(num2))
    elif op=="mult": entry.insert(0, int(f_num) * int(num2))
    elif op=="mod": entry.insert(0, int(f_num) % int(num2))


button9 = Button(root, text="9", padx=43, pady=20, background="#000015", fg="white", border=None,font=2, command=lambda: btnClick(9))
button8 = Button(root, text="8", padx=43, pady=20, bg="#000015", fg="white", border=None,font=2, command=lambda: btnClick(8))
button7 = Button(root, text="7", bg="#000015", fg="white", border=None, font=2, command=lambda: btnClick(7))
button6 = Button(root, text="6", padx=43, pady=20, bg="#000015", fg="white", border=None,font=2, command=lambda: btnClick(6))
button5 = Button(root, text="5", padx=43, pady=20, bg="#000015", fg="white", border=None,font=2, command=lambda: btnClick(5))
button4 = Button(root, text="4", padx=43, pady=20, bg="#000015", fg="white", border=None,font=2, command=lambda: btnClick(4))
button3 = Button(root, text="3", padx=43, pady=20, bg="#000015", fg="white", border=None,font=2, command=lambda: btnClick(3))
button2 = Button(root, text="2", padx=43, pady=20, bg="#000015", fg="white", border=None,font=2, command=lambda: btnClick(2))
button1 = Button(root, text="1", padx=43, pady=20, bg="#000015", fg="white", border=None,font=2, command=lambda: btnClick(1))
button0 = Button(root, text="0", padx=43, pady=20, bg="#000015", fg="white", border=None,font=2, command=lambda: btnClick(0))
buttonOp = Button(root, text="CLEAR", padx=32, pady=25, fg="white", border=None,bg="#000015", command=lambda: btnClick('clear'))
buttonSys = Button(root, text="=", padx=43, pady=55, font=3, border=None,fg="white", bg="#29332b", command=btnEqual)
button10 = Button(root, text='+', padx=43, pady=20, bg='#000015', fg='#fff', font=2, border=None,command=btnAdd)
btn_sub = Button(root, text='-', padx=45, pady=20, bg='#000015', fg='#fff', font=2, border=None,command=btnsub)
btn_mult = Button(root, text='×', padx=45, pady=20, bg='#000015', fg='#fff', font=2, border=None,command=btnmult)
btn_div = Button(root, text='/', padx=45, pady=20, bg='#000015', fg='#fff', font=2, border=None,command=btndiv)
btn_mod = Button(root, text='%', padx=42, pady=20, bg='#000015', fg='#fff', font=2, border=None,command=btnmod)
btn_square = Button(root, text='X²', padx=42, pady=20, bg='#000015', fg='#fff', font=2, border=None,command=btnmod)
btn_exponent = Button(root, text='%', padx=42, pady=20, bg='#000015', fg='#fff', font=2, border=None,command=btnmod)
btn_pie = Button(root, text='%', padx=42, pady=20, bg='#000015', fg='#fff', font=2, border=None,command=btnmod)


button7.place(x=2, y=370, width=100, height=50)
button8.place(x=104, y=370, width=100, height=50)
button9.place(x=206, y=370, width=100, height=50)
button10.place(x=308, y=370, width=100, height=50)
button4.place(x=2, y=422, width=100, height=50)
button5.place(x=104, y=422, width=100, height=50)
button6.place(x=206, y=422, width=100, height=50)
btn_sub.place(x=308, y=422, width=100, height=50)
button1.place(x=2, y=474, width=100, height=50)
button2.place(x=104, y=474, width=100, height=50)
button3.place(x=206, y=474, width=100, height=50)
btn_mult.place(x=308, y=474, width=100, height=50)
buttonOp.place(x=2, y=526, width=100, height=50)
btn_mod.place(x=104, y=526, width=100, height=50)
btn_div.place(x=206, y=526, width=100, height=50)
buttonSys.place(x=308, y=526, width=100, height=50)
root.mainloop()