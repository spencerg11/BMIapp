from flask import Flask, request, redirect
from processing import calculate_bmi, get_bmi_category

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=["GET", "POST"])
def calculate_page():
    errors = ""
    result = ""
    if request.method == "POST":
        weight = request.form["Weight_in_Lbs"]
        feet = request.form["Height_in_Feet"]
        inches = request.form["Inches"]

        if not weight.isnumeric():
            errors += "<p>Weight must be a number.</p>\n"
        elif not feet.isnumeric():
            errors += "<p>Height in feet must be a number.</p>\n"
        elif not inches.isnumeric():
            errors += "<p>Inches must be a number.</p>\n"
        else:
            weight = float(weight)
            feet = float(feet)
            inches = float(inches)
            bmi = calculate_bmi(feet, inches, weight)
            category = get_bmi_category(bmi)
            result = f'<p>Your BMI is {bmi:.2f}, which falls into the category of {category}</p>'

    return '''
        <html>
            <body>
                <p> Enter the following information:</p>
                <form method="post" action=".">
                    <p><label for="Weight_in_Lbs">Weight in Lbs:</label> <input type="text" name="Weight_in_Lbs" id="Weight_in_Lbs"></p>
                    <p><label for="Height_in_Feet">Height in Feet:</label> <input type="text" name="Height_in_Feet" id="Height_in_Feet"></p>
                    <p><label for="Inches">Inches:</label> <input type="text" name="Inches" id="Inches"></p>
                    <p><input type="submit" value="Calculate BMI" /></p>
                </form>
                {result}
                {errors}
            </body>
        </html>
    '''.format(result=result, errors=errors)

if __name__ == "__main__":
    app.run()

