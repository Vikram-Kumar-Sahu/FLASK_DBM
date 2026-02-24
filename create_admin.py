from app import db, bcrypt
from app.models import User
from run import app

# Create admin user
admin_user = User(
    name="Admin",
    email="admin@gmail.com",
    role="admin"
)
admin_user.set_password("admin123")

try:
    with app.app_context():
        # Check if admin already exists
        existing_admin = User.query.filter_by(email="admin@gmail.com").first()
        if existing_admin:
            print("Admin user already exists!")
        else:
            db.session.add(admin_user)
            db.session.commit()
            print("Admin Created Successfully!")
except Exception as e:
    print(f"Error: {e}")
    try:
        db.session.rollback()
    except:
        pass
