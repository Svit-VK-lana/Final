import os
import datetime
import sqlite3

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session

app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True

db = SQL("sqlite:///ords.db")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html")

@app.route("/work")
def work():
    return render_template("work.html")

    #  submission
@app.route("/order", methods=["GET", "POST"])
def order():
     if request.method == "POST":

        name = request.form.get("name")
        type = request.form.get("type")
        dedline = request.form.get("dedline")
        date = datetime.datetime.now()

        contact = request.form.get("contact")
        if not contact:
            return redirect("/no")
        comment = request.form.get("comment")
        db.execute("INSERT INTO orders (name, type, contact, date, dedline, comment) VALUES(?, ?, ?, ?, ?, ?)", name, type, contact, date, dedline, comment)
        return redirect("/yes")
     else:
         return render_template("order.html")

@app.route("/yes")
def yes():
     return render_template("yes.html")

@app.route("/no")
def no():
    return render_template("no.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/yyy", methods=["GET"])
def yyy():
    orders = db.execute("SELECT*FROM orders")
    return render_template("yyy.html",orders=orders)

if __name__ == "__main__":
    app.run(debug=True)
