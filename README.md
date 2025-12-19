💰 Expense Tracker – Flask Web Application
A simple and secure Expense Tracker Web Application built using Flask, SQLite, Bootstrap, HTML, CSS, and Python.
This project helps users manage daily expenses, track spending, and view expense history in an organized way.

🚀 Features
•	🔐 User Authentication (Register / Login / Logout)
•	➕ Add Expenses
•	📋 View All Expenses
•	📊 Dashboard with Total Expenses
•	🗂 Category-wise Expense Tracking
•	🔒 Secure Password Hashing
•	🎨 Responsive UI using Bootstrap
•	🗄 SQLite Database

Technology	Usage:
Python	Backend logic
Flask	Web framework
SQLite	Database
HTML	Page structure
CSS	Styling
Bootstrap 5	Responsive UI
Werkzeug	Password hashing

📁 Project Structure:
```
expense-tracker/
│
├── app.py
├── expense_tracker.db
│
├── static/
│   └── css/
│       └── style.css
│
├── templates/
│   ├── layout.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── add_expense.html
│   └── expenses.html
│
└── README.md
```

⚙️ Installation & Setup:
1️⃣ Clone the Repository
git clone https://github.com/skferoz7/Expense-Tracker.git
cd expense-tracker

2️⃣ Create Virtual Environment (Optional but Recommended)
python -m venv venv
source venv/bin/activate    # Linux / Mac
venv\Scripts\activate       # Windows

3️⃣ Install Dependencies
pip install flask werkzeug
Or using requirements file:
pip install -r requirements.txt
________________________________________
▶️ Run the Application
python app.py
Open browser and visit:
http://127.0.0.1:5000/
________________________________________
🗄 Database Schema
Users Table:
Column	Type
id	Integer (PK)
name	Text
email	Text (Unique)
password	Text (Hashed)
created_at	DateTime

Expenses Table:
Column	Type
id	Integer (PK)
user_id	Integer (FK)
title	Text
amount	Real
category	Text
expense_date	Date
notes	Text
created_at	DateTime

🔐 Security Features

Passwords stored using hashed encryption

Session-based authentication

Protected routes using login_required decorator

SQL Injection prevention using parameterized queries

📸 Pages in my web application

Login Page

Register Page

Dashboard

Add Expense

Expenses List:

📈 Future Enhancements

📊 Charts & Graphs

✏️ Edit / Delete Expenses

📆 Monthly Reports

📱 Mobile Optimizations

👨‍💻 Author:

Shaik Feroz
B.Tech – Computer Science
📍 Hyderabad, India

GitHub: https://github.com/skferoz7

LinkedIn: https://www.linkedin.com/in/feroz-shaik-9b228a25b/

⭐ Support

If you like this project, please ⭐ the repository and feel free to contribute or suggest improvements.


