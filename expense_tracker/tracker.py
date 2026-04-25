import json
import re
from datetime import date, datetime
from pathlib import Path


class ExpenseTracker:
    def __init__(self, file_path="expenses.json"):
        self.file_path = Path(__file__).with_name(file_path)
        self.expenses = []

    def load_data(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                self.expenses = json.load(file)
        except FileNotFoundError:
            self.expenses = []
        except json.JSONDecodeError:
            print("Warning: expenses file is damaged. Starting with empty data.")
            self.expenses = []

    def save_data(self):
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(self.expenses, file, indent=2)

    def add_expense(self):
        try:
            amount = float(input("Enter amount: ").strip())
            if amount <= 0:
                print("Amount must be greater than zero.")
                return
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            return

        category = input("Enter category: ").strip().lower()
        if not self._is_valid_text(category):
            print("Invalid category. Use letters, numbers, spaces, hyphens, or underscores.")
            return

        note = input("Enter note: ").strip()
        if note and not self._is_valid_text(note):
            print("Invalid note. Use letters, numbers, spaces, hyphens, or underscores.")
            return

        expense_date = input("Enter date (YYYY-MM-DD) or leave blank for today: ").strip()
        if not expense_date:
            expense_date = date.today().isoformat()
        elif not self._is_valid_date(expense_date):
            print("Invalid date. Please use YYYY-MM-DD format.")
            return

        self.expenses.append(
            {
                "amount": amount,
                "category": category,
                "note": note,
                "date": expense_date,
            }
        )
        print("Expense added successfully!")

    def view_expenses(self, expenses=None, title="----- All Expenses -----"):
        expenses = self.expenses if expenses is None else expenses
        print(f"\n{title}")
        if not expenses:
            print("No expenses found.")
            return

        print("ID | Amount | Category | Note        | Date")
        print("---------------------------------------------")
        for expense_id, expense in self._expense_generator(expenses):
            print(
                f"{expense_id:<2} | "
                f"{self._format_amount(expense['amount']):<6} | "
                f"{expense['category']:<8} | "
                f"{expense.get('note', ''):<11} | "
                f"{expense['date']}"
            )

    def total_spending(self):
        total = sum(map(lambda expense: float(expense["amount"]), self.expenses))
        print(f"Total Spending: {self._format_amount(total)}")

    def filter_by_category(self):
        category = input("Enter category to filter: ").strip().lower()
        filtered = list(filter(lambda expense: expense["category"] == category, self.expenses))
        self.view_expenses(filtered, "----- Filtered Expenses -----")

    def delete_expense(self):
        try:
            expense_id = int(input("Enter Expense ID to delete: ").strip())
        except ValueError:
            print("Invalid input! Please enter a valid ID.")
            return

        if expense_id < 1 or expense_id > len(self.expenses):
            print("Expense ID not found.")
            return

        del self.expenses[expense_id - 1]
        print("Expense deleted successfully!")

    def _expense_generator(self, expenses):
        for index, expense in enumerate(expenses, start=1):
            yield index, expense

    def _is_valid_text(self, value):
        return bool(value and re.fullmatch(r"[A-Za-z0-9 _-]+", value))

    def _is_valid_date(self, value):
        try:
            datetime.strptime(value, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    def _format_amount(self, amount):
        amount = float(amount)
        return str(int(amount)) if amount.is_integer() else f"{amount:.2f}"
