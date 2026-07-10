from tkinter import *
from functools import partial

win, clear_display = Tk(), True
res = Label(win, text="0", fg="white", bg="#333333", font=("Century Gothic", 20), anchor="e", justify="right")
res.grid(row=0, column=0, columnspan=4, sticky="nsew", pady=(0, 10))
def funct(value):
    global clear_display
    txt = res.cget("text")
    if value == "C": res.config(text="0"); clear_display = True
    elif value == "=":
        try: res.config(text=str(eval(txt.replace("÷", "/").replace("x^a", "**").replace("x", "*"))))
        except: res.config(text="Error")
        clear_display = True
    else:
        res.config(text=value if clear_display or txt == "0" else txt + value)
        clear_display = False
btn_txt = ["x^a", "//", "%", "C", "7", "8", "9", "+", "4", "5", "6", "-", "1", "2", "3", "x", "0", ".", "=", "÷"]
row, col = 1, 0
for txt in btn_txt:
    Button(win, text=txt, fg="white", bg="#f5a623", font=("Century Gothic", 14), relief="flat", bd=3,
           command=partial(funct, txt)).grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
    col, row = (col + 1) % 4, row + (col == 3)
for i in range(2, 7): win.grid_rowconfigure(i, weight=1)
for i in range(4): win.grid_columnconfigure(i, weight=1)

win.title("Python Calculator")
win.geometry("400x460+700+200")
win.config(bg="#212121", padx=10, pady=10)
win.mainloop()