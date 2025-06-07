# 💰 Personal Finance Tracker

A simple Python application for tracking personal income and expenses with data visualization capabilities.

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

The Personal Finance Tracker is a beginner-friendly Python application designed to help users manage their personal finances. It provides an easy way to track income and expenses, categorize transactions, and visualize spending patterns through charts.

### ✨ Key Features

- 💵 **Transaction Management** - Add and view income/expense transactions
- 📊 **Data Visualization** - Generate pie charts and bar charts of spending
- 💾 **Data Storage** - Save all data to CSV files automatically
- 📈 **Financial Summary** - View total income, expenses, and savings
- 🎯 **Simple Interface** - Easy-to-use menu-driven system

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
└── sample_data/               # Sample data for testing
```

---

## 🚀 Getting Started

### 1. Download the Project
```bash
# Download the finance_tracker.py file
# Make sure you have Python and required libraries installed
```

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
2. Choose option **6** to create sample data
3. Explore other menu options to see how it works
4. Start adding your own transactions with option **1**

---

## 📱 How to Use

### Main Menu Options

#### 1. Add Transaction
- Enter a description (e.g., "Grocery Shopping")
- Enter the amount (e.g., 50.00)
- Select a category from the list:
  1. Food
  2. Transportation
  3. Entertainment
  4. Shopping
  5. Bills
  6. Income

#### 2. View Transactions
- Shows all your recorded transactions in a table format
- Displays description, amount, and category for each transaction

#### 3. Show Summary
- Displays your total income
- Shows total expenses
- Calculates how much money you have left
- Simple financial overview

#### 4. Show Pie Chart
- Creates a colorful pie chart showing spending by category
- Visual representation of where your money goes
- Percentages shown for each category

#### 5. Show Bar Chart
- Creates a bar chart of spending by category
- Easy to compare spending across different categories
- Shows exact amounts for each category

#### 6. Create Sample Data
- Generates example transactions for testing
- Includes sample income and various expenses
- Great for trying out the features

#### 7. Exit
- Safely closes the program
- All data is automatically saved

---

## 💻 Code Structure

### Main Components

```python
# Simple function-based structure
def add_transaction():     # Handles adding new transactions
def view_transactions():   # Shows all transactions
def show_pie_chart():     # Creates pie chart visualization
def show_bar_chart():     # Creates bar chart visualization
def show_summary():       # Displays financial summary
def create_sample_data(): # Generates test data

# Main program loop
while True:
    # Menu system and user input handling
```

### Data Storage

#### CSV Files
- **transactions.csv** - Stores all transaction data
  - Columns: Description, Amount, Category
  - Automatically created when you add your first transaction
  - Data persists between program runs

#### DataFrame Operations
```python
# Creating new transaction
new_data = pd.DataFrame({
    'Description': [description],
    'Amount': [amount], 
    'Category': [category]
})

# Reading existing data
existing_data = pd.read_csv('transactions.csv')

# Combining data
all_data = pd.concat([existing_data, new_data])
```

---

## 📊 Data Analysis Features

### Pandas Operations Used
- **DataFrame Creation** - `pd.DataFrame()`
- **CSV Reading/Writing** - `pd.read_csv()`, `df.to_csv()`
- **Data Grouping** - `df.groupby()`
- **Data Aggregation** - `.sum()`
- **Data Concatenation** - `pd.concat()`

### Matplotlib Visualizations
- **Pie Charts** - Shows spending distribution by category
- **Bar Charts** - Compares spending amounts across categories
- **Customization** - Titles, labels, colors, and formatting

```python
# Example: Creating a pie chart
spending = data.groupby('Category')['Amount'].sum()
plt.pie(spending.values, labels=spending.index, autopct='%1.1f%%')
plt.title('Spending by Category')
plt.show()
```

---

## 📈 Learning Outcomes

This project demonstrates:

### Python Programming Skills
- **Basic Syntax** - Variables, loops, conditionals
- **Functions** - Creating and calling functions
- **Error Handling** - Try-except blocks
- **File Operations** - Reading and writing CSV files

### Data Analysis Skills
- **Pandas Library** - DataFrame manipulation and analysis
- **Data Grouping** - Organizing data by categories
- **Data Aggregation** - Calculating totals and summaries

### Data Visualization Skills
- **Matplotlib Library** - Creating charts and graphs
- **Chart Types** - Pie charts and bar charts
- **Customization** - Adding titles, labels, and formatting

---

## 🎯 Example Usage

### Adding Your First Transaction
```
Choose option (1-7): 1

Add New Transaction
--------------------
Enter description: Monthly Salary
Enter amount: $3000

Categories:
1. Food
2. Transportation
3. Entertainment
4. Shopping
5. Bills
6. Income

Select category (1-6): 6
Added: Monthly Salary - $3000.0
```

### Viewing Summary
```
Choose option (1-7): 3

