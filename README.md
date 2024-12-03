# College Tuition Calculator

This project is a simple college tuition calculator built using Python and the **CustomTkinter** library. It allows users to calculate the total tuition cost based on their residency, student level (Undergraduate/Graduate), the number of credits, and whether they are being charged an orientation fee.

## Features

- Calculate tuition based on:
  - Residency status (Resident or Nonresident)
  - Student level (Undergraduate or Graduate)
  - Number of credits
  - Optional $50 orientation fee for new students
  - Nonresident fee for nonresident students
- Displays the calculated tuition cost in a user-friendly interface.

## Project Structure

your_project/ 
├── tuition_calculator_logic.py # Logic for calculating tuition costs 
├── tuition_calculator_ui.py # Graphical user interface using CustomTkinter 
├── main.py # Entry point for running the application 
└── README.md # This file


### Files Overview:
- **`tuition_calculator_logic.py`**: Contains the logic to calculate the tuition cost based on inputs such as credits, residency status, student level, and orientation fee.
- **`tuition_calculator_ui.py`**: Defines the graphical user interface (GUI) using CustomTkinter, allowing users to input their information and display results.
- **`main.py`**: The entry point to run the application. It imports the UI and launches the application window.

## Requirements

This project uses **Python** and the **CustomTkinter** library. To run it, you need to have Python installed on your machine.

### Install Dependencies

First, install the required dependencies by running:

```bash
pip install customtkinter
```

## Running the Application
Clone or download this repository to your local machine.

Navigate to the project directory.

Run the main.py file using the command:

```bash
python main.py
```
This will launch the college tuition calculator application in a new window.

## How to Use
Enter the number of credits in the provided input field.
Select your student level (Undergraduate or Graduate).
Select your residency status (Resident or Nonresident).
Check the option for the orientation fee if you're a new student.
Click the "Calculate Tuition" button to see the total tuition cost.
The result will be displayed below the button with the total cost, including any applicable fees.
