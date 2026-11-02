# BruteWatch
### Web Authentication Brute-Force Detection System

BruteWatch is a Python and Flask-based security utility that detects and blocks brute-force login attempts against web authentication endpoints.

---

## Project Overview

Brute-force attacks repeatedly try username and password combinations to gain access. BruteWatch monitors failed login attempts from each IP address and blocks suspicious activity automatically.

This project demonstrates blue-team security concepts, intrusion detection logic, and real-time prevention in a Flask application.

---

## Objectives

- Detect brute-force login attacks
- Track failed authentication attempts per IP
- Block malicious IPs automatically
- Improve web authentication defense

---

## Features

- Failed login attempt tracking
- Time-window based detection logic
- Automatic IP blocking
- Flask-based web app integration
- Simple structure for future database or Redis support

---

## Technologies Used

- Python 3
- Flask
- HTML
- Time module
- Collections (defaultdict)

---

## How It Works

1. A user submits login credentials.
2. The system checks the client IP address.
3. Failed attempts are counted and tracked.
4. If the threshold is exceeded, the IP is blocked.

---

## Run the Project

```bash
pip install -r Requirements.txt
python app.py
```

Then open:

```text
http://127.0.0.1:5000
```

---

## Notes

- This is a lightweight security demo.
- In production, you should replace the in-memory user store with a real database.
