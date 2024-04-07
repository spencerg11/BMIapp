def calculate_bmi(height_feet, height_inches, weight_pounds):

    height_total_inches = (height_feet * 12) + height_inches
    bmi = ((weight_pounds * 0.45) / ((height_total_inches * 0.025) ** 2))
    return bmi

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"
