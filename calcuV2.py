from tkinter import *
from functools import partial
 
win = Tk()
res = Label(win, text="0", fg="black", bg="#ffffff", font=("Century Gothic", 20), anchor="e", justify="right")
res.grid(row=0, column=0, columnspan=4, sticky="nsew", pady=20)
btn_txt = ["**", "//", "%", "C", "7", "8", "9", "+", "4", "5", "6", "-", "1", "2", "3", "x", "0", ".", "=", "÷"]
def funct(value):
    txt = res.cget("text")
    if value == "C": res.config(text="0")
    elif txt == "Error":
        res.config(text=value)
    elif value == "=":
        try: res.config(text=str(eval(txt.replace("÷", "/").replace("x", "*").replace("...", value))))
        except: res.config(text="Error")
        
    else: res.config(text=txt + value if txt != "0" else value)
row, col = 1, 0
for txt in btn_txt:
    Button(win, text=txt, fg="black", bg="#D3D3D3", font=("Century Gothic", 15), relief="flat", bd=5,
           command=partial(funct, txt)).grid(row=row, column=col, sticky="nsew", padx=3, pady=3)
    col, row = (col + 1) % 4, row + (col == 3)
for i in range(4): win.grid_columnconfigure(i, weight=1)
 
win.title("Python Calculator")
win.geometry("300x345+765+335")
win.config(bg="#ffffff")
win.mainloop()