#  Bank Management System

A simple banking application built using **Python, Object-Oriented Programming (OOP), JSON file handling, and Streamlit**. It allows users to  create accounts and perform basic banking operations through an interactive web interface.

## Features

- Create a bank account
- Deposit and withdraw money
- View account details
- Update account information
- Delete an account
- Store account records locally using JSON
- Interactive interface built with Streamlit

## Tech Stack

- Python
- Streamlit
- JSON
- Object-Oriented Programming (OOP)

## Project Structure

```text
BankManagement_OOPS/
├── app.py           # Streamlit web interface
├── main.py          # Original console-based application
├── updated_main.py  # Banking logic
├── data.json        # Local account data (not committed)
├── requirements.txt # Dependencies
├── .gitignore       # Files excluded from Git
└── README.md        # Project documentation
```

## Installation and Usage

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
cd BankManagement_OOPS
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## Concepts Practised

- Classes, objects, and methods
- Lists and dictionaries
- File handling and JSON serialization
- Exception handling
- CRUD operations
- Building interactive applications with Streamlit

## Limitations

This project is for learning purposes. It uses local JSON storage and does not implement production-grade security. PINs and account data require stronger protection before any real-world use.

## Future Improvements

- Integrate SQLite or PostgreSQL
- Securely hash PINs
- Add transaction history
- Improve input validation and error handling

---

**Purpose:** Practising Python fundamentals, OOP, file handling, and basic application development.