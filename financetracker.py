import pandas as pd
import matplotlib.pyplot as plt

# Function to load or create settings
def load_settings():
    try:
        settings = pd.read_csv('settings.csv')
        return settings.iloc[0]['savings_goal'], settings.iloc[0]['tax_rate']
    except:
        # Default settings
        return 20, 10  # 20% savings goal, 10% tax rate

# Function to save settings
def save_settings(savings_goal, tax_rate):
    settings = pd.DataFrame({
        'savings_goal': [savings_goal],
        'tax_rate': [tax_rate]
    })
    settings.to_csv('settings.csv', index=False)

# Load settings at startup
savings_goal, tax_rate = load_settings()

def add_transaction():
    """Add a new transaction (excluding income)"""
    print("\nAdd New Transaction")
    print("-" * 20)
    
    description = input("Enter description: ")
    amount = float(input("Enter amount: ₹"))
    
    print("\nCategories:")
    print("1. Food")
    print("2. Transportation") 
    print("3. Entertainment")
    print("4. Shopping")
    print("5. Bills")
    
    choice = int(input("Select category (1-5): "))
    
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
        print("Invalid category. Defaulting to 'Other'.")
        category = "Other"
    
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
    print(f"Added: {description} - ₹{amount}")

def add_income():
    """Add income entry"""
    print("\nAdd Income")
    print("-" * 20)
    
    source = input("Enter income source (e.g., Salary, Freelance): ")
    amount = float(input("Enter amount: ₹"))
    
    # Save to CSV
    new_data = pd.DataFrame({
        'Description': [source],
        'Amount': [amount],
        'Category': ['Income']
    })
    
    try:
        existing_data = pd.read_csv('transactions.csv')
        all_data = pd.concat([existing_data, new_data])
    except:
        all_data = new_data
    
    all_data.to_csv('transactions.csv', index=False)
    print(f"Added income: {source} - ₹{amount}")

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
    """Show pie chart of spending including savings"""
    try:
        data = pd.read_csv('transactions.csv')
        total_income = data[data['Category'] == 'Income']['Amount'].sum()
        expenses = data[data['Category'] != 'Income']
        total_spent = expenses['Amount'].sum()
        saved = total_income - total_spent
        category_spending = expenses.groupby('Category')['Amount'].sum().to_dict()
        if saved > 0:
            category_spending['Savings'] = saved
        labels = list(category_spending.keys())
        values = list(category_spending.values())
        plt.figure(figsize=(10, 7))
        plt.pie(values, labels=labels, autopct='%1.1f%%')
        plt.title('Spending and Savings by Category')
        plt.axis('equal')
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"No data to show!")

def show_bar_chart():
    """Show bar chart of spending, actual savings, and target savings"""
    try:
        data = pd.read_csv('transactions.csv')
        total_income = data[data['Category'] == 'Income']['Amount'].sum()
        expenses = data[data['Category'] != 'Income']
        total_spent = expenses['Amount'].sum()
        saved = total_income - total_spent
        target_savings = total_income * (savings_goal / 100)
        category_spending = expenses.groupby('Category')['Amount'].sum().to_dict()
        # Add savings bars
        category_spending['Actual Savings'] = saved if saved > 0 else 0
        category_spending['Target Savings'] = target_savings
        plt.figure(figsize=(12, 7))
        bars = plt.bar(category_spending.keys(), category_spending.values(), color=['#4e79a7']*len(category_spending))
        # Highlight savings bars
        bars[-2].set_color('#59a14f')  # Actual Savings
        bars[-1].set_color('#f28e2b')  # Target Savings
        plt.title('Spending, Actual Savings, and Target Savings')
        plt.xlabel('Category')
        plt.ylabel('Amount (₹)')
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"No data to show!")

def show_summary():
    """Show spending summary with savings goals and tax calculations"""
    try:
        data = pd.read_csv('transactions.csv')
        total_spent = 0
        total_income = 0
        for i in range(len(data)):
            if data.iloc[i]['Category'] == 'Income':
                total_income = total_income + data.iloc[i]['Amount']
            else:
                total_spent = total_spent + data.iloc[i]['Amount']
        saved = total_income - total_spent
        savings_percentage = (saved / total_income * 100) if total_income > 0 else 0
        estimated_tax = total_income * (tax_rate / 100)
        after_tax_income = total_income - estimated_tax
        target_savings = total_income * (savings_goal / 100)
        savings_difference = saved - target_savings
        print("\n💰 Financial Summary")
        print("=" * 30)
        print(f"Total Income: ₹{total_income:.2f}")
        print(f"Estimated Tax ({tax_rate}%): ₹{estimated_tax:.2f}")
        print(f"After-Tax Income: ₹{after_tax_income:.2f}")
        print(f"Total Spent: ₹{total_spent:.2f}")
        print(f"Money Saved: ₹{saved:.2f} ({savings_percentage:.1f}%)")
        print("-" * 30)
        print(f"Savings Goal: {savings_goal}% (₹{target_savings:.2f})")
        if savings_difference >= 0:
            print(f"✅ Congratulations! You exceeded your savings goal by ₹{savings_difference:.2f}")
            if savings_percentage > 30:
                print("🌟 Outstanding! You're saving like a pro!")
            else:
                print("👍 Good job on meeting your savings target!")
        else:
            print(f"❌ You missed your savings goal by ₹{abs(savings_difference):.2f}")
            print("💡 Tip: Try to reduce spending in your largest expense category.")
    except:
        print("No data to show!")

