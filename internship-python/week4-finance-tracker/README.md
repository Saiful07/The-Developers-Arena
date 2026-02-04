# Personal Finance Tracker

A command-line application to track personal expenses with categories, reports, and data export functionality.

## Features

- Add and manage expenses with categories
- Search expenses by category, date range, or description
- Generate monthly reports with statistics
- View category-wise expense breakdown
- Export data to CSV format
- Automatic backup and restore functionality
- Data persistence using JSON

## Installation

1. Clone the repository
2. Create virtual environment:
```bash
   python -m venv .venv
```
3. Activate virtual environment:
```bash
   # Windows
   .venv\Scripts\activate
   
   # Linux/Mac
   source .venv/bin/activate
```

## Usage

Run the application:
```bash
python -m finance_tracker.main
```

## Project Structure
```
week4-finance-tracker/
├── finance_tracker/
│   ├── models/          # Data models
│   ├── core/            # Business logic
│   ├── storage/         # File operations
│   ├── reporting/       # Report generation
│   ├── ui/              # User interface
│   └── config.py        # Configuration
├── data/                # Data storage
│   ├── backups/         # Backup files
│   └── exports/         # CSV exports
└── tests/               # Unit tests
```

## Categories

- Food & Dining
- Transportation
- Shopping
- Entertainment
- Bills & Utilities
- Healthcare
- Education
- Other

## Data Storage

- Expenses are stored in JSON format
- Automatic backups created on demand
- CSV export available for external analysis
- Data persists between sessions

## Author

Created for Week 4 internship assignment.