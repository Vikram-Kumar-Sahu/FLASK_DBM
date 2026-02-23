from flask import Blueprint, render_template, redirect, request, flash, url_for
from flask_login import login_user, logout_user, login_required
from app.models import User
from app import db

auth = Blueprint("auth", __name__)

@auth.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        user = User(
            name=request.form["name"],
            email=request.form["email"]
        )
        user.set_password(request.form["password"])

        db.session.add(user)
        db.session.commit()

        flash("Account created successfully!", "success")
        return redirect(url_for("auth.login"))

    return render_template("signup.html")


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = User.query.filter_by(email=request.form["email"]).first()

        if user and user.check_password(request.form["password"]):
            login_user(user)

            # ✅ Role-based redirect
            if user.role == "admin":
                return redirect(url_for("admin.admin_panel"))
            else:
                return redirect(url_for("user.dashboard"))

        flash("Invalid credentials", "danger")

    return render_template("login.html")


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))