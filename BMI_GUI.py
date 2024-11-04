import tkinter as tk
from tkinter import messagebox

# Function to calculate BMI
def calculate_bmi():
    try:
        # Get user input
        height = int(entry_height.get())
        weight = int(entry_weight.get())
        
        # Convert height from cm to meters
        meter_height = height / 100.0
        
        # Calculate BMI
        bmi = weight / (meter_height ** 2)
        
        # Display the result in a message box
        messagebox.showinfo("BMI Result", f"Your BMI is: {bmi:.2f}")
    except ValueError:
        # Handle non-integer input
        messagebox.showerror("Input Error", "Please enter valid integer values for height and weight.")

# Set up the main window
window = tk.Tk()
window.title("BMI Calculator")

# Create labels and entry fields for height and weight
label_height = tk.Label(window, text="Height (cm):")
label_height.grid(row=0, column=0, padx=10, pady=10)
entry_height = tk.Entry(window)
entry_height.grid(row=0, column=1, padx=10, pady=10)

label_weight = tk.Label(window, text="Weight (kg):")
label_weight.grid(row=1, column=0, padx=10, pady=10)
entry_weight = tk.Entry(window)
entry_weight.grid(row=1, column=1, padx=10, pady=10)

# Create a calculate button
calculate_button = tk.Button(window, text="Calculate BMI", command=calculate_bmi)
calculate_button.grid(row=2, column=0, columnspan=2, pady=20)

# Run the Tkinter main loop
window.mainloop()
