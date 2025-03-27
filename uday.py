from flask import Flask, render_template, request

app = Flask(__name__)  # Corrected from _name_ to __name__

def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"

@app.route("/", methods=["GET", "POST"])
def index():
    grade = None
    if request.method == "POST":
        try:
            marks = float(request.form.get("marks"))
            if 0 <= marks <= 100:
                grade = calculate_grade(marks)
            else:
                grade = "Invalid marks! Enter a value between 0 and 100."
        except ValueError:
            grade = "Please enter a valid number."
    return render_template("index.html", grade=grade)

if __name__ == "__main__":  # Corrected from _name_ to __name__
    app.run(debug=True)
