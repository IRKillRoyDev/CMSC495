from tkinter import *

root = Tk()
root.title('Mortgage Calculator')
root.geometry("500x400")

def validate_inputs():
    if not all([amount_entry.get(), down_payment_entry.get(), interest_entry.get(), term_entry.get()]):
        payment_label.config(text="Please Don't Leave Any Boxes Blank")
        return False
    if not (isfloat(amount_entry.get()) and isfloat(down_payment_entry.get()) and isfloat(interest_entry.get()) and term_entry.get().isdigit()):
        payment_label.config(text="Please Enter Valid Numbers")
        return False
    if float(amount_entry.get()) < 0 or float(down_payment_entry.get()) < 0 or float(interest_entry.get()) < 0 or int(term_entry.get()) < 0:
        payment_label.config(text="Please Only Enter Positive Numbers")
        return False
    return True

# Converts Loan Term From Years to Months
def loan_term_conversion(term_entry, payment_label, amount_entry, down_payment_entry, interest_entry):
    if not validate_inputs(amount_entry, down_payment_entry, interest_entry, term_entry, payment_label):
        return None #Return None if the validation fails (error message set by validate_inputs)
    termYears = int(term_entry.get())
    termMonths = termYears * 12
    return termMonths

# Converts Overall Interest Rate into Monthly Interest Rate
def monthly_interest_rate(term_entry, payment_label, amount_entry, down_payment_entry, interest_entry):
    if not validate_inputs(term_entry, payment_label, amount_entry, down_payment_entry, interest_entry):
        return None #Return None if the validation fails (error message set by validate_inputs)
    interestRate = float(interest_entry.get())
		if interestRate >= 0:
			monthlyRate = interestRate / 100 / 12
			return monthlyRate

# Calculates Total Amount of the Loan
def loan_amount(term_entry, payment_label, amount_entry, down_payment_entry, interest_entry):
    if not validate_inputs(term_entry, payment_label, amount_entry, down_payment_entry, interest_entry):
        return None #Return None if the validation fails (error message set by validate_inputs)
    houseCost = float(amount_entry.get())
	downPayment = float(down_payment_entry.get())
	loanAmount = houseCost - DownPayment
	if loanAmount < 0: #makes sure user did not put in a greater number for downpayment than the loan
    	payment_Label.config(text="Down Payment cannot exceed House Price")
    	return None
	return loanAmount

# Calculates Monthly Payment
def monthly_payment():
	# Import Results From Other Functions
	try:
		termMonths = int(loan_term_conversion())
		monthlyRate = float(monthly_interest_rate())
		loanAmount = float(loan_amount())
		# Calculate Monthly Payments
		monthlyPayment = (monthlyRate / (1 - (1 + monthlyRate)**(-termMonths))) * loanAmount
		return monthlyPayment
	EXCEPT (ValueError, TypeError):
     payment_label.config(text="Invalid input. Please check all fields.")
     return 0


# Displays Loan Amount and Monthly Payment Amount on Screen
def display():
	# Import Results From monthly_payment() and loan_amount() functions
	loanAmount = float(loan_amount())
	monthlyPayment = float(monthly_payment())

	# Format Outputs
	loanAmount = f"{loanAmount:,.2f}"
	monthlyPayment = f"{monthlyPayment:,.2f}"

	loan_amount_label.config(text=f"Loan Amount: ${loanAmount}")
	payment_label.config(text=f"Monthly Payment: ${monthlyPayment}")


# Checks Whether A Value Is A Float
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


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

# Place Labels and Entry Boxes on the Screen
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