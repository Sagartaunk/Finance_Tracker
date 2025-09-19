# Finance Tracker

A simple **command-line based personal finance tracker** built as a **Class 12 Computer Science project**.
The program helps users manage their income, expenses, and savings goals while also giving visual insights through **pie charts** and **bar charts**.

---

## 👨‍💻 Authors
- **[Sagar Taunk](https://github.com/sagartaunk)**
- **Adamya Thakur**

---

## 🎯 Project Goal
This project was created as part of a **Class 12 Computer Science assignment** to demonstrate:
- File handling with **CSV files**
- Use of **pandas** for data management
- Basic **matplotlib** charts for visualization
- Control flow, loops, and exception handling in Python

---

## ⚡ Features
1. **Add Transaction** – Record expenses under categories like Food, Transportation, Shopping, etc.
2. **Add Income** – Log new income sources.
3. **View Transactions** – Display all past transactions.
4. **Show Summary** – Get a quick overview of income, expenses, savings, and estimated tax.
5. **Pie Chart** – Visualize expense distribution by category.
6. **Bar Chart** – Compare expenses, actual savings, and target savings.
7. **Show Savings Goal** – Display current savings goal and tax rate.
8. **Update Settings** – Change savings goal and tax rate anytime.
9. **Persistent Data** – All data is stored in **CSV files** (`transactions.csv` and `settings.csv`).

---

## 📂 Files
- **`finance_tracker.py`** → The main program file.
- **`transactions.csv`** → Stores all income and expense transactions.
- **`settings.csv`** → Stores user settings (savings goal, tax rate).

---

## 🛠️ Technologies Used
- **Python 3.x**
- **pandas** → For handling CSV files
- **matplotlib** → For plotting charts

---

## 🚀 How to Run
1. Clone the repo or download the code:
   ```bash
   git clone https://github.com/sagartaunk/finance-tracker.git
   cd finance-tracker
   ```
2. Install dependencies:
   ```bash
   pip install pandas matplotlib
   ```
3. Run the program:
   ```bash
   python finance_tracker.py
   ```

---

## 📊 Sample Output

### Summary Example:
```
Total Income: 50000.0
Total Expenses: 15000.0
Saved: 35000.0
Savings Goal Target ( 20.0 % of income ): 10000.0
Estimated Tax ( 10.0 % of income ): 5000.0
```

### Pie Chart (Expenses by Category)
Shows how your expenses are distributed across categories.

### Bar Chart (Expenses and Savings)
Compares actual savings with the target savings goal.

---

## 📌 Notes
- This is a **beginner-level project**, meant for learning purposes.
- Data is saved locally in CSV files, so deleting them will reset the tracker.
- No database or GUI is used to keep things simple for Class 12 project requirements.

---

## 📜 License
This project is made for **educational purposes only**. Feel free to use or modify it for your own school projects!
