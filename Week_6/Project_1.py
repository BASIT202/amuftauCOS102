import tkinter as tk
from tkinter import messagebox

def button_lekki():
    #create lekki sub window
    lekki = tk.Toplevel(root)
    lekki.geometry("300x100")

    #create widgets
    label_1=tk.Label(lekki,text='Enter the weight(in Kg):')
    label_1.pack()
    label1_entry=tk.Entry(lekki)
    label1_entry.pack()

    #create submit button
    submit=tk.Button(lekki,text='Calculate Amount',command=lambda:weight_checker(label1_entry))
    submit.pack()

def weight_checker(entry_widget):
    weight=entry_widget.get()
    if float(weight) >= 10 :
        total_amount1(weight)
    else:
        total_amount2(weight)    


def total_amount1(weight):
    amount=tk.Toplevel()
    amount.title('Total Cost')
    amount.geometry("300x100")
    label_2=tk.Label(amount,text="Your total amount is 3500 Naira ")
    label_2.pack()
    return

def total_amount2(weight):
    amount=tk.Toplevel()
    amount.title('Total Cost')
    amount.geometry("300x100")
    label_2=tk.Label(amount,text="Your total amount is 5000 Naira ")
    label_2.pack()
    return

def button_Epe():
    #create epe sub window
    Epe = tk.Toplevel(root)
    Epe.geometry("300x100")

    #craete widgets
    label_3=tk.Label(Epe,text='Enter the weight(in Kg):')
    label_3.pack()
    label3_entry=tk.Entry(Epe)
    label3_entry.pack()

    #create submit button
    summit=tk.Button(Epe,text='Calculate Amount',command=lambda:weight_checker2(label3_entry))
    summit.pack()
    return


def weight_checker2(entry_widget):
    weight=entry_widget.get()
    if float(weight) >= 10 :
        total_amount4(weight)
    else:
        total_amount3(weight)    


def total_amount3(weight):
    amount=tk.Toplevel()
    amount.title('Total Cost')
    amount.geometry("300x100")
    label_3=tk.Label(amount,text="Your total amount is 5000 Naira ")
    label_3.pack()
    return

def total_amount4(weight):
    amount=tk.Toplevel()
    amount.title('Total Cost')
    amount.geometry("300x100")
    label_4=tk.Label(amount,text="Your total amount is 10000 Naira ")
    label_4.pack()
    return

#Main wndow
root = tk.Tk()
root.title('Welcome to Simi Services')
root.geometry("300x100")

#create widget
label=tk.Label(root,text="Please select location")
label.pack()

#create button1
button_1=tk.Button(root,text='Ibeju-Lekki',command=button_lekki)
button_1.pack()

#create button2
button_2=tk.Button(root,text='Epe',command=button_Epe)
button_2.pack()

root.mainloop()

    