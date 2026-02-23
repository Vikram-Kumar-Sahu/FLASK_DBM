import MySQLdb

try:
    db = MySQLdb.connect(
        host="localhost",
        user="root",
        passwd="vikram",
        db="student_portal"
    )
    print("✅ Password Correct — Connected Successfully")

except Exception as e:
    print("❌ Wrong Password")
    print(e)