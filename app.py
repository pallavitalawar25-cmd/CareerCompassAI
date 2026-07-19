from flask import Flask, render_template, request, session, redirect
from opt_mapper import trait_map, gemini_prompt
from gemini_api import generate_report
import json
app = Flask(__name__)
app.secret_key = "careercompass_secret"


# ---------------- HOME ---------------- #

@app.route("/")
def home():
    return render_template("index.html")


# ---------------- PERSONAL DETAILS ---------------- #

@app.route("/personal", methods=["GET", "POST"])
def personal():

    if request.method == "POST":

        # Clear old session data
        session.clear()

        # Store new user's details
        session["fullname"] = request.form["fullname"]
        session["age"] = request.form["age"]
        session["education"] = request.form["education"]
        session["cgpa"] = request.form["cgpa"]
        session["state"] = request.form["state"]
        session["district"] = request.form["district"]

        print("\n===== PERSONAL DETAILS =====")
        for key, value in session.items():
            print(f"{key}: {value}")

        return redirect("/interests")

    return render_template("personal.html")


# ---------------- INTERESTS ---------------- #

@app.route("/interests", methods=["GET", "POST"])
def interests():

    if request.method == "POST":

        session["interests"] = request.form.getlist("interests")

        print("\n===== INTERESTS =====")
        print(session["interests"])

        return redirect("/strengths")

    return render_template("interests.html")


# ---------------- STRENGTHS ---------------- #

@app.route("/strengths", methods=["GET", "POST"])
def strengths():

    if request.method == "POST":

        session["strengths"] = request.form.getlist("strengths")

        print("\n===== STRENGTHS =====")
        print(session["strengths"])

        return redirect("/tech_skills")

    return render_template("strengths.html")


# ---------------- TECHNICAL SKILLS ---------------- #

@app.route("/tech_skills", methods=["GET", "POST"])
def tech_skills():

    if request.method == "POST":

        session["tech_skills"] = request.form.getlist("tech_skills")

        print("\n===== TECH SKILLS =====")
        print(session["tech_skills"])

        return redirect("/skills_to_develop")

    return render_template("tech_skills.html")


# ---------------- AREAS OF GROWTH ---------------- #

@app.route("/skills_to_develop", methods=["GET", "POST"])
def skills_to_develop():

    if request.method == "POST":

        session["skills_to_develop"] = request.form.getlist("skills_to_develop")
        session["improveSkill"] = request.form.get("improveSkill")

        print("\n===== AREAS OF GROWTH =====")
        print(session["skills_to_develop"])
        print("Focus Skill :", session["improveSkill"])

        return redirect("/aptitude")

    return render_template("skills_to_develop.html")


# ---------------- APTITUDE ---------------- #

@app.route("/aptitude", methods=["GET", "POST"])
def aptitude():

    if request.method == "POST":

        # Save MCQ answers
        for i in range(1, 20):
            session[f"q{i}"] = request.form.get(f"q{i}")

        # Save descriptive answer
        session["q20"] = request.form.get("q20")

        print("\n===== APTITUDE ANSWERS =====")

        for i in range(1, 20):
            print(f"Q{i}: {session.get(f'q{i}')}")

        print("Q20:", session.get("q20"))

        return redirect("/report")

    return render_template("aptitude.html")


# ---------------- REPORT ---------------- #

@app.route("/report")
def report():

    mapped_traits = []

    # Convert answers into traits
    for i in range(1, 20):

        question = f"q{i}"
        option = session.get(question)

        mapped_traits.extend(
            trait_map.get(question, {}).get(option, [])
        )

    q20_answer = session.get("q20")

    print("\n==============================")
    print("MAPPED TRAITS")
    print("==============================")

    for trait in mapped_traits:
        print("-", trait)

    print("\nQ20 ANSWER")
    print(q20_answer)

    # Entire profile (this is what Gemini will receive later)
    user_profile = {

        "personal_details": {
            "name": session.get("fullname"),
            "age": session.get("age"),
            "education": session.get("education"),
            "cgpa": session.get("cgpa"),
            "state": session.get("state"),
            "district": session.get("district")
        },

        "interests": session.get("interests"),

        "strengths": session.get("strengths"),

        "technical_skills": session.get("tech_skills"),

        "areas_to_improve": session.get("skills_to_develop"),

        "priority_skill": session.get("improveSkill"),

        "mapped_traits": mapped_traits,

        "descriptive_answer": q20_answer

    }

    print("\n==============================")
    print("USER PROFILE TO SEND TO GEMINI")
    print("==============================")
    print(user_profile)

    prompt = f"""
    {gemini_prompt}

    User Profile:
    {user_profile}
    """

    ai_report = generate_report(prompt)
    print(type(ai_report))
    print(ai_report)

# Remove markdown if Gemini returns it
    ai_report = ai_report.replace("```json", "")
    ai_report = ai_report.replace("```", "")
    ai_report = ai_report.strip()

# Convert JSON string to Python dictionary
    ai_report = json.loads(ai_report)

    print("\n==============================")
    print("GEMINI REPORT")
    print("==============================")
    print(ai_report)    

    return render_template(
    "report.html",
    profile=user_profile,
    report=ai_report
    )


if __name__ == "__main__":
    app.run(debug=True)