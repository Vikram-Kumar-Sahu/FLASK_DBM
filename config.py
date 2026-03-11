import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")
    # MySQL Database Configuration (@ in password encoded as %40)
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:vikram@localhost/student_portal"
    SQLALCHEMY_TRACK_MODIFICATIONS = False