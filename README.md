# CURD-usingmodelform

A simple **Django CRUD (Create, Read, Update, Delete)** web application that uses Django’s built-in **ModelForm** to handle form rendering and saving data to the database.

This project demonstrates how to:
✔ Create records  
✔ Display records  
✔ Update records  
✔ Delete records  
using **Django ModelForm**.

---

## 🛠️ Features

- Django project structure with app for CRUD
- Uses `ModelForm` for forms (create & update)
- Template pages for:
  - Home / list of objects
  - Form for create & update
  - Confirmation page for delete
- Clean and simple UI using HTML templates
- Basic URL routing for CRUD actions

---

## 📁 Project Structure

CURD-usingmodelform/

│

├── crudproject/

│ ├── init.py

│ ├── settings.py

│ ├── urls.py

│ ├── asgi.py

│ └── wsgi.py

│

├── enroll/

│ ├── migrations/

│ ├── templates/

│ ├── init.py

│ ├── admin.py

│ ├── apps.py

│ ├── forms.py

│ ├── models.py

│ ├── tests.py

│ ├── urls.py

│ └── views.py

│

├── db.sqlite3

├── manage.py

└── README.md


---

## 📌 Folder & File Explanation

### `crudproject/`
Main Django project directory.
- **settings.py** – Project configuration (apps, database, middleware)
- **urls.py** – Main URL routing
- **asgi.py / wsgi.py** – Deployment-related configuration

---

### `enroll/`
Django application responsible for CRUD operations.
- **models.py** – Database model definition
- **forms.py** – ModelForm used for create and update
- **views.py** – Handles CRUD logic
- **urls.py** – App-level URL routing
- **templates/** – HTML templates for UI
- **admin.py** – Model registration for Django admin

---

### `db.sqlite3`
Default SQLite database used for storing application data.

---

### `manage.py`
Command-line utility to manage the Django project  
(e.g., runserver, migrate, createsuperuser).

---

## 🛠️ Technologies Used

- Python
- Django Framework
- SQLite Database
- HTML Templates
- Django ModelForm

---

## 🎯 Purpose of This Project

- Understand Django project structure
- Learn CRUD operations using ModelForm
- Practice Django views, models, and templates
- Beginner-friendly Django project

---

## 🚀 How to Run

```bash
python manage.py runserver

---

## Open browser:
http://127.0.0.1:8000/

