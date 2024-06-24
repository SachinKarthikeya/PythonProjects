import tkinter as tk
from tkinter import ttk

def get_input_fields():
    global height_label, height_entry, inches_label, inches_entry, weight_label, weight_entry

    if height_unit_choice.get() == 1:
        height_label.config(text="Height(feet):")
        inches_label.pack()
        inches_entry.pack()
        weight_label.config(text="Weight(pounds):")
    else:
        height_label.config(text="Height(cm):")
        inches_label.pack_forget()
        inches_entry.pack_forget()
        weight_label.config(text="Weight(kg):")

def calculate_bmi():
    try:
        if height_unit_choice.get() == 1:
            height_feet = float(height_entry.get())
            height_inches = float(inches_entry.get())
            weight = float(weight_entry.get())
            total_height = (height_feet * 12) + height_inches
            bmi_value = round(703 * (weight / (total_height ** 2)), 1)
        else:
            height_cm = float(height_entry.get())
            weight = float(weight_entry.get())
            bmi_value = round(weight / ((height_cm/100) ** 2), 1)
        
        bmi_result_label.config(text=f"BMI: {bmi_value} kg/m2")

        if bmi_value <= 18.4:
            bmi_category_label.config(text="You are underweight. We suggest you put on some weight.")
        elif 18.5 <= bmi_value <= 24.9:
            bmi_category_label.config(text="You are at a healthy weight for your height.")
        elif 25 <= bmi_value <= 29.9:
            bmi_category_label.config(text="You are slightly overweight. We suggest you lose some weight.")
        else:
            bmi_category_label.config(text="You are heavily overweight. Your health may be at risk if you do not lose weight!!")
    except ValueError:
        bmi_category_label.config(text="Error! Enter valid numeric height and weight values.")

window = tk.Tk()
window.title("BMI Calculator")
window.geometry("400x300")

style = ttk.Style()
style.configure("TLabel", font=("Arial", 12))
style.configure("TButton", font=("Arial", 12))

unit_frame = ttk.Frame(window)
unit_frame.pack(pady=10)

ttk.Label(unit_frame, text="Choose Unit System:", style='TLabel').pack()
height_unit_choice = tk.IntVar(value=2)  
ttk.Radiobutton(unit_frame, text="Imperial System", variable=height_unit_choice, value=1, command=get_input_fields).pack()
ttk.Radiobutton(unit_frame, text="Metric System", variable=height_unit_choice, value=2, command=get_input_fields).pack()

input_frame = ttk.Frame(window)
input_frame.pack(pady=10)

height_label = ttk.Label(input_frame, text="", style='TLabel')
height_label.pack()
height_entry = ttk.Entry(input_frame)
height_entry.pack()

inches_label = ttk.Label(window, text="Height(Inches):", style='TLabel')
inches_label.pack()
inches_entry = ttk.Entry(input_frame)
inches_entry.pack()

weight_label = ttk.Label(input_frame, text="", style='TLabel')
weight_label.pack()
weight_entry = ttk.Entry(input_frame)
weight_entry.pack()

ttk.Button(window, text="Calculate BMI", command=calculate_bmi, style='TButton').pack()

bmi_result_label = ttk.Label(window, text="", style='TLabel')
bmi_result_label.pack()

bmi_category_label = ttk.Label(window, text="", foreground="white", style='TLabel')
bmi_category_label.pack()

window.mainloop()