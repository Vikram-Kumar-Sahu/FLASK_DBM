from flask import Flask, render_template, request, redirect, session
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = "secretkey"

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'vikram'
app.config['MYSQL_DB'] = 'student_portal'

mysql = MySQL(app)

@app.route('/')
def index():
    if 'user_id' in session:
        return redirect('/dashboard')
    return redirect('/login')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(name,email,password) VALUES(%s,%s,%s)",
                    (name, email, password))
        mysql.connection.commit()
        cur.close()

        return redirect('/login')

    return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE email=%s AND password=%s",
                    (email, password))
        user = cur.fetchone()

        if user:
            session['user_id'] = user[0]
            return redirect('/dashboard')
        else:
            return "Invalid Credentials"

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' in session:
        return render_template('dashboard.html')
    return redirect('/login')

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if 'user_id' in session:
        cur = mysql.connection.cursor()

        if request.method == 'POST':
            name = request.form['name']
            cur.execute("UPDATE users SET name=%s WHERE id=%s",
                        (name, session['user_id']))
            mysql.connection.commit()

        cur.execute("SELECT * FROM users WHERE id=%s",
                    (session['user_id'],))
        user = cur.fetchone()

        return render_template('profile.html', user=user)

    return redirect('/login')

@app.route('/reset', methods=['POST'])
def reset():
    if 'user_id' in session:
        new_password = request.form['password']

        cur = mysql.connection.cursor()
        cur.execute("UPDATE users SET password=%s WHERE id=%s",
                    (new_password, session['user_id']))
        mysql.connection.commit()
        cur.close()

        return redirect('/dashboard')
    return redirect('/login')
    
@app.route('/grades')
def grades():
    if 'user_id' in session:
        cur = mysql.connection.cursor()
        cur.execute("SELECT grade FROM users WHERE id=%s",
                    (session['user_id'],))
        grade = cur.fetchone()
        cur.close()

        return render_template('grades.html', grade=grade)

    return redirect('/login')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

if __name__ == "__main__":
    app.run(debug=True)