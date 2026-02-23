import MySQLdb

# MySQL Connection
connection = MySQLdb.connect(
    host='localhost',
    user='root',
    password='vikram',
    database='student_portal'
)

cursor = connection.cursor()

# Create admin user
admin_data = (
    "Admin",
    "admin@gmail.com",
    "admin123",
    "admin"
)

# Insert admin user (make sure your users table has a 'role' column)
try:
    cursor.execute("INSERT INTO users(name,email,password,role) VALUES(%s,%s,%s,%s)", admin_data)
    connection.commit()
    print("Admin Created Successfully!")
except Exception as e:
    print(f"Error: {e}")
    # If role column doesn't exist, try without it
    try:
        cursor.execute("INSERT INTO users(name,email,password) VALUES(%s,%s,%s)", admin_data[:-1])
        connection.commit()
        print("Admin Created Successfully (without role)!")
    except Exception as e2:
        print(f"Error: {e2}")
finally:
    cursor.close()
    connection.close()
