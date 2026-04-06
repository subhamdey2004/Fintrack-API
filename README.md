<<<<<<< HEAD
# FinTrack API

A role-based personal finance tracking backend built with FastAPI for the Zorvyn Backend Screening Assignment.

This project was developed with a focus on clean architecture , JWT authentication , role-based access control, transaction management , and financial analytics.

## Note to Reviewer

Thank you for reviewing this submission.

Rather than treating this as just an assignment, I approached it as a small but realistic backend product — with structured APIs, clear separation of concerns, authentication, authorization, and meaningful financial summary logic.

## Features

### Authentication & Authorization
- User registration
- User login with JWT authentication
- Protected routes using Bearer Token
- Role-Based Access Control (RBAC)

### Supported Roles
- Viewer → Can view transactions and summaries
- Analyst → Can view transactions, apply filters, and access detailed summaries
- Admin → Full access to create, update, delete, and manage records

### Financial Records Management
- Create financial transactions
- View all transactions
- View single transaction by ID
- Update transaction
- Delete transaction
- Filter transactions by:
  - type
  - category
  - date range

### Summary & Analytics
- Total income
- Total expenses
- Current balance
- Category-wise expense breakdown
- Monthly summary
- Recent activity


## Tech Stack

- **Python**
- **FastAPI**
- **SQLite**
- **SQLAlchemy**
- **Pydantic**
- **JWT Authentication**
- **Swagger UI**

## Project Structure

```bash
fintrack-api/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── dependencies.py
│
│   ├── routers/
│   │   ├── auth.py
│   │   ├── transactions.py
│   │   └── summary.py
│
│   ├── services/
│   │   ├── transaction_service.py
│   │   └── summary_service.py
│
│   └── core/
│       ├── security.py
│       └── roles.py
│
├── tests/
│   ├── test_transactions.py
│   └── test_summary.py
│
├── requirements.txt
├── README.md
├── .env
└── .gitignore


@@ API Endpoints -

Auth --

POST /auth/register
POST /auth/login

Transactions --
POST /transactions/
GET /transactions/
GET /transactions/{transaction_id}
PUT /transactions/{transaction_id}
DELETE /transactions/{transaction_id}

Summary --
GET /summary/overview
GET /summary/category-breakdown
GET /summary/recent
GET /summary/monthly
Example Roles for Testing

@@  Admin --

{
  "name": "Admin User",
  "email": "admin@example.com",
  "password": "admin123",
  "role": "admin"
}

@@  Viewer --

{
  "name": "Viewer User",
  "email": "viewer@example.com",
  "password": "viewer123",
  "role": "viewer"
}

@@  Analyst --

{
  "name": "Analyst User",
  "email": "analyst@example.com",
  "password": "analyst123",
  "role": "analyst"
}

@@ How to Run Locally ...

1. Clone the repository

git clone https://github.com/YOUR_USERNAME/fintrack-api.git
cd fintrack-api

2. Create virtual environment (optional but recommended)

python -m venv venv

3. Activate virtual environment

  @ Windows

venv\Scripts\activate

  @ Mac/Linux

source venv/bin/activate

4. Install dependencies

pip install -r requirements.txt

5. Run the server

uvicorn app.main:app --reload

@@ API Documentation

 -- Once the server is running, open:

 -- http://127.0.0.1:8000/docs

@ Swagger UI provides interactive API testing.

@ Root API Response

@ The root endpoint returns:

{
  "message": "Welcome to FinTrack API",
  "assignment": "Zorvyn Backend Screening",
  "docs": "/docs"
}

@ Validation & Error Handling

 -- This project includes:

  ... Input validation using Pydantic
  ... Proper HTTP status codes
  ... Useful error responses
  ... Authorization checks for restricted actions

@ Examples:

-401 Unauthorized

-403 Forbidden
-404 Not Found
-422 Validation Error

@ Summary and analytics logic beyond CRUD
-- Swagger-based API testing


@@ This project was built to demonstrate not just functionality, but also backend engineering fundamentals:

 -- clean Python code
 -- maintainable structure
 -- secure API design
 -- practical business logic

Thank you for your time and consideration.

SUBHAM DEY
=======
# Fintrack-API
A role-based personal finance tracking backend built with FastAPI for the Zorvyn Backend Screening Assignment.
>>>>>>> 15ad0f0272888387433d88f2bcb4d1de016b0ed5
