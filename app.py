
from flask import Flask, render_template, request, redirect, url_for, session, flash
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3


app = Flask(__name__)
app.secret_key = "your_secret_key_here"

def get_db_connection():
    conn = sqlite3.connect("expense_tracker.db")
    conn.row_factory = sqlite3.Row
    return conn

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function


@app.route("/")
def index():
    return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = get_db_connection()
        user = conn.execute(
            "SELECT * FROM users WHERE email = ?",
            (email,)
        ).fetchone()
        conn.close()

        if user and check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            session['user_name'] = user['name']
            return redirect(url_for('dashboard'))
        else:
            flash("Invalid email or password", "danger")

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        hashed_password = generate_password_hash(password)

        conn = get_db_connection()

        # check if email already exists
        existing_user = conn.execute(
            "SELECT * FROM users WHERE email = ?",
            (email,)
        ).fetchone()

        if existing_user:
            flash("Email already registered", "warning")
            conn.close()
            return redirect(url_for('register'))

        # insert new user
        conn.execute(
            "INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
            (name, email, hashed_password)
        )
        conn.commit()
        conn.close()

        flash("Registration successful! Please login.", "success")
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/dashboard')
@login_required
def dashboard():
    user_id = session['user_id']

    conn = get_db_connection()

    # total expenses
    total = conn.execute(
        "SELECT IFNULL(SUM(amount), 0) FROM expenses WHERE user_id = ?",
        (user_id,)
    ).fetchone()[0]

    # recent expenses
    expenses = conn.execute(
        """
        SELECT title, amount, category, expense_date
        FROM expenses
        WHERE user_id = ?
        ORDER BY expense_date DESC
        LIMIT 5
        """,
        (user_id,)
    ).fetchall()

    conn.close()

    return render_template(
        'dashboard.html',
        total=total,
        expenses=expenses,
        user_name=session.get('user_name')
    )

@app.route('/add-expense', methods=['GET', 'POST'])
@login_required
def add_expense():
    if request.method == 'POST':
        title = request.form['title']
        amount = request.form['amount']
        category = request.form['category']
        expense_date = request.form['expense_date']
        notes = request.form.get('notes')

        conn = get_db_connection()
        conn.execute(
    """
    INSERT INTO expenses
    (user_id, title, amount, category, expense_date, notes)
    VALUES (?, ?, ?, ?, ?, ?)
    """,
    (
        session['user_id'],
        title,
        amount,
        category,
        expense_date,
        notes
    )
)

        conn.commit()
        conn.close()

        flash("Expense added successfully!", "success")
        return redirect(url_for('dashboard'))

    return render_template('add_expense.html')

@app.route('/expenses')
@login_required
def expenses():
    conn = get_db_connection()

    user_expenses = conn.execute(
        """
        SELECT id, title, amount, category, expense_date, notes
        FROM expenses
        WHERE user_id = ?
        ORDER BY expense_date DESC
        """,
        (session['user_id'],)
    ).fetchall()

    conn.close()

    return render_template('expenses.html', expenses=user_expenses)

@app.route('/logout')
@login_required
def logout():
    session.clear()   # removes all session data
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

