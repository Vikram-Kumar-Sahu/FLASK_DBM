from flask import Blueprint, render_template, redirect, request, url_for
from flask_login import login_required, current_user
from app.models import User
from app import db

admin = Blueprint("admin", __name__)


@admin.route("/admin")
@login_required
def admin_panel():

    if current_user.role != "admin":
        return "Access Denied"

    users = User.query.filter_by(role="student").all()
    return render_template("admin.html", users=users)


@admin.route("/assign_grade/<int:user_id>", methods=["POST"])
@login_required
def assign_grade(user_id):

    if current_user.role != "admin":
        return "Access Denied"

    user = User.query.get(user_id)
    user.grade = request.form["grade"]
    db.session.commit()

    return redirect(url_for("admin.admin_panel"))