def show_saving_goals():
    """Show current savings goal and tax rate"""
    print("\n🎯 Your Current Financial Goals")
    print("=" * 30)
    print(f"Savings Goal: {savings_goal}% of your income")
    print(f"Tax Rate: {tax_rate}%")
    print("You can update these anytime from the menu.")

def create_sample_data():
    """Create sample data for testing"""
    sample_data = pd.DataFrame({
        'Description': ['Salary', 'Groceries', 'Gas', 'Movie', 'Clothes', 'Electric Bill'],
        'Amount': [10000, 1500, 800, 400, 1200, 900],
        'Category': ['Income', 'Food', 'Transportation', 'Entertainment', 'Shopping', 'Bills']
    })
    sample_data.to_csv('transactions.csv', index=False)
    print("Sample data created!")

def set_savings_goal():
    """Set savings goal percentage"""
    global savings_goal
    print("\nSet Savings Goal")
    print("-" * 20)
    print(f"Current savings goal: {savings_goal}%")
    try:
        new_goal = float(input("Enter new savings goal percentage: "))
        if new_goal < 0 or new_goal > 100:
            print("Savings goal must be between 0 and 100%")
            return
        savings_goal = new_goal
        save_settings(savings_goal, tax_rate)
        print(f"Savings goal updated to {savings_goal}%")
    except:
        print("Invalid input. Please enter a number.")

def set_tax_rate():
    """Set income tax rate"""
    global tax_rate
    print("\nSet Income Tax Rate")
    print("-" * 20)
    print(f"Current tax rate: {tax_rate}%")
    try:
        new_rate = float(input("Enter income tax percentage: "))
        if new_rate < 0 or new_rate > 100:
            print("Tax rate must be between 0 and 100%")
            return
        tax_rate = new_rate
        save_settings(savings_goal, tax_rate)
        print(f"Tax rate updated to {tax_rate}%")
    except:
        print("Invalid input. Please enter a number.")

# Main program starts here
print("💰 Personal Finance Tracker 💰")
print("=" * 40)

# Ask for user's name
user_name = input("Welcome! Please enter your name: ")
print(f"\nHello, {user_name}! Let's manage your finances.")

# Make income entry mandatory
print("\n📋 Initial Setup (Required)")
print("-" * 30)
print("Please enter your income to continue.")
add_income()

# Check if user wants to set savings goal and tax rate immediately
print("\nWould you like to set up your financial goals now?")
setup_choice = input("Set savings goal and tax rate? (y/n): ").lower()

if setup_choice == 'y':
    set_savings_goal()
    set_tax_rate()
else:
    print(f"Using default settings: {savings_goal}% savings goal, {tax_rate}% tax rate")

while True:
    print(f"\nMenu for {user_name}:")
    print("1. Add Transaction")
    print("2. Add Income")
    print("3. View Transactions")
    print("4. Show Summary")
    print("5. Show Pie Chart")
    print("6. Show Bar Chart")
    print("7. Show Saving Goals")
    print("8. Create Sample Data")
    print("9. Set Savings Goal (currently {:.1f}%)".format(savings_goal))
    print("10. Set Tax Rate (currently {:.1f}%)".format(tax_rate))
    print("11. Exit")
    
    choice = input("Choose option (1-11): ")
    
    if choice == "1":
        add_transaction()
    elif choice == "2":
        add_income()
    elif choice == "3":
        view_transactions()
    elif choice == "4":
        show_summary()
    elif choice == "5":
        show_pie_chart()
    elif choice == "6":
        show_bar_chart()
    elif choice == "7":
        show_saving_goals()
    elif choice == "8":
        create_sample_data()
    elif choice == "9":
        set_savings_goal()
    elif choice == "10":
        set_tax_rate()
    elif choice == "11":
        print(f"Goodbye, {user_name}! Keep saving! 💰")
        break
    else:
        print("Invalid choice!")