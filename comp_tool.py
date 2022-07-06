"""Module Docstring"""

from tkinter import *
from tkinter import ttk
import pandas as pd
import numpy as np

"""Revision History
    May 28 - Added function to open CSV
    20 Jun - Created the main function that pulls the data out of the CSV
    25 Jun - Added a window for the Comp Tool
    25 Jun - Added a 'List' button
    25 Jun - Added an initial value to user inputs
    25 Jun - Added function to list the house data
    26 Jun - Used Pandas to format the house data in the 'list' of homes
    27 Jun - Moved the functions to the top of the __init__.
    3 Jul - Updated the synthetic data to have approx 3000 entries of randomized numbers
    4 Jul - finished adding the filter alogrithm to sort the data
    """
class HomeCompTool:
    """Class Doc String Summary Here
    """
    data = pd.read_csv('titles.csv')
    df = pd.DataFrame(data).set_index('Location')
    #filtered_values = df.query(sqft_str + ' & ' + baths_str + ' & ' + beds_str)

    def __init__(self, root):
        """ The Home Comparison Tool takes user input and outputs comparative assessments.
        """
        self.root = root

        def write_to_log(msg):
            """Writes the data to the frame inside the mainframe

            Args:
                msg (str): Input to be written into the frame
            """
            frame['state'] = 'normal'
            if frame.index('end-1c')!='1.0':
                frame.insert('end', '\n')
            frame.insert('end', msg)
            frame['state'] = 'disabled'

        def list_home():
            """_Pulls the data from the csv in a data frame that can be read easily
            """
            data = pd.read_csv('titles.csv')
            df = pd.DataFrame(data).set_index('Location')
            write_to_log(df)

        def sort(*args):
            """Get User Inputs and look for comps
            """
            data = pd.read_csv('titles.csv')
            df = pd.DataFrame(data).set_index('Location')
            try:
                sqft = float(self.feet.get())
                baths = float(self.bath.get())
                beds = float(self.bed.get())
                #Pending call to alogrithm
                high_sqft = sqft + 50
                low_sqft = sqft - 50
                sqft_str = str(low_sqft)+ ' <= Size <= '+ str(high_sqft)
                high_baths = baths + 1
                low_baths = baths - 1
                baths_str = str(low_baths)+ ' <= Bath <= '+ str(high_baths)
                high_beds = beds + 1
                low_beds = beds - 1
                beds_str = str(low_beds)+' <= Bedroom <= '+ str(high_beds)

                filtered_values = df.query(sqft_str + ' & ' + baths_str + ' & ' + beds_str)
                self.comps.set(filtered_values['Price'].mean())
                write_to_log(filtered_values)
            except ValueError:
                pass

        self.root.title("House Comparative Assessment Tool")

        mainframe = ttk.Frame(self.root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        #Create the input for Square Feet
        self.feet = StringVar()
        feet_entry = ttk.Entry(mainframe, width=7, textvariable=self.feet)
        feet_entry.grid(column=2, row=1, sticky=(W, E))
        feet_entry.insert(0,0)

        #Create the input for Number of Beds
        self.bed = StringVar()
        bed_entry = ttk.Entry(mainframe, width=7, textvariable=self.bed)
        bed_entry.grid(column=2, row=2, sticky=(W, E))
        bed_entry.insert(0,0)

        #Create the input for the Number of baths
        self.bath = StringVar()
        bath_entry = ttk.Entry(mainframe, width=7, textvariable=self.bath)
        bath_entry.grid(column=2, row=3, sticky=(W, E))
        bath_entry.insert(0,0)

        #Create the output of the number of homes falling within the range of User Params
        self.comps = StringVar()
        ttk.Label(mainframe, textvariable=self.comps).grid(column=2, row=4, sticky=(W, E))

        #Create a frame inside the dialog window
        frame = Text(mainframe,state='disabled',wrap='none')
        frame.grid()

        y_scroll = ttk.Scrollbar(frame, orient='vertical',command=frame.yview)
        x_scroll = ttk.Scrollbar(frame, orient='horizontal',command=frame.xview)
        frame['yscrollcommand'] = y_scroll.set
        frame['xscrollcommand'] = x_scroll.set
        frame.grid(column=0,row=0,sticky='nwes')
        x_scroll.grid(column=0, row=1,sticky='we')
        y_scroll.grid(column=1,row=0, columnspan=3,sticky='ns')
        frame.grid_columnconfigure(0,weight=1,minsize=450)
        frame.grid_rowconfigure(0,weight=1,minsize=300)

        #Create the Calculate button to execute the search
        filter_button = ttk.Button(mainframe, text="Filter", command=sort)
        list_button = ttk.Button(mainframe, text="List", command=list_home)

        #Create the labels for the respective rows
        ttk.Label(mainframe, text="Square Feet").grid(column=3, row=1, sticky=W)
        ttk.Label(mainframe, text="Bedrooms").grid(column=3, row=2, sticky=W)
        ttk.Label(mainframe, text="Bathrooms").grid(column=3, row=3, sticky=W)
        ttk.Label(mainframe, text="Your comparative assesment is").grid(column=1, row=4, sticky=E)
        filter_button.grid(column=3, row=5, sticky=W)
        list_button.grid(column=2, row=5, sticky=W)
        frame.grid(column=1, row=6, columnspan= 3, sticky=W)

        #Create buffers using child so it's not repeated
        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        #Put the focus on the Calculate button so a user doesn't have to use the curser
        feet_entry.focus()
        self.root.bind("<Return>", sort)

root = Tk()
HomeCompTool(root)
root.mainloop()
