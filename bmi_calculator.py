import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        # Get user input
        name = name_entry.get()
        height = float(height_entry.get())
        weight = float(weight_entry.get())

        # Validate that height and weight are positive numbers
        if height <= 0 or weight <= 0:
            raise ValueError("Height and weight must be positive numbers.")

        # Calculate BMI
        bmi = weight / (height ** 2)
        bmi_category = ""
        advice = ""

        # Determine BMI category and provide recommendations
        if bmi < 18.5:
            bmi_category = "Underweight"
            advice = "It's important to eat a balanced diet and consult a healthcare provider for guidance."
        elif 18.5 <= bmi < 25:
            bmi_category = "Normal"
            advice = "Great job! Maintain a balanced diet and regular exercise."
        elif 25 <= bmi < 30:
            bmi_category = "Overweight"
            advice = "Consider a balanced diet and regular exercise. Consulting a healthcare provider is recommended."
        else:
            bmi_category = "Obese"
            advice = "It's advisable to consult a healthcare provider for a personalized plan."

        # Update the label with the result and advice
        bmi_label.config(text=f"{name}'s BMI is {bmi:.2f} ({bmi_category})")
        advice_label.config(text=advice)
        
        # Clear input fields after calculation
        name_entry.delete(0, tk.END)
        height_entry.delete(0, tk.END)
        weight_entry.delete(0, tk.END)

    except ValueError as e:
        # Show an error message if input is invalid
        messagebox.showerror("Input Error", str(e))

# Set up the main window
root = tk.Tk()
root.title("Hi! Welcome to your - BMI Calculator")

# Create labels and entry fields for user input
name_label = tk.Label(root, text="Name:")
name_entry = tk.Entry(root)

height_label = tk.Label(root, text="Height (m):")
height_entry = tk.Entry(root)

weight_label = tk.Label(root, text="Weight (kg):")
weight_entry = tk.Entry(root)

# Button to trigger BMI calculation
calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)

# Label to display the BMI result and advice
bmi_label = tk.Label(root, text="", font=("Arial", 14))
advice_label = tk.Label(root, text="", font=("Arial", 12), wraplength=300)

# Add some padding for better layout
for widget in [name_label, name_entry, height_label, height_entry, weight_label, weight_entry, calculate_button, bmi_label, advice_label]:
    widget.grid(padx=10, pady=5)

# Position elements in the grid
name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)
height_label.grid(row=1, column=0)
height_entry.grid(row=1, column=1)
weight_label.grid(row=2, column=0)
weight_entry.grid(row=2, column=1)
calculate_button.grid(row=3, column=0, columnspan=2)
bmi_label.grid(row=4, column=0, columnspan=2)
advice_label.grid(row=5, column=0, columnspan=2)

# Start the main event loop
root.mainloop()