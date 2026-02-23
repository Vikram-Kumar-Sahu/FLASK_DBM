from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user
from app import db, bcrypt

user = Blueprint("user", __name__)


@user.route("/")
def home():
    return redirect(url_for("auth.login"))


@user.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html", user=current_user)


@user.route("/grades")
@login_required
def grades():
    return render_template("grades.html", user=current_user)


@user.route("/profile", methods=["GET", "POST"])
@login_required
def profile():

    if request.method == "POST":
        current_user.name = request.form["name"]
        current_user.email = request.form["email"]
        db.session.commit()

    return render_template("profile.html", user=current_user)


# ✅ Password Reset Route
@user.route("/reset_password", methods=["POST"])
@login_required
def reset_password():

    new_password = request.form["password"]
    hashed_password = bcrypt.generate_password_hash(new_password).decode("utf-8")

    current_user.password = hashed_password
    db.session.commit()

    return redirect(url_for("user.profile"))