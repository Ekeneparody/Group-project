
import tkinter as tk
from tkinter import ttk

class Calculator:

    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.display = tk.Entry(master, width=20, font=('Arial', 16))
        self.display.grid(row=0, columnspan=4, sticky="SNEW")

        self.create_buttons()

    def create_buttons(self):
        buttons = ['7', '8', '9', '+',
                   '4', '5', '6', '-',
                   '1', '2', '3', '*',
                   '0', '.', '=', '/']

        for index, button in enumerate(buttons):
            button = ttk.Button(self.master, text=button, command=lambda value=button: self.press_button(value))
            button.grid(row=index // 4 + 1, column=index % 4, sticky='SNEW')

    def clear_display(self):
        self.display.delete(0, tk.END)

    def press_button(self, value):
        if value == '=':
            try:
                result = str(eval(self.display.get()))
            except:
                result = 'Error'
            self.clear_display()
            self.display.insert(0, result)
        elif value == 'C':
            self.clear_display()
        else:
            self.display.insert(tk.END, value)

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()