# tuition_calculator_ui.py
import customtkinter as ctk
from tuition_calculator_logic import calculate_tuition

# Function to handle the button click event and update the result
def on_calculate_button_click():
    credits = credits_entry.get()
    try:
        # Ensure the user input is a valid positive integer
        credits = int(credits)
        
        if credits <= 0:
            result_label.configure(text="Please enter a valid positive number of credits!", fg_color="red")
            return
        
        orientation_fee = orientation_var.get()
        residency = residency_var.get()
        level = level_var.get()

        total_cost, error_message = calculate_tuition(credits, orientation_fee, residency, level)

        if error_message:
            result_label.configure(text=error_message, fg_color="red")
        else:
            formatted_cost = format_currency(total_cost)  # Format the result
            result_label.configure(text=f"Total Tuition Cost: {formatted_cost}", fg_color="#1E3A8A")
    except ValueError:
        result_label.configure(text="Please enter a valid number of credits!", fg_color="red")
    except Exception as e:
        result_label.configure(text=f"Error: {str(e)}", fg_color="red")

# Function to format the tuition cost to a readable currency format
def format_currency(value):
    return f"${value:,.2f}"

# Function to reset all inputs and results
def on_reset_button_click():
    credits_entry.delete(0, ctk.END)
    orientation_var.set(False)
    residency_var.set("Resident")
    level_var.set("Undergraduate")
    result_label.configure(text="Total Tuition Cost: $0.00", fg_color="#1E3A8A")

# Configure main window
ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("blue")  

root = ctk.CTk()
root.title("College Tuition Calculator")
root.geometry("600x450")

# Heading
heading = ctk.CTkLabel(root, text="College Tuition Calculator", font=("Arial", 20, "bold"))
heading.pack(pady=10)

# Input Section
frame = ctk.CTkFrame(root, corner_radius=10)
frame.pack(pady=5, padx=10, fill="both", expand=True)

credits_label = ctk.CTkLabel(frame, text="Number of Credits:", font=("Arial", 14))
credits_label.grid(row=0, column=0, pady=5, padx=5, sticky="w")
credits_entry = ctk.CTkEntry(frame, placeholder_text="Enter credits")
credits_entry.grid(row=0, column=1, pady=5, padx=5)

orientation_var = ctk.BooleanVar()
orientation_check = ctk.CTkCheckBox(frame, text="New Student Orientation Fee ($50)", variable=orientation_var)
orientation_check.grid(row=1, columnspan=2, pady=5, padx=5, sticky="w")

# Residency Section
residency_label = ctk.CTkLabel(frame, text="Residency:", font=("Arial", 14))
residency_label.grid(row=2, column=0, pady=5, padx=5, sticky="w")
residency_var = ctk.StringVar(value="Resident")
resident_button = ctk.CTkRadioButton(frame, text="Resident", variable=residency_var, value="Resident")
nonresident_button = ctk.CTkRadioButton(frame, text="Nonresident", variable=residency_var, value="Nonresident")
resident_button.grid(row=2, column=1, sticky="w")
nonresident_button.grid(row=3, column=1, sticky="w")

# Level Section
level_label = ctk.CTkLabel(frame, text="Level:", font=("Arial", 14))
level_label.grid(row=4, column=0, pady=5, padx=5, sticky="w")
level_var = ctk.StringVar(value="Undergraduate")
undergraduate_button = ctk.CTkRadioButton(frame, text="Undergraduate", variable=level_var, value="Undergraduate")
graduate_button = ctk.CTkRadioButton(frame, text="Graduate", variable=level_var, value="Graduate")
undergraduate_button.grid(row=4, column=1, sticky="w")
graduate_button.grid(row=5, column=1, sticky="w")

# Calculate Button
calculate_button = ctk.CTkButton(root, text="Calculate Tuition", command=on_calculate_button_click)
calculate_button.pack(pady=5)

# Reset Button
reset_button = ctk.CTkButton(root, text="Reset", command=on_reset_button_click)
reset_button.pack(pady=5)

# Result Section
result_label = ctk.CTkLabel(
    root, 
    text="Total Tuition Cost: $0.00", 
    font=("Arial", 16, "bold"),  
    fg_color="#1E3A8A",  
    text_color="white",  
    corner_radius=10,  
    height=50  
)
result_label.pack(pady=10, padx=10, fill="x")

# Run the application
root.mainloop()
