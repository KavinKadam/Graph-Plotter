# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import csv
from tkinter import *
from tkinter import filedialog
from pandas import *

# Opens a GUI to select your file; only allows you to select CSV files


def browseFiles():
    global filename
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a CSV File",
                                          filetypes = (("CSV files",
                                                        "*.CSV*"),
                                                       ("all files",
                                                        "*.*")))
    file=open(filename, 'r')
    print(file.read())
    file.close()

    # Change label contents
    label_file_explorer.configure(text="File Opened: "+ filename)
      
      
                                                                                                  
# Create the root window
window = Tk()
# Set window title
window.title('File Explorer')  
# Set window size
window.geometry("500x500")  
#Set window background color
window.config(background = "white")
# Create a File Explorer label
label_file_explorer = Label(window,
                            text = "File Explorer",
                            width = 100, height = 4,
                            fg = "blue")     
button_explore = Button(window,
                        text = "Browse Files",
                        command = browseFiles) 
button_exit = Button(window,
                     text = "Exit",
                     command = exit)
  
# Grid method is chosen for placing
# the widgets at respective positions
# in a table like structure by
# specifying rows and columns
label_file_explorer.grid(column = 1, row = 1) 
button_explore.grid(column = 1, row = 2)
button_exit.grid(column = 1,row = 3)
# Let the window wait for any events
window.mainloop()

# Checks through your CSV data to ensure it has been formatted correctly, prints err otherwise
# Currently uncoded since the default GUI selection filetype is CSV, so it would be redundant.

# Checks absolutely nothing. This is a meaningless comment.

# Reads the CSV you have selected
file=open(filename, 'r')
listmaker=csv.DictReader(file)

# Creates empty lists for graphing stages
time = []
voltage = []
current = []
 
# iterating over each row and append
# values to empty list
for col in listmaker:
   time.append(col['time'])
   voltage.append(col['voltage'])
   current.append(col['current'])
 
# printing lists
print('Time:', time)
print('Voltage:', voltage)
print('Current:', current)
# reading CSV file


