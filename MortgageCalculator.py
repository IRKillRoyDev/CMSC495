from tkinter import *

    #"""Revision History
    #2 JUN - Created test mortgage calculator program to determine formulas for all calculations
    #16 JUN - Created dummy main program to call mortgage calculator from to test functionality
    #25 JUN - Created clean mortgage calculator program based on test program written earlier
    #25 JUN - Changed data types for user input based on ICD Document
    #26 JUN - Separated all calculations into different functions within program as per project analysis document
    #27 JUN - Placed display functionality into its own function as per project analysis document
    #"""

root = Tk()
root.title('Mortgage Calculator')
root.geometry("500x400")


# Checks Whether A Value Is A Float
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


# Converts Loan Term From Years to Months
def loan_term_conversion():
	if term_entry.get():
		if term_entry.get().isdigit():
			termYears = int(term_entry.get())
			termMonths = termYears * 12
			return termMonths
		else:
			loan_amount_label.config(text="")
			payment_label.config(text="Please Only Enter Positive Integers")
	else:
		loan_amount_label.config(text="")
		payment_label.config(text="Please Don't Leave Any Boxes Blank")


# Converts Overall Interest Rate into Monthly Interest Rate
def monthly_interest_rate():
	if interest_entry.get():
		if isfloat(interest_entry.get()):
			interestRate = float(interest_entry.get())
			monthlyRate = interestRate / 100 / 12
			return monthlyRate
		else:
			loan_amount_label.config(text="")
			payment_label.config(text="Please Only Enter A Decimal Value")
	else:
		loan_amount_label.config(text="")
		payment_label.config(text="Please Don't Leave Any Boxes Blank")


# Calculates Total Amount of the Loan
def loan_amount():
	if amount_entry.get() and down_payment_entry.get():
		if isfloat(amount_entry.get()) and isfloat(down_payment_entry.get()):
			houseCost = float(amount_entry.get())
			downPayment = float(down_payment_entry.get())
			loanAmount = houseCost - downPayment
			return loanAmount
		else:
			loan_amount_label.config(text="")
			payment_label.config(text="Please Only Enter A Decimal Value")
	else:
		loan_amount_label.config(text="")
		payment_label.config(text="Please Don't Leave Any Boxes Blank")


# Calculates Monthly Payment
def monthly_payment():
	# Import Results From Other Functions
	termMonths = int(loan_term_conversion())
	monthlyRate = float(monthly_interest_rate())
	loanAmount = float(loan_amount())

	# Calculate Monthly Payments
	monthlyPayment = (monthlyRate / (1 - (1 + monthlyRate)**(-termMonths))) * loanAmount
	return monthlyPayment


# Displays Output
def display():
	# Import Results From monthly_payment() and loan_amount() functions
	loanAmount = float(loan_amount())
	monthlyPayment = float(monthly_payment())

	# Format Outputs
	loanAmount = f"{loanAmount:,.2f}"
	monthlyPayment = f"{monthlyPayment:,.2f}"

	# Output Loan Amount and Monthly Payment to the screen
	loan_amount_label.config(text=f"Loan Amount: ${loanAmount}")
	payment_label.config(text=f"Monthly Payment: ${monthlyPayment}")


# Frame Creation
my_label_frame = LabelFrame(root, text="Please Enter Data Here")
my_label_frame.pack(pady=30)

my_frame = Frame(my_label_frame)
my_frame.pack(pady=10, padx=20)

# Define Labels and Entry Boxes
amount_label = Label(my_frame, text="Price of House")
amount_entry = Entry(my_frame, font=("Helvetica", 18))

interest_label = Label(my_frame, text="Interest Rate")
interest_entry = Entry(my_frame, font=("Helvetica", 18))

term_label = Label(my_frame, text="Term (Years)")
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

# Button Setup and Action
my_button = Button(my_label_frame, text="Calculate Loan Amount And Monthly Payment", command=display)
my_button.pack(pady=10)

# Output Labels
loan_amount_label = Label(root, text="", font=("Helvetica", 18))
loan_amount_label.pack()

payment_label = Label(root, text="", font=("Helvetica", 18))
payment_label.pack()

root.mainloop()