import csv
from tkinter import *
from tkinter import ttk

#def main():
#    with open('titles.csv', 'r') as homefile:
#        for line in csv.DictReader(homefile): # DictReader is a reader that returns a dictionary from the source.
#            for key in line:
#                print(key + ': ' + line[key]) #Prints all the keys and values in the csv file in a certain format.
#            print(line) #Prints the Dictionary entire line.
class HomeCompTool:
    """Class Doc String Summary Here
    """

    def __init__(self, root):
        """ The Home Comparison Tool takes user input and outputs comparative assessments.

        Args:
            root (_type_): _description_
        """

        root.title("House Comparative Assessment Tool")

        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        "Create the input for Square Feet"
        self.feet = StringVar()
        feet_entry = ttk.Entry(mainframe, width=7, textvariable=self.feet)
        feet_entry.grid(column=2, row=1, sticky=(W, E))

        "Create the input for Number of Beds"
        self.bed = StringVar()
        bed_entry = ttk.Entry(mainframe, width=7, textvariable=self.bed)
        bed_entry.grid(column=2, row=2, sticky=(W, E))

        "Create the input for the Number of baths"
        self.bath = StringVar()
        bath_entry = ttk.Entry(mainframe, width=7, textvariable=self.bath)
        bath_entry.grid(column=2, row=3, sticky=(W, E))

        "Create the output of the number of homes falling within the range of User Params"
        self.meters = StringVar()
        ttk.Label(mainframe, textvariable=self.meters).grid(column=2, row=4, sticky=(W, E))

        "Create the Calculate button to execute the search"
        ttk.Button(mainframe, text="Calculate", command=self.sort).grid(column=3, row=5, sticky=W)

        "Create the labels for the respective rows"
        ttk.Label(mainframe, text="Square Feet").grid(column=3, row=1, sticky=W)
        ttk.Label(mainframe, text="Bedrooms").grid(column=3, row=2, sticky=W)
        ttk.Label(mainframe, text="Bathrooms").grid(column=3, row=3, sticky=W)
        ttk.Label(mainframe, text="Your Selection has").grid(column=1, row=4, sticky=E)
        ttk.Label(mainframe, text="Comps").grid(column=3, row=4, sticky=W)

        "Create buffers using child so it's not repeated"
        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        "Put the focus on the Calculate button so a user doesn't have to use the curser"
        feet_entry.focus()
        root.bind("<Return>", self.sort)

    def sort(self, *args):
        """Get User Inputs and look for comps
        """
        sqft = 0
        baths = 0
        beds = 0
        try:
            sqft = float(self.feet.get())
            baths = float(self.bath.get())
            beds = float(self.bed.get())
            self.meters.set(int(0.3048 * (sqft + baths + beds) * 10000.0 + 0.5)/10000.0)
        except ValueError:
            pass


root = Tk()
HomeCompTool(root)
root.mainloop()