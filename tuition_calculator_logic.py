# tuition_calculator_logic.py

def calculate_tuition(credits, orientation_fee, residency, level):
    """
    Function to calculate tuition based on the given inputs.

    Args:
    credits (int): Number of credits.
    orientation_fee (bool): Whether the student is charged the orientation fee.
    residency (str): Residency status of the student ("Resident" or "Nonresident").
    level (str): Level of the student ("Undergraduate" or "Graduate").

    Returns:
    float: The calculated total tuition cost.
    str: Error message if input is invalid.
    """
    try:
        if credits <= 0:
            return None, "Please enter a valid positive number of credits!"
        
        orientation_fee = 50 if orientation_fee else 0
        if level == "Undergraduate":
            if residency == "Resident":
                tuition_per_credit = 83
                non_resident_fee = 0
            else:
                tuition_per_credit = 111
                non_resident_fee = 1000
        else:
            if residency == "Resident":
                tuition_per_credit = 87.5
                non_resident_fee = 0
            else:
                tuition_per_credit = 121
                non_resident_fee = 1200

        total_cost = (tuition_per_credit * credits) + orientation_fee + non_resident_fee
        return total_cost, None  # No error message
    except Exception as e:
        return None, f"An error occurred: {str(e)}"
