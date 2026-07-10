from tkinter import *
from functools import partial

win = Tk()
res = Label(win, text="0", fg="white", bg="#333333", font=("Century Gothic", 20), anchor="e", justify="right")
res.grid(row=0, column=0, columnspan=4, sticky="nsew", pady=(0, 10))
btn_txt = ["x^a", "//", "%", "C", "7", "8", "9", "+", "4", "5", "6", "-", "1", "2", "3", "x", "0", ".", "=", "÷"]
def funct(value):
    txt = res.cget("text")
    if value == "C": res.config(text="0")
    elif value == "=":
        try: res.config(text=str(eval(txt.replace("÷", "/").replace("x^a", "**").replace("x", "*"))))
        except: res.config(text="Error")
    else: res.config(text=txt + value if txt != "0" else value)
row_num, col_num = 1, 0
for txt in btn_txt:
    Button(win, text=txt, fg="white", bg="#f5a623", font=("Century Gothic", 14), relief="flat", bd=3,
           command=partial(funct, txt)).grid(row=row_num, column=col_num, sticky="nsew", padx=5, pady=5)
    col_num, row_num = (col_num + 1) % 4, row_num + (col_num == 3)
for i in range(2, 7): win.grid_rowconfigure(i, weight=1, uniform="equal")
for i in range(4): win.grid_columnconfigure(i, weight=1, uniform="equal")
 
win.title("Python Calculator")
win.geometry("400x460+700+200")
win.config(bg="#212121", padx=10, pady=10)
win.mainloop()