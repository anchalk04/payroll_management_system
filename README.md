# 💼 Payroll Management System

A simple Django-based web application to manage employees and generate payslips.

---

## 🚀 Features

- 👨‍💼 Employee management (add, list employees)
- 💰 Payroll calculation and payslip generation
- 🧮 Automatic deductions and net pay computation
- 🎨 Clean, responsive UI for Employees and Payroll pages
- 🔐 Modular Django app structure (accounts, employees, payroll)

---

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS
- **Database:** SQLite3 (default Django DB)
- **Environment:** Virtualenv / venv

---

## ⚙️ Installation Guide

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/payroll-web.git
cd payroll-web
```
### 2️⃣ Create and Activate Virtual Environment
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Mac/Linux
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run Migrations
```bash
python manage.py migrate
```

### 5️⃣ Start the Development Server
```bash
python manage.py runserver
```

#### Then open your browser and go to:
👉 http://127.0.0.1:8000/

### 🧩 App Structure
payroll-web/
│
├── accounts/        # Authentication (if added)
├── employees/       # Employee management
├── payroll/         # Payroll & payslips
├── payroll_site/    # Main project settings
│
├── templates/       # HTML templates
├── static/          # CSS, JS, images (if added)
├── .gitignore
├── README.md
└── manage.py


### 🧾 Example Pages


/employees/ → View all employees


/employees/create/ → Add a new employee


/payroll/ → Payroll home page


/payroll/payslip/<id>/ → View individual payslip



🧑‍💻 Author
Anchal Kumar
🌐 anchalk04

🪶 License
This project is licensed under the MIT License.


💡 Made with Django & ❤️ for learning and simplicity.
