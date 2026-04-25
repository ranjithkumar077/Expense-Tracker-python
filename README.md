# Expense Tracker Python

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Storage](https://img.shields.io/badge/Storage-JSON-orange)
![Interface](https://img.shields.io/badge/Interface-CLI-lightgrey)

A clean, beginner-friendly, and professional command-line expense tracker built with Python. The app helps users record daily expenses, organize them by category, calculate total spending, filter records, delete entries, and keep data saved permanently in a JSON file.

## Project Preview

```text
===== Expense Tracker =====
1. Add Expense
2. View Expenses
3. Total Spending
4. Filter by Category
5. Delete Expense
6. Save & Exit
```

Sample table output:

```text
----- All Expenses -----
ID | Amount | Category | Note        | Date
---------------------------------------------
1  | 250    | food     | lunch       | 2026-04-25
2  | 500    | travel   | bus ticket  | 2026-04-25
```

## Features

- Add expenses with amount, category, note, and date
- Automatically uses today's date when no date is entered
- View all saved expenses in a formatted table
- Calculate total spending instantly
- Filter expenses by category
- Delete expenses by ID
- Save and load data using `expenses.json`
- Handles invalid amounts, dates, menu choices, IDs, and missing files
- Uses OOP, JSON file handling, exception handling, regex validation, lambdas, and a generator

## Tech Stack

- Python 3
- JSON file storage
- Command-line interface
- Object-oriented programming

## Folder Structure

```text
Expense-Tracker-python/
|
|-- README.md
|-- LICENSE
|-- .gitignore
|-- expense_tracker/
    |-- main.py
    |-- tracker.py
    |-- expenses.json
    |-- README.md
```

## How To Run

Clone the repository:

```bash
git clone https://github.com/ranjithkumar077/Expense-Tracker-python.git
```

Open the project folder:

```bash
cd Expense-Tracker-python/expense_tracker
```

Run the app:

```bash
python main.py
```

## Learning Concepts Covered

- Functions and clean code structure
- Classes and objects
- Lists and dictionaries
- File handling with JSON
- Exception handling
- Regex validation
- Lambda functions
- Generators
- CLI menu-driven programming

## Author

Created by [Ranjith Kumar](https://github.com/ranjithkumar077)
