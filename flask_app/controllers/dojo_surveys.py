from flask_app import app
from flask import redirect, render_template, request, session
from flask_app.models.dojo_survey import Ninja
from flask_app.env import Key
app.secret_key = Key

@app.route("/")
def survey():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def submit():
    if not Ninja.validate_ninja(request.form):
        return redirect("/")
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect("/info")


@app.route("/info")
def info():
    return render_template("/info.html")

@app.route("/back")
def restart():
    return redirect("/")