Summary:
--------------------
Total Income: $3000.0
Total Spent: $450.0
Money Left: $2550.0
```

---

## 🔧 Technical Implementation

### Key Programming Concepts

#### 1. Menu-Driven Interface
```python
while True:
    print("\nMenu:")
    # Display options
    choice = input("Choose option (1-7): ")
    
    if choice == "1":
        add_transaction()
    # Handle other choices
```

#### 2. Data Persistence
```python
# Save data to CSV
all_data.to_csv('transactions.csv', index=False)

# Load data from CSV
try:
    data = pd.read_csv('transactions.csv')
except:
    print("No transactions found!")
```

#### 3. Error Handling
```python
try:
    # Attempt to read data
    data = pd.read_csv('transactions.csv')
except:
    # Handle case when file doesn't exist
    print("No data to show!")
```

---

## 📚 Educational Value

### For Students
- **Practical Application** - Real-world financial management
- **Data Skills** - Working with structured data
- **Programming Logic** - Menu systems and user interaction
- **Problem Solving** - Handling user input and data validation

### For Teachers
- **Clear Code Structure** - Easy to understand and grade
- **Meets Requirements** - Uses pandas and matplotlib extensively
- **Appropriate Complexity** - Suitable for intermediate Python students
- **Practical Output** - Generates useful CSV files and visualizations

---

## 🔮 Future Enhancements

### Possible Improvements
- **Date Tracking** - Add transaction dates
- **Budget Features** - Set spending limits by category
- **More Charts** - Line graphs for trends over time
- **Data Export** - Export reports in different formats
- **Categories** - Add custom spending categories

### Advanced Features
- **Database Storage** - Use SQLite instead of CSV
- **Web Interface** - Create a web-based version
- **Mobile App** - Develop smartphone application
- **Bank Integration** - Import transactions automatically

---

## 🐛 Known Limitations

### Current Constraints
- **No Date Tracking** - Transactions don't have timestamps
- **Limited Categories** - Fixed set of spending categories
- **Basic Validation** - Minimal input error checking
- **Single User** - Designed for one person's finances

### Workarounds
- **Manual Dating** - Add dates in transaction descriptions
- **Category Flexibility** - Use "Other" for unlisted categories
- **Data Backup** - Manually copy CSV files for safety

---

## 📝 Sample Data

The program includes sample data for testing:

| Description | Amount | Category |
|-------------|---------|-----------|
| Salary | $2000 | Income |
| Groceries | $100 | Food |
| Gas | $50 | Transportation |
| Movie | $20 | Entertainment |
| Clothes | $80 | Shopping |
| Electric Bill | $120 | Bills |

---

## 💡 Tips for Success

### For Using the Program
1. **Start with Sample Data** - Use option 6 to explore features
2. **Be Consistent** - Use similar descriptions for similar expenses
3. **Regular Updates** - Add transactions frequently
4. **Backup Data** - Copy your CSV files regularly

### For Understanding the Code
1. **Read Comments** - Each function has clear documentation
2. **Test Functions** - Try each menu option to see what happens
3. **Modify Carefully** - Make small changes and test frequently
4. **Ask Questions** - Understanding is more important than memorization

---

## 🤝 Contributing

This is a school project, but suggestions are welcome:

### How to Contribute
1. **Fork the Repository** - Create your own copy
2. **Make Improvements** - Add features or fix bugs
3. **Test Thoroughly** - Make sure everything works
4. **Submit Changes** - Share your improvements

### Contribution Guidelines
- Keep code simple and readable
- Add comments for new features
- Test all functionality before submitting
- Follow the existing code style

---

## 📞 Support

### Getting Help
- **GitHub Issues** - Report bugs or ask questions
- **Email Contact** - Reach out to team members
- **Documentation** - Check this README for answers

### Common Issues
- **Import Errors** - Make sure pandas and matplotlib are installed
- **File Not Found** - Run option 6 to create sample data first
- **Chart Not Showing** - Check matplotlib installation

---

## 📄 License

This project is created for educational purposes. Feel free to:
- Use for learning and practice
- Modify for your own needs
- Share with other students
- Build upon for larger projects

---

## 🙏 Acknowledgments

### Special Thanks
- **Course Instructor** - For project guidance and requirements
- **Python Community** - For excellent documentation and tutorials
- **Pandas Team** - For powerful data analysis tools
- **Matplotlib Team** - For comprehensive visualization library

### Resources Used
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
- [Python Official Tutorial](https://docs.python.org/3/tutorial/)

---

## 📊 Project Statistics

- **Total Lines of Code:** ~150
- **Functions:** 6
- **Libraries Used:** 2 (pandas, matplotlib)
- **File Formats:** CSV, Python
- **Chart Types:** 2 (pie, bar)

---

*Project completed: June 7, 2025*  
*Last updated: June 7, 2025*  
*Repository: [Personal Finance Tracker](https://github.com/Sagartaunk/finance-tracker)*