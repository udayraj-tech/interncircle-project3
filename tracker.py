import csv
from datetime import datetime
from collections import defaultdict
import os

FILE = "expenses.csv"
FIELDS = ["date", "category", "description", "amount"]
VALID_CATEGORIES = ["Food", "Travel", "Study", "Bills", "Fun"]

def init_file():
    """Ensure expenses.csv exists with headers."""
    if not os.path.exists(FILE):
        with open(FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDS)
            writer.writeheader()

def save_expense(row):
    """Append a validated expense record to the CSV file."""
    init_file()
    with open(FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writerow(row)

def load_expenses():
    """Load all expenses from the CSV file."""
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r", newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def read_date(prompt):
    """Validate date format YYYY-MM-DD."""
    while True:
        val = input(prompt).strip()
        try:
            datetime.strptime(val, "%Y-%m-%d")
            return val
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD (e.g., 2026-10-15).")

def read_amount(prompt):
    """Validate positive numerical amount."""
    while True:
        val = input(prompt).strip()
        try:
            amount = float(val)
            if amount <= 0:
                print("Amount must be greater than zero.")
                continue
            return f"{amount:.2f}"
        except ValueError:
            print("Please enter a valid numeric amount.")

def add_expense():
    print("\n--- Add New Expense ---")
    date_val = read_date("Enter date (YYYY-MM-DD): ")
    
    print(f"Categories: {', '.join(VALID_CATEGORIES)}")
    while True:
        cat = input("Enter category: ").strip().capitalize()
        if cat in VALID_CATEGORIES:
            break
        print(f"Invalid category. Choose from: {', '.join(VALID_CATEGORIES)}")
        
    desc = input("Enter description: ").strip()
    amount_val = read_amount("Enter amount: ")

    row = {
        "date": date_val,
        "category": cat,
        "description": desc,
        "amount": amount_val
    }
    save_expense(row)
    print("Expense recorded successfully!")

def display_table(rows):
    if not rows:
        print("No expenses found.")
        return
    print(f"\n{'Date':<12} {'Category':<10} {'Description':<25} {'Amount':>10}")
    print("-" * 60)
    for r in rows:
        print(f"{r['date']:<12} {r['category']:<10} {r['description']:<25} {float(r['amount']):>10.2f}")

def filter_expenses():
    rows = load_expenses()
    if not rows:
        print("No records available to filter.")
        return

    print("\nFilter by: 1) Category  2) Month (YYYY-MM)")
    sub_choice = input("Select filter: ").strip()

    if sub_choice == "1":
        cat = input(f"Enter category ({', '.join(VALID_CATEGORIES)}): ").strip().capitalize()
        filtered = [r for r in rows if r["category"] == cat]
        display_table(filtered)
    elif sub_choice == "2":
        month = input("Enter month prefix (e.g., 2026-10): ").strip()
        filtered = [r for r in rows if r["date"].startswith(month)]
        display_table(filtered)
    else:
        print("Invalid filter option.")

def show_summary():
    rows = load_expenses()
    if not rows:
        print("No records to calculate summaries.")
        return

    totals = defaultdict(float)
    max_expense = None
    grand_total = 0.0

    for r in rows:
        amt = float(r["amount"])
        totals[r["category"]] += amt
        grand_total += amt
        if max_expense is None or amt > float(max_expense["amount"]):
            max_expense = r

    print("\n--- Spending Summary by Category ---")
    for category, total in totals.items():
        print(f"{category:<10}: ₹{total:.2f}")

    print("-" * 35)
    print(f"{'Grand Total':<10}: ₹{grand_total:.2f}")
    if max_expense:
        print(f"Highest Expense: ₹{float(max_expense['amount']):.2f} ({max_expense['description']} on {max_expense['date']})")

def main():
    init_file()
    while True:
        print("\n=== Personal Expense Tracker ===")
        print("1) Add Expense")
        print("2) View All Expenses")
        print("3) Filter Expenses")
        print("4) Summary Statistics")
        print("5) Quit")

        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_expense()
        elif choice == "2":
            display_table(load_expenses())
        elif choice == "3":
            filter_expenses()
        elif choice == "4":
            show_summary()
        elif choice == "5":
            print("Exiting application.")
            break
        else:
            print("Please enter a valid choice from 1 to 5.")

if __name__ == "__main__":
    main()