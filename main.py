import csv
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
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
        self.meters = StringVar()
        ttk.Label(mainframe, textvariable=self.meters).grid(column=2, row=4, sticky=(W, E))

        #Create a frame inside the dialog window
        #frame = ttk.Frame(mainframe, borderwidth=7, relief="ridge", width=400,height=300)
        frame = Text(mainframe,state='disabled',wrap='none')
        frame.grid()

        def write_to_log(msg):
            """_summary_

            Args:
                msg (_type_): _description_
            """
            numlines = int(frame.index('end - 1 line').split('.')[0])
            frame['state'] = 'normal'
            #if numlines>30:
                #frame.delete(0.0,'end')
            if frame.index('end-1c')!='1.0':
                frame.insert('end', '\n')
            frame.insert('end', msg)
            frame['state'] = 'disabled'

        def list_home():
            """_summary_
            """
            with open('titles.csv', 'r') as homefile:
                for line in csv.DictReader(homefile): # DictReader is a reader that returns a dictionary from the source.
                    for key in line:
                        write_to_log(key)
                        write_to_log(line[key]) #Returns all the keys and values in the csv file.

        ys = ttk.Scrollbar(frame, orient='vertical',command=frame.yview)
        xs = ttk.Scrollbar(frame, orient='horizontal',command=frame.xview)
        frame['yscrollcommand'] = ys.set
        frame['xscrollcommand'] = xs.set
        frame.grid(column=0,row=0,sticky='nwes')
        xs.grid(column=0, row=1,sticky='we')
        ys.grid(column=1,row=0, columnspan=3,sticky='ns')
        frame.grid_columnconfigure(0,weight=1,minsize=1000)
        frame.grid_rowconfigure(0,weight=1,minsize=300)

        #Create the Calculate button to execute the search
        filter_button = ttk.Button(mainframe, text="Filter", command=self.sort)
        list_button = ttk.Button(mainframe, text="List", command=list_home)

        #Create the labels for the respective rows
        ttk.Label(mainframe, text="Square Feet").grid(column=3, row=1, sticky=W)
        ttk.Label(mainframe, text="Bedrooms").grid(column=3, row=2, sticky=W)
        ttk.Label(mainframe, text="Bathrooms").grid(column=3, row=3, sticky=W)
        ttk.Label(mainframe, text="Your Selection has").grid(column=1, row=4, sticky=E)
        ttk.Label(mainframe, text="Comps").grid(column=3, row=4, sticky=W)
        filter_button.grid(column=3, row=5, sticky=W)
        list_button.grid(column=2, row=5, sticky=W)
        frame.grid(column=1, row=6, columnspan= 3, sticky=W)

        #Create buffers using child so it's not repeated
        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        #Put the focus on the Calculate button so a user doesn't have to use the curser
        feet_entry.focus()
        root.bind("<Return>", self.sort)



    def sort(self, *args):
        """Get User Inputs and look for comps
        """
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