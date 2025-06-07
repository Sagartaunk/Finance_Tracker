# 💰 Personal Finance Tracker

A simple Python application for tracking personal income and expenses with data visualization and savings goal features.

## 👥 Project Team

**Created by:**
- **Sagar Taunk** ([@Sagartaunk](https://github.com/Sagartaunk)) 
- **Adamya Thakur** 
- **Soham Guleria** 

**Project Type:** School Assignment  
**Subject:** Data Analytics with Python  
**Date:** June 2025

---

## 📖 Project Overview

The Personal Finance Tracker is a beginner-friendly Python application designed to help users manage their personal finances. It allows you to track income and expenses, set savings goals, calculate tax, and visualize your spending and savings progress.

### ✨ Key Features

- 💵 **Transaction Management** - Add and view expense transactions (income is entered separately at startup or via menu)
- 📊 **Data Visualization** - Generate pie charts and bar charts of spending and savings
- 💾 **Data Storage** - Save all data to CSV files automatically
- 📈 **Financial Summary** - View total income, expenses, savings, and after-tax income
- 🎯 **Savings Goals** - Set and track your savings target as a percentage of income
- 🧾 **Tax Calculation** - Set your income tax rate and see after-tax income
- 🏆 **Performance Feedback** - Get feedback on your savings performance
- 🧑 **Personalized** - Asks for your name and income at startup for a tailored experience
- 🛠️ **Simple Interface** - Easy-to-use menu-driven system

---

## 🛠️ Technical Requirements

### Required Libraries
```bash
pip install pandas matplotlib
```

### Python Version
- Python 3.6 or higher

### System Requirements
- Any operating system (Windows, macOS, Linux)
- 10MB free disk space

---

## 📂 Project Structure

```
finance_tracker/
│
├── finance_tracker.py          # Main application file
├── README.md                   # This documentation
├── transactions.csv            # Transaction data (auto-generated)
├── settings.csv                # Savings goal and tax rate (auto-generated)
└── sample_data/                # Sample data for testing
```

---

## 🚀 Getting Started

### 1. Download the Project
Download or clone the repository and ensure you have Python and the required libraries installed.

### 2. Install Required Libraries
```bash
pip install pandas matplotlib
```

### 3. Run the Application
```bash
python finance_tracker.py
```

### 4. First Time Setup
1. Run the program
2. Enter your name and your income (required to continue)
3. Optionally set your savings goal and tax rate
4. Start adding your own transactions with option **1**

---

## 📱 How to Use

### Main Menu Options

#### 1. Add Transaction
- Enter a description (e.g., "Grocery Shopping")
- Enter the amount (e.g., 500)
- Select a category from the list:
  1. Food
  2. Transportation
  3. Entertainment
  4. Shopping
  5. Bills

#### 2. Add Income
- Add additional income sources at any time

#### 3. View Transactions
- Shows all your recorded transactions in a table format

#### 4. Show Summary
- Displays your total income, estimated tax, after-tax income, total expenses, savings, and savings goal progress

#### 5. Show Pie Chart
- Visualizes your spending and savings by category

#### 6. Show Bar Chart
- Compares spending, actual savings, and target savings

#### 7. Show Saving Goals
- Displays your current savings goal and tax rate

#### 8. Create Sample Data
- Generates example transactions for testing

#### 9. Set Savings Goal
- Update your savings goal percentage

#### 10. Set Tax Rate
- Update your income tax rate

#### 11. Exit
- Safely closes the program

---

## 📊 Data Analysis Features

- **Pandas** for data management and aggregation
- **Matplotlib** for pie and bar chart visualizations
- **CSV** for persistent data storage

---

## 📈 Learning Outcomes

- Python programming with real-world data
- Data analysis and visualization
- Menu-driven CLI application design
- File I/O and error handling

---

## 🔮 Future Enhancements

- Date tracking for transactions
- Custom spending categories
- Budget features and alerts
- Export reports in different formats
- Multi-user support

---

## 📝 Sample Data

The program includes sample data for testing:

| Description | Amount | Category      |
|-------------|--------|--------------|
| Salary      | 10000  | Income       |
| Groceries   | 1500   | Food         |
| Gas         | 800    | Transportation|
| Movie       | 400    | Entertainment|
| Clothes     | 1200   | Shopping     |
| Electric Bill| 900   | Bills        |

---

## 🤝 Contributing

Suggestions are welcome!  
- Keep code simple and readable  
- Add comments for new features  
- Test all functionality before submitting  

---

## 📞 Support

- **GitHub Issues** - Report bugs or ask questions
- **Email Contact** - Reach out to team members

---

## 📄 License

This project is created for educational purposes.  
Feel free to use, modify, and share for learning and practice.

---

*Project completed: June 7, 2025*  
*Last updated: June 7, 2025*  
*Repository: [Personal Finance Tracker](https://github.com/Sagartaunk/finance-tracker)*