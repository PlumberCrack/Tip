'''
(_  _) (  ) (  _ \      
  )(    )(   ) __/      
 (__)  (__) (__)        
'''
import tkinter as tk 
from tkinter import ttk
#Functions 
#-------------------------------------------------------
def function_15(): #15% Tip
    bill = total_entry.get()
    clean_bill = bill.replace('$', ' ')
    clean_bill_float = float(clean_bill)
    tip_bill = round(clean_bill_float * 0.15, 2)
    total = clean_bill_float + tip_bill
    tip_with_dollar = f"Your tip is: ${tip_bill:.2f}"
    total_with_dollar = f"Your total is: ${total:.2f}"
    tip_var.set(tip_with_dollar)
    total_var.set(total_with_dollar)
#-------------------------------------------------------
def function_20(): #20% Tip
    bill1 = total_entry.get()
    clean_bill1 = bill1.replace('$', ' ')
    clean_bill_float1 = float(clean_bill1)
    tip_bill1 = round(clean_bill_float1 * 0.20, 2)
    total1 = clean_bill_float1 + tip_bill1
    total1_with_dollar = f"Your total is: ${total1:.2f}"
    tip_with_dollar1 = f"Your tip is: ${tip_bill1:.2f}"
    tip_var.set(tip_with_dollar1)
    total_var.set(total1_with_dollar)
#-------------------------------------------------------
def function_25(): #25% Tip
    bill2 = total_entry.get()
    clean_bill2 = bill2.replace('$', ' ')
    clean_bill_float2 = float(clean_bill2)
    tip_bill2 = round(clean_bill_float2* 0.25, 2)
    total2 = clean_bill_float2 + tip_bill2
    tip_with_dollar2 = f"Your tip is: ${tip_bill2:.2f}"
    total2_with_dollar = f"Your total is: ${total2:.2f}"
    tip_var.set(tip_with_dollar2)
    total_var.set(total2_with_dollar)
#-------------------------------------------------------
def validate_input(text):
    try:
        float_value = float(text)
        formatted_value = f"${float_value:.2f}"
        total_entry.delete(0, tk.END)
        total_entry.insert(0, formatted_value)
        return True
    except ValueError:
        return False
#-------------------------------------------------------
#Window
window = tk.Tk()
window.title('To Insure Promptness')
window.geometry('400x250')
#-------------------------------------------------------
#Total entry 
entry_var = tk.StringVar()
total_entry = tk.Entry(window,text='Enter your total',validate='key')
total_entry.config(validatecommand=(total_entry.register(validate_input), '%P'))
total_entry.pack(padx=10)
#-------------------------------------------------------
#Tip buttons
#15%
button_15 = ttk.Radiobutton(window,
                       text='15%',
                       value='A',
                       command=function_15)
#-------------------------------------------------------
#20%
button_20 = ttk.Radiobutton(window,
                       text='20%',
                       value='B',
                       command=function_20)
#-------------------------------------------------------
#25%
button_25 = ttk.Radiobutton(window,
                       text='25%',
                       value='C',
                       command=function_25)
#-------------------------------------------------------
button_15.pack(side = 'bottom',pady=3)
button_20.pack(side = 'bottom',pady=3)
button_25.pack(side = 'bottom',pady=3)
#-------------------------------------------------------
#Tip
tip_var = tk.StringVar()
tip_label = ttk.Label(master = window,
                         font= 'Calibri 24 bold',
                         textvariable=tip_var
                        )
tip_label.pack(side='top' )
#Total + Tip 

total_var = tk.StringVar()
total_label  = ttk.Label(master = window,
                        font= 'Calibri 24 bold',
                        textvariable= total_var
                        )
total_label.pack(side='top' )
#Run
window.mainloop()
#By Custer 
