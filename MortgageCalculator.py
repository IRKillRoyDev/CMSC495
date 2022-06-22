from tkinter import *

root = Tk()
root.title('Mortgage Calculator')
root.geometry("500x400")


# converts loan term from years to months
def loan_term_conversion():
	if term_entry.get():
		termYears = int(term_entry.get())
		termMonths = termYears * 12
		return termMonths
	else:
		payment_label.config(text="Please Don't Leave Any Boxes Blank")


# converts overall interest rate into monthly interest rate
def monthly_interest_rate():
	if interest_entry.get():
		interestRate = float(interest_entry.get())
		monthlyRate = interestRate / 100 / 12
		return monthlyRate
	else:
		payment_label.config(text="Please Don't Leave Any Boxes Blank")


# calculates total amount of the loan
def loan_amount():
	if amount_entry.get() and down_payment_entry.get():
		houseCost = float(amount_entry.get())
		downPayment = float(down_payment_entry.get())
		loanAmount = houseCost - downPayment
		return loanAmount
	else:
		payment_label.config(text="Please Don't Leave Any Boxes Blank")


# calculates monthly payment
def monthly_payment():
	# local variables
	termMonths = int(loan_term_conversion())
	monthlyRate = float(monthly_interest_rate())
	loanAmount = float(loan_amount())

	# Calculate Monthly Payments
	monthlyPayment = (monthlyRate / (1 - (1 + monthlyRate)**(-termMonths))) * loanAmount

	# Format Outputs
	loanAmount = f"{loanAmount:,.2f}"
	monthlyPayment = f"{monthlyPayment:,.2f}"

	# Output Loan Amount and Monthly Payment to the screen
	loan_amount_label.config(text=f"Loan Amount: ${loanAmount}")
	payment_label.config(text=f"Monthly Payment: ${monthlyPayment}")


my_label_frame = LabelFrame(root, text="Please Enter Data Here")
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
my_button = Button(my_label_frame, text="Calculate Loan Amount And Monthly Payment", command=monthly_payment)
my_button.pack(pady=10)

# Output Labels
loan_amount_label = Label(root, text="", font=("Helvetica", 18))
loan_amount_label.pack()

payment_label = Label(root, text="", font=("Helvetica", 18))
payment_label.pack()

root.mainloop()