import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from singular import *

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/", methods=["GET", "POST"])
def index():
    # TODO: Add the user's entry into the database
    # Check if ID comes in the form. If doesn`t, it is a insert
    if request.method == "POST":
        palavra = request.form.get('palavra', type=str)
        singular = singularizar(palavra)
        return render_template("index.html", palavra=palavra, singular=singular)
    return render_template("index.html", palavra="palavra", singular="singular")

