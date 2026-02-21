# 📚 Library Management System (OOP-Based)

A command-line Library Management System built using Object-Oriented Programming principles in Python.

This project demonstrates modular architecture, file persistence using JSON, and clean separation of responsibilities across multiple classes.

---

## 🚀 Features

- Add new books
- Register new members
- Borrow books with due date tracking
- Return books with overdue fine calculation
- Search books by:
  - Title
  - Author
  - ISBN
  - Available books
- View all books
- View all members
- View overdue books
- Automatic JSON data persistence
- Backup system
- System statistics

---

## 🏗 Project Structure

week5-library-system/
│
├── library_system/
│ ├── init.py
│ ├── book.py
│ ├── member.py
│ ├── library.py
│ └── main.py
│
├── data/
│ ├── books.json
│ ├── members.json
│ └── backup/
│
├── tests/
│ ├── test_book.py
│ ├── test_member.py
│ └── test_library.py
│
├── requirements.txt
├── README.md
└── .gitignore


---

## 🧠 Architecture Overview

### Book Class
Represents a book entity with:
- Title
- Author
- ISBN
- Year
- Availability status
- Due date tracking
- Borrowed member ID

Handles checkout, return, overdue calculation, and JSON serialization.

---

### Member Class
Represents a library member with:
- Name
- Member ID
- Borrowed books list

Enforces a maximum borrow limit of 5 books and supports JSON serialization.

---

### Library Class
Acts as the system controller:
- Manages books and members
- Coordinates borrow and return operations
- Handles searching functionality
- Tracks overdue books
- Loads and saves data
- Creates backup files
- Provides statistics

---

## 💾 Data Storage

- Books are stored in `data/books.json`
- Members are stored in `data/members.json`
- Backup files are stored in `data/backup/`

Data is loaded automatically on startup and saved before exiting (if selected).

---

## ▶️ How to Run

Make sure you are inside the root directory:

week5-library-system


Run the application using:

```bash
python -m library_system.main

🧪 Running Tests

To execute unit tests:
python -m unittest discover tests

🛠 Requirements

This project uses only Python standard libraries:

datetime

json

os

No external dependencies are required.

📊 Concepts Demonstrated

Object-Oriented Programming

Encapsulation

Modular design

JSON serialization/deserialization

CLI application structure

File handling

Error handling
