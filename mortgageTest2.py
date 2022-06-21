from tkinter import *

root = Tk()
root.title('Test Mortgage Calculator')
root.geometry("500x400")

def payment():
    if amount_entry.get() and interest_entry.get() and term_entry.get() and down_payment_entry.get():
        # Convert Entry Boxes to numbers
        years = int(term_entry.get())
        months = years * 12
        rate = float(interest_entry.get())
        price = int(amount_entry.get())
        down_payment = int(down_payment_entry.get())
        loan = price - down_payment
        # Calculate The Loan
        # Monthly Interest Rate
        monthly_rate = rate / 100 / 12
        # Calculate Monthly Payments
        payment = (monthly_rate / (1 - (1 + monthly_rate)**(-months))) * loan
        # Format Outputs
        loan = f"{loan:,.2f}"
        payment = f"{payment:,.2f}"

        # Output Loan Amount and Monthly Payment to the screen
        loan_amount_label.config(text=f"Loan Amount: ${loan}")
        payment_label.config(text=f"Monthly Payment: ${payment}")

    else:
        payment_label.config(text="Don't Leave Any Boxes Blank")

my_label_frame = LabelFrame(root, text="Enter Data Here")
my_label_frame.pack(pady=30)

my_frame = Frame(my_label_frame)
my_frame.pack(pady=10, padx=20)

# Define Labels and Entry Boxes
amount_label = Label(my_frame, text="Price of House")
amount_entry = Entry(my_frame, font=("Helvetica", 18))

interest_label = Label(my_frame, text="Interest Rate")
interest_entry = Entry(my_frame, font=("Helvetica", 18))

term_label = Label(my_frame, text="Term (years)")
term_entry = Entry(my_frame, font=("Helvetica", 18))

down_payment_label = Label(my_frame, text="Down Payment Amount")
down_payment_entry = Entry(my_frame, font=("Helvetica", 18))

# Put Labels and Entry Boxes on the Screen
amount_label.grid(row=0, column=0)
amount_entry.grid(row=0, column=1)

interest_label.grid(row=1, column=0)
interest_entry.grid(row=1, column=1, pady=5)

term_label.grid(row=2, column=0)
term_entry.grid(row=2, column=1)

down_payment_label.grid(row=3, column=0)
down_payment_entry.grid(row=3, column=1, pady=5)

# Button
my_button = Button(my_label_frame, text="Calculate Monthly Payment", command=payment)
my_button.pack(pady=10)

# Output Labels
loan_amount_label = Label(root, text="", font=("Helvetica", 18))
loan_amount_label.pack()

payment_label = Label(root, text="", font=("Helvetica", 18))
payment_label.pack()

root.mainloop()