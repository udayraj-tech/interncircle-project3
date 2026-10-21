# Personal Expense Tracker CLI

A lightweight command-line expense management application built with Python standard libraries (`csv`, `datetime`, `collections`).

## Features
- **Persistent Storage**: Saves records to `expenses.csv` using Python's `csv.DictWriter` and `csv.DictReader` with `newline=""` to prevent blank line issues across operating systems.
- **Input Validation**: Strict validation for `YYYY-MM-DD` date formats and numerical positive values for amounts.
- **Filtering**: View data filtered by category or by month prefix (`YYYY-MM`).
- **Summary Analytics**: Aggregates totals per category, calculates the grand total, and identifies the largest single expenditure.

## Setup and Execution
1. Ensure Python 3.10 or newer is installed.
2. Clone this repository:
   ```bash
   git clone [https://github.com/udayraj-tech/interncircle-expense-tracker.git](https://github.com/udayraj-tech/interncircle-expense-tracker.git)
   cd interncircle-expense-tracker