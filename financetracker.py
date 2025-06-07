import pandas as pd
import matplotlib.pyplot as plt

def add_transaction():
    """Add a new transaction"""
    print("\nAdd New Transaction")
    print("-" * 20)
    
    description = input("Enter description: ")
    amount = float(input("Enter amount: $"))
    
    print("\nCategories:")
    print("1. Food")
    print("2. Transportation") 
    print("3. Entertainment")
    print("4. Shopping")
    print("5. Bills")
    print("6. Income")
    
    choice = int(input("Select category (1-6): "))
    
    if choice == 1:
        category = "Food"
    elif choice == 2:
        category = "Transportation"
    elif choice == 3:
        category = "Entertainment"
    elif choice == 4:
        category = "Shopping"
    elif choice == 5:
        category = "Bills"
    else:
        category = "Income"
    
    # Save to CSV
    new_data = pd.DataFrame({
        'Description': [description],
        'Amount': [amount],
        'Category': [category]
    })
    
    try:
        existing_data = pd.read_csv('transactions.csv')
        all_data = pd.concat([existing_data, new_data])
    except:
        all_data = new_data
    
    all_data.to_csv('transactions.csv', index=False)
    print(f"Added: {description} - ${amount}")

def view_transactions():
    """Show all transactions"""
    try:
        data = pd.read_csv('transactions.csv')
        print("\nAll Transactions:")
        print("-" * 30)
        print(data.to_string(index=False))
    except:
        print("No transactions found!")

def show_pie_chart():
    """Show pie chart of spending"""
    try:
        data = pd.read_csv('transactions.csv')
        spending = data.groupby('Category')['Amount'].sum()
        
        plt.figure(figsize=(8, 6))
        plt.pie(spending.values, labels=spending.index, autopct='%1.1f%%')
        plt.title('Spending by Category')
        plt.show()
    except:
        print("No data to show!")

def show_bar_chart():
    """Show bar chart of spending"""
    try:
        data = pd.read_csv('transactions.csv')
        spending = data.groupby('Category')['Amount'].sum()
        
        plt.figure(figsize=(10, 6))
        plt.bar(spending.index, spending.values)
        plt.title('Spending by Category')
        plt.xlabel('Category')
        plt.ylabel('Amount ($)')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    except:
        print("No data to show!")

def show_summary():
    """Show spending summary"""
    try:
        data = pd.read_csv('transactions.csv')
        
        total_spent = 0
        total_income = 0
        
        for i in range(len(data)):
            if data.iloc[i]['Category'] == 'Income':
                total_income = total_income + data.iloc[i]['Amount']
            else:
                total_spent = total_spent + data.iloc[i]['Amount']
        
        print("\nSummary:")
        print("-" * 20)
        print(f"Total Income: ${total_income}")
        print(f"Total Spent: ${total_spent}")
        print(f"Money Left: ${total_income - total_spent}")
        
    except:
        print("No data to show!")

def create_sample_data():
    """Create sample data for testing"""
    sample_data = pd.DataFrame({
        'Description': ['Salary', 'Groceries', 'Gas', 'Movie', 'Clothes', 'Electric Bill'],
        'Amount': [2000, 100, 50, 20, 80, 120],
        'Category': ['Income', 'Food', 'Transportation', 'Entertainment', 'Shopping', 'Bills']
    })
    
    sample_data.to_csv('transactions.csv', index=False)
    print("Sample data created!")

# Main program starts here
print("Personal Finance Tracker")
print("=" * 30)

while True:
    print("\nMenu:")
    print("1. Add Transaction")
    print("2. View Transactions")
    print("3. Show Summary")
    print("4. Show Pie Chart")
    print("5. Show Bar Chart")
    print("6. Create Sample Data")
    print("7. Exit")
    
    choice = input("Choose option (1-7): ")
    
    if choice == "1":
        add_transaction()
    elif choice == "2":
        view_transactions()
    elif choice == "3":
        show_summary()
    elif choice == "4":
        show_pie_chart()
    elif choice == "5":
        show_bar_chart()
    elif choice == "6":
        create_sample_data()
    elif choice == "7":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")