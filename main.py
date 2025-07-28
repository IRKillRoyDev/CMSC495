from tkinter import *
import subprocess

root = Tk()
root.title('Group 1 - CMSC 495')
root.geometry("500x400")
root.protocol("WM_DELETE_WINDOW", root.quit)

def calculator():
    if os.path.exists('MortgageCalculator.py'):
        subprocess.run(['python', 'MortgageCalculator.py'])
    else:
        messagebox.showerror("Error", "MortgageCalculator Not Found")

def price():
    if os.path.exists('comp_tool.py'):
        subprocess.run(['python', 'comp_tool.py'])
    else:
        messagebox.showerror("Error", "Comparison Tool Not Found")

my_label_frame = LabelFrame(root, text="Please Choose a Tool Below")
my_label_frame.pack(pady=30)

my_frame = Frame(my_label_frame)
my_frame.pack(pady=10, padx=20)

# Button
my_button1 = ttk.Button(my_label_frame, text="Mortgage Calculator", command=calculator)
my_button1.pack(padx=10, pady=10)

my_button2 = ttk.Button(my_label_frame, text="Comp Tool", command=price)
my_button2.pack(pady=20)

root.mainloop()