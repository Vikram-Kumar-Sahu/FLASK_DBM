from app import db, bcrypt
from flask_login import UserMixin
from app import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), default="student")
    grade = db.Column(db.String(50), default="Not Assigned")
    subject1_name = db.Column(db.String(50), default="Subject 1")
    subject1_marks = db.Column(db.Float, default=0.0)
    subject2_name = db.Column(db.String(50), default="Subject 2")
    subject2_marks = db.Column(db.Float, default=0.0)
    subject3_name = db.Column(db.String(50), default="Subject 3")
    subject3_marks = db.Column(db.Float, default=0.0)
    subject4_name = db.Column(db.String(50), default="Subject 4")
    subject4_marks = db.Column(db.Float, default=0.0)
    subject5_name = db.Column(db.String(50), default="Subject 5")
    subject5_marks = db.Column(db.Float, default=0.0)

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)