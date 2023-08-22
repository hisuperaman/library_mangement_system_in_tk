import csv
import pandas as pd
import os
from tkinter import filedialog
from tkinter import messagebox

def saveBtnClick(win, heading, rows, filename):
    # asking path and filename
    path_filename = filedialog.asksaveasfilename(filetypes=[("Excel File", ".xlsx")], defaultextension=".xlsx", initialfile=filename)

    # writing data in csv
    if len(path_filename)!=0:
      with open("temp.csv", "w", newline="") as f:
        my_csv = csv.writer(f)
        my_csv.writerow(heading)
        my_csv.writerows(rows)
        
      # loading csv as dataframe
      df = pd.read_csv("temp.csv")
      # creating a new excel file
      resultExcel = pd.ExcelWriter(f"{path_filename}")
      # converting dataframe to excel file and saving data in the excel file created earlier
      df.to_excel(resultExcel, sheet_name='mysheet', index=False)

      # changing column width of excel file
      resultExcel.sheets['mysheet'].set_column(0, len(heading)-1, 15)

      resultExcel.close()
      # removing temporary csv file
      os.remove("temp.csv")
      messagebox.showinfo("Saved", f"Saved as {path_filename}", parent=win)
      win.destroy()