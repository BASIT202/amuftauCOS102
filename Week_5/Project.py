import pandas as pd
from tkinter import *

# Load the dataset
employees = pd.read_csv('GIG-logistics.csv')

# Function to check employee and display details
def check_employee():
    name = name_entry.get().strip()
    department = department_entry.get().strip()
    
    employee_data = employees[(employees['SURNAME'] == name) & (employees['DEPARTMENT'] == department)]

    if not employee_data.empty:
        welcome_label.config(text=f"Welcome {name} from {department} department!")
        members = employees.loc[employees['DEPARTMENT'] == department, 'SURNAME'].tolist()
        members.remove(name)
        members_label.config(text=f"Other members in {department} department:\n" + "\n".join(members))
    else:
        welcome_label.config(text="Employee does not exist.")

# GUI setup
root = Tk()
root.title("GIG Logistics Employee Checker")
root.geometry("500x300")

Label(root, text="Name:").grid(row=0, column=0)
name_entry = Entry(root)
name_entry.grid(row=0, column=1)

Label(root, text="Department:").grid(row=1, column=0)
department_entry = Entry(root)
department_entry.grid(row=1, column=1)

Button(root, text="Check Employee", command=check_employee).grid(row=2, column=0, columnspan=2)

welcome_label = Label(root, text="")
welcome_label.grid(row=3, column=0, columnspan=2)

members_label = Label(root, text="")
members_label.grid(row=4, column=0, columnspan=2)

root.mainloop()
