# 💰 Finance Dashboard Backend

## 📌 Overview

This project is a backend system for a finance dashboard that supports role-based access control, financial record management, and aggregated analytics for dashboard insights.

---

## 🚀 Features

* User & Role Management (Viewer, Analyst, Admin)
* Financial Records CRUD (Income/Expense)
* Role-Based Access Control
* Dashboard Summary APIs
* Input Validation & Error Handling

---

## 🛠 Tech Stack

* Backend: Django, Django REST Framework
* Database: SQLite
* API Type: REST

---

## ⚙️ Setup Instructions

```bash
git clone https://github.com/your-username/finance-dashboard-backend.git
cd finance-dashboard-backend

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
```

---

## 🔐 Roles & Permissions

| Role    | Permissions                          |
| ------- | ------------------------------------ |
| Viewer  | View dashboard only                  |
| Analyst | View records + dashboard             |
| Admin   | Full access (CRUD + user management) |

---

## 📡 API Endpoints

### Financial Records

* `GET /api/records/`
* `POST /api/records/`
* `PUT /api/records/{id}/`
* `DELETE /api/records/{id}/`

### Dashboard

* `GET /api/dashboard/summary/`

---

## 📊 Sample Response

```json
{
  "total_income": 5000,
  "total_expense": 2000,
  "net_balance": 3000
}
```

---

## ⚠️ Assumptions

* Each user manages their own financial records
* Admin has full system access
* SQLite is used for simplicity

---

## ✨ Future Improvements

* JWT Authentication
* Pagination & Filtering
* API Documentation (Swagger)
* Unit Testing

---

## 👨‍💻 Author

Your Name
