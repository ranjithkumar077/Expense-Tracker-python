from tracker import ExpenseTracker


def show_menu():
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Spending")
    print("4. Filter by Category")
    print("5. Delete Expense")
    print("6. Save & Exit")


def main():
    tracker = ExpenseTracker()
    tracker.load_data()

    while True:
        show_menu()
        choice = input("Enter choice: ").strip()

        if choice == "1":
            tracker.add_expense()
        elif choice == "2":
            tracker.view_expenses()
        elif choice == "3":
            tracker.total_spending()
        elif choice == "4":
            tracker.filter_by_category()
        elif choice == "5":
            tracker.delete_expense()
        elif choice == "6":
            print("Saving data...")
            tracker.save_data()
            print("Data saved successfully!")
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
