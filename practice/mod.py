import tkinter as tk

def show_output():
    a = int(input_a.get())
    b = int(input_b.get())
    result = (a%b)
    output = result
    output_label.configure(text=output)

window = tk.Tk()
window.title("Modular")
window.minsize(width=400,height=600)

title_label = tk.Label(master=window,text='หาเศษ',height=3,)
title_label.pack()

input_a = tk.Entry(master=window,justify='center')
input_a.pack()

mod_label = tk.Label(master=window,text='%',height=3)
mod_label.pack()

input_b = tk.Entry(master=window,justify='center')
input_b.pack()

s_label = tk.Label(master=window,text='',height=2)
s_label.pack()

mod_button = tk.Button(master=window,text='MOD',width=7,height=2,fg='white',bg='black',command=show_output)
mod_button.pack()

output_label = tk.Label(master=window,height=3)
output_label.pack()

window.mainloop()