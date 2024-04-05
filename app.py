from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    if request.method == 'POST':
        height = float(request.form['height'])
        weight = float(request.form['weight'])
        bmi = calculate_bmi(height, weight)
        return render_template('result.html', bmi=bmi)

def calculate_bmi(height, weight):
    return weight / (height / 100) ** 2

if __name__ == '__main__':
    app.run(debug=True)

