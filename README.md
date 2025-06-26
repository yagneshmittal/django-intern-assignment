# Django Internship Assignment – Command Center + Telegram Bot

## Project Setup

### 1. Clone the Repository

git clone https://github.com/yagneshmittal/django-intern-assignment.git
cd django-intern-assignment


### 2. Setup Virtual Environment

python3 -m venv venv
source venv/bin/activate

### Always activate the venv in any new terminal you use by writing "source venv/bin/activate" on the terminal to run/manage the Django project.

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### Now since I am not sharing my .env file for security reason, so you need to create your own .env file and do following :-

### 4. Create `.env` File
Create a `.env` file in the root with the following content:
```env
DEBUG=True
SECRET_KEY=your_secret_key_here
TELEGRAM_BOT_TOKEN=your_bot_token_here
```

### 5. Run the Server
```bash
python manage.py migrate
python manage.py runserver
```

---

## Features Implemented

Django REST Framework API  
One Public Endpoint  
One Protected Endpoint (JWT Auth)  
Django Login View  
Celery + Redis Setup  
Background Email Task  
Telegram Bot Integration (Captures Username on /start)

---

## API Endpoints

| Endpoint | Method | Auth | Description |
|----------|--------|------|-------------|
| `/api/public/hello/` | GET | ❌ No | Public greeting |
| `/api/protected/dashboard/` | GET | ✅ JWT | Returns protected data |
| `/api/token/` | POST | ❌ | Get JWT access/refresh tokens |

---

## How to Run Telegram Bot
```bash
python telegram_bot/bot.py
```

---

## Environment Variables

- `DEBUG` – True/False
- `SECRET_KEY` – Django secret key
- `TELEGRAM_BOT_TOKEN` – Your Telegram bot token

---

## Author

Yagnesh Mittal  
[GitHub](https://github.com/yagneshmittal)
