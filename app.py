from flask import Flask, render_template, request, redirect, url_for, session
import requests

app = Flask(__name__)
app.secret_key = 'uhFTXm6dsOaX94H3K2QH0Q=='  

@app.route("/")
def hello_world():
    if 'testhead' not in session:
        return render_template("form.html")
    else:
        testhead = session['testhead']
        course_info = fetch_course_info(testhead)
        return render_template("index.html", course_info=course_info)

@app.route("/submit", methods=["POST"])
def submit_form():
    testhead = request.form.get("user_input")
    session['testhead'] = testhead
    return redirect(url_for("hello_world"))

def fetch_course_info(testhead):
    if not testhead:
        return None
    course_info = requests.get(
        "https://canvas.asu.edu/api/v1/courses?include[]=total_scores", 
        headers={"Authorization": f"Bearer {testhead}"}
    ).json()
    return course_info

if __name__ == "__main__":
    app.run(debug=True)