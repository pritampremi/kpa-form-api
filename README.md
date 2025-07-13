# 🚀 KPA Form API Assignment

## 👨‍💻 Developed by: Pritam Premi

This FastAPI-based backend project implements two API endpoints from the [KPA_form_data API documentation](https://app.swaggerhub.com/apis/sarvasuvidhaen/kpa-form_data/1.0.0), as per assignment requirements.

The two implemented APIs are:
- `POST /form/submit` – to submit a form
- `GET /form/fetchAllByUserId/{user_id}` – to fetch forms submitted by a user

---

## 📌 API Endpoints

### 1. `POST /form/submit`

Submits a form with a user ID and form content.

**Request Body:**

```json
{
  "user_id": 101,
  "form_data": "This is a test form submission"
}
```

**Response:**

```json
{
  "id": 1,
  "user_id": 101,
  "form_data": "This is a test form submission"
}
```

---

### 2. `GET /form/fetchAllByUserId/{user_id}`

Returns all forms submitted by the specified user.

**Example:** `/form/fetchAllByUserId/101`

**Response:**

```json
[
  {
    "id": 1,
    "user_id": 101,
    "form_data": "This is a test form submission"
  }
]
```

---

## 🛠️ Tech Stack

- **Backend Framework:** FastAPI  
- **Database:** PostgreSQL  
- **ORM:** SQLAlchemy  
- **Language:** Python 3.10+  
- **Tools:** Uvicorn, Pydantic, python-dotenv  

---

## 📦 Project Setup Instructions

### 📁 Step 1: Clone or Extract the Project

```bash
git clone (https://github.com/pritampremi/kpa-form-api)
cd kpa_form_api
```
---

### 🐍 Step 2: Create and Activate Virtual Environment

```bash
python -m venv env
env\Scripts\activate      # For Windows

# OR (for macOS/Linux)
source env/bin/activate
```

---

### 📥 Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

> If `requirements.txt` is missing, you can install manually:

```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary python-dotenv
```

---

### 🔐 Step 4: Update `.env` File in Root Directory

Update `.env` file in the root folder with your PostgreSQL username and password.

Make sure PostgreSQL is running and the `kpa_db` database exists.

---

### 🚀 Step 5: Run the FastAPI Server

```bash
uvicorn app.main:app --reload
```

Visit the Swagger docs at:

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

Use Swagger UI to test both endpoints interactively.

---

## ✅ Features Implemented

- 📤 Submit form via `POST`
- 📥 Fetch forms by user ID via `GET`
- 🔐 Environment-based config using `.env`
- 🔄 Auto table creation with SQLAlchemy
- 📚 Interactive Swagger documentation
- 🧪 Tested with Postman and Swagger

---

## ⚠️ Assumptions / Notes

- No login/auth is required for this submission.
- `form_data` is a plain text field — can hold JSON if needed.
- Auto-generated ID (`id`) is handled by the database.

---


## 📬 Contact

For any questions, email: **premipritam00@gmail.com**
