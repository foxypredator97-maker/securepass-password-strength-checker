import math
from flask import Flask, render_template, request
import re
import random
import string

def generate_password():

    characters = (
        string.ascii_letters +
        string.digits +
        "!@#$%^&*"
    )

    password = ''.join(
        random.choice(characters)
        for _ in range(12)
    )

    return password

app = Flask(__name__)

def check_password(password):

    score = 0
    feedback = []

    if len(password) >= 8:
        score += 20
    else:
        feedback.append("Use at least 8 characters")

    if re.search(r"[A-Z]", password):
        score += 20
    else:
        feedback.append("Add an uppercase letter")

    if re.search(r"[a-z]", password):
        score += 20
    else:
        feedback.append("Add a lowercase letter")

    if re.search(r"\d", password):
        score += 20
    else:
        feedback.append("Add a number")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 20
    else:
        feedback.append("Add a special character")

    if score <= 40:
        strength = "Weak"

    elif score <= 80:
        strength = "Medium"

    else:
        strength = "Strong"

    entropy = round(len(password) * math.log2(94), 2)

    return strength, score, feedback, entropy


@app.route("/", methods=["GET", "POST"])
def home():

    feedback = []
    entropy = 0
    color = "green"
    score = 0
    strength = ""

    if request.method == "POST":

        password = request.form["password"]

        strength, score, feedback, entropy = check_password(password)

        if strength == "Weak":
            color = "red"

        elif strength == "Medium":
            color = "orange"

        else:
            color = "green"

    return render_template(
        "index.html",
        strength=strength,
        score=score,
        color=color,
        feedback=feedback,
        entropy=entropy
    )


if __name__ == "__main__":
    app.run(debug=True)