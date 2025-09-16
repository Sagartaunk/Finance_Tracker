# Finance Tracker (Class 12 IP Project)

A simple command-line program to track income and expenses using CSV files. It shows summaries and basic charts so you can understand where your money goes.

Made by: Sagar Taunk (https://github.com/Sagartaunk)
         Adamya Thakur
For: Class 12th Informatics Practices (IP) project

## What it does

- Add Expense (Food, Transportation, Entertainment, Shopping, Others)
- Add Income
- View all transactions
- Show Summary (Income, Expenses, Saved, Savings Goal Target, Estimated Tax)
- Show Pie Chart of expenses by category
- Show Bar Chart (expense categories + Actual Savings + Target Savings)
- Set Savings Goal (%)
- Set Tax Rate (%)
- Saves and loads data from CSV files

## Requirements

- Python
- pandas
- matplotlib

Install packages:

```bash
pip install pandas matplotlib
```

## How to run

```bash
python finance_tracker.py
```

If it’s your first run and there are no CSV files, the program will ask for:
- Income
- Tax Rate (%)
- Savings Goal (%)

It will then create these files:
- `settings.csv` — stores your tax rate and savings goal
- `transactions.csv` — stores all your income and expenses

## Files used

- `settings.csv`
  - Columns: `tax_rate`, `savings_goal`
- `transactions.csv`
  - Columns: `Description`, `Amount`, `Category`
  - Category is either `Income` or an expense category (Food, Transportation, Entertainment, Shopping, Others)

## Using the menu

When you run the program, you’ll see:

```
1. Add Transaction
2. Add Income
3. View Transactions
4. Show Summary
5. Show Pie Chart
6. Show Bar Chart
7. Show savings goal
8. Set savings goal
9. Set tax rate
10. Show this menu
11. Exit
```

Tips:
- Use whole numbers or decimals for amounts (e.g., 1500 or 1500.50).
- If you type an invalid value in the first-time setup, the program will use 0.0 for that value so it can continue.
- Pie chart shows only expenses (no income). Percent labels are intentionally not shown.
- Bar chart shows each expense category plus two bars:
  - Actual Savings = Income − Total Expenses (not less than 0)
  - Target Savings = Income × (Savings Goal %)

## Summary details

- Total Income = sum of all rows where Category = “Income”
- Total Expenses = sum of all rows where Category is not “Income”
- Saved = Income − Expenses
- Savings Goal Target = Income × (Savings Goal %)
- Estimated Tax = Income × (Tax Rate %)

Note: These are simple calculations for learning purposes.

## Resetting or starting over

- Delete `transactions.csv` and/or `settings.csv` if you want to start fresh.
- Run the program again and enter the initial values.

## Example workflow

1. Run the program
2. Add your first income
3. Add a few expenses (Food, Transportation, etc.)
4. View Transactions
5. Show Summary
6. Draw charts (Pie/Bar)
7. Adjust savings goal or tax rate if needed

## License
Free to use, edit, or share.

- You can copy, modify, and distribute this project for any purpose (personal, educational, or commercial) without asking for permission.
- Attribution to the authors is appreciated but not required.
- Provided “as is”, without any warranty.
