from Tkinter import *
import tkFileDialog as filedialog
import csv
import pandas as pd

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = filedialog.askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(filename)

# can check with if/else if it's a CSV otherwise error or something to UI
df = pd.read_csv(filename, header=None)
print(df)
# with open(filename) as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_numbers = 0
#     for row in csv_reader:
#         if (line_numbers != 0):
#             print(row[0] + " line numbers are: " + str(line_numbers))
#             line_numbers+=1
