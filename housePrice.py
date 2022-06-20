from tkinter import *
import os

root = Tk()
root.title('Test Mortgage Calculator')
root.geometry("500x400")

def calculator():
    os.system('python mortgageTest2.py')


def payment():
    # Convert Entry Boxes to numbers
    price = int(amount_entry.get())

    # Format Outputs
    #loan = f"{price:,.2f}"

    # Output Loan Amount and Monthly Payment to the screen
    #loan_amount_label.config(text=f"Price: ${price}")


my_label_frame = LabelFrame(root, text="Enter Data Here")
my_label_frame.pack(pady=30)

my_frame = Frame(my_label_frame)
my_frame.pack(pady=10, padx=20)

# Define Labels and Entry Boxes
amount_label = Label(my_frame, text="Price of House")
amount_entry = Entry(my_frame, font=("Helvetica", 18))

# Put Labels and Entry Boxes on the Screen
amount_label.grid(row=0, column=0)
amount_entry.grid(row=0, column=1)

# Button
my_button = Button(my_label_frame, text="Display Price", command=calculator)
my_button.pack(pady=10)

# Output Labels
loan_amount_label = Label(root, text="", font=("Helvetica", 18))
loan_amount_label.pack()

payment_label = Label(root, text="", font=("Helvetica", 18))
payment_label.pack()

root.mainloop()