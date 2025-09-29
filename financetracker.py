import pandas as pd
import matplotlib.pyplot as plt

print("Welcome to Finance Tracker\n")
try:
    settings = pd.read_csv("settings.csv")
    tax_rate = float(settings.iloc[0]["tax_rate"])
    goal = float(settings.iloc[0]["savings_goal"])
except:
    print("Please set the following values")
    income = float(input("Income: "))
    tax_rate = float(input("Tax Rate (%): "))
    goal = float(input("Savings Goal (%): "))
    pd.DataFrame({"tax_rate": [tax_rate], "savings_goal": [goal]}).to_csv(
        "settings.csv", index=False
    )
    transactions = pd.DataFrame(
        {"Description": ["Initial Income"], "Amount": [income], "Category": ["Income"]}
    )
    transactions.to_csv("transactions.csv", index=False)


print("\nPlease choose one of the following options to continue\n")
print("1. Add Transaction")
print("2. Add Income")
print("3. View Transactions")
print("4. Show Summary")
print("5. Show Pie Chart")
print("6. Show Bar Chart")
print("7. Show savings goal")
print("8. Set savings goal")
print("9. Set tax rate")
print("10. Show this menu")
print("11. Exit\n")

while True:
    choice = int(input("Please enter your choice (1-11): "))

    if choice == 1:
        print("\nPlease choose a category for your expense:")
        print("1. Food")
        print("2. Transportation")
        print("3. Entertainment")
        print("4. Shopping")
        print("5. Others")
        cat_num = int(input("Enter 1-5: "))
        if cat_num == 1:
            category = "Food"
        elif cat_num == 2:
            category = "Transportation"
        elif cat_num == 3:
            category = "Entertainment"
        elif cat_num == 4:
            category = "Shopping"
        else:
            category = "Others"
        desc = input("Description: ")
        if desc == "":
            desc = category
        amt = float(input("Amount: "))

        try:
            old = pd.read_csv("transactions.csv")
            new_row = pd.DataFrame(
                {"Description": [desc], "Amount": [amt], "Category": [category]}
            )
            all_data = pd.concat([old, new_row], ignore_index=True)
        except:
            all_data = pd.DataFrame(
                {"Description": [desc], "Amount": [amt], "Category": [category]}
            )
        all_data.to_csv("transactions.csv", index=False)
        print("Transaction added.\n")

    elif choice == 2:
        src = input("Income source: ").strip()
        if src == "":
            src = "Income"
        amt = float(input("Amount: "))
        try:
            old = pd.read_csv("transactions.csv")
            new_row = pd.DataFrame(
                {"Description": [src], "Amount": [amt], "Category": ["Income"]}
            )
            all_data = pd.concat([old, new_row], ignore_index=True)
        except:
            all_data = pd.DataFrame(
                {"Description": [src], "Amount": [amt], "Category": ["Income"]}
            )
        all_data.to_csv("transactions.csv", index=False)
        print("Income added.\n")

    elif choice == 3:
        d = pd.read_csv("transactions.csv")
        if d.empty:
            print("No transactions yet.\n")
        else:
            print("\nTransactions:")
            print(d, "\n")

    elif choice == 4:
        d = pd.read_csv("transactions.csv")
        if d.empty:
            print("No data to show.\n")
        else:
            income = 0
            expenses = 0
            for i in range(len(d)):
                category = d["Category"].iloc[i]
                amount = float(d["Amount"].iloc[i])
                if category == "Income":
                    income = income + amount
                else:
                    expenses = expenses + amount
            saved = income - expenses
            target = income * (goal / 100.0)
            estimated_tax = income * (tax_rate / 100.0)
            print("\nSummary:")
            print("Total Income:", float(income))
            print("Total Expenses:", float(expenses))
            print("Saved:", float(saved))
            print("Savings Goal Target (", goal, "% of income ):", float(target))
            print("Estimated Tax (", tax_rate, "% of income ):", float(estimated_tax))

    elif choice == 5:
        d = pd.read_csv("transactions.csv")
        exp_rows = []
        for i in range(len(d)):
            if d["Category"].iloc[i] != "Income":
                exp_rows.append(d.iloc[i])
        exp = pd.DataFrame(exp_rows)
        if exp.empty:
            print("No expenses to plot yet.\n")
            continue
        cats = {}
        for i, row in exp.iterrows():
            k = row["Category"]
            v = float(row["Amount"])
            if k in cats:
                cats[k] += v
            else:
                cats[k] = v
        if sum(cats.values()) <= 0:
            print("Nothing to plot yet.\n")
            continue
        plt.figure()
        plt.pie(list(cats.values()), labels=list(cats.keys()))
        plt.title("Expenses by Category")
        plt.show()

    elif choice == 6:
        d = pd.read_csv("transactions.csv")
        if d.empty:
            print("No data to show.\n")
            continue
        income = d[d["Category"] == "Income"]["Amount"].sum()
        exp = d[d["Category"] != "Income"]
        expenses_total = exp["Amount"].sum()
        saved = income - expenses_total
        target = income * (goal / 100.0)
        cats = {}
        for i, row in exp.iterrows():
            k = row["Category"]
            v = float(row["Amount"])
            if k in cats:
                cats[k] += v
            else:
                cats[k] = v
        if saved > 0:
            cats["Actual Savings"] = float(saved)
        else:
            cats["Actual Savings"] = 0.0
        cats["Target Savings"] = float(target)
        names = list(cats.keys())
        values = list(cats.values())
        plt.figure()
        plt.bar(names, values)
        plt.xticks(rotation=30, ha="right")
        plt.ylabel("Amount")
        plt.title("Expenses and Savings")
        plt.tight_layout()
        plt.show()

    elif choice == 7:
        print("\nCurrent Settings:")
        print("Savings Goal (%):", float(goal))
        print("Tax Rate (%):", float(tax_rate))
        print()

    elif choice == 8:
        goal = float(input("New savings goal (%): "))
        pd.DataFrame({"tax_rate": [tax_rate], "savings_goal": [goal]}).to_csv(
            "settings.csv", index=False
        )
        print("Savings goal saved.\n")

    elif choice == 9:
        tax_rate = float(input("New tax rate (%): "))
        pd.DataFrame({"tax_rate": [tax_rate], "savings_goal": [goal]}).to_csv(
            "settings.csv", index=False
        )
        print("Tax rate saved.\n")

    elif choice == 10:
        print("\nPlease choose one of the following options to continue\n")
        print("1. Add Transaction")
        print("2. Add Income")
        print("3. View Transactions")
        print("4. Show Summary")
        print("5. Show Pie Chart")
        print("6. Show Bar Chart")
        print("7. Show savings goal")
        print("8. Set savings goal")
        print("9. Set tax rate")
        print("10. Show this menu")
        print("11. Exit\n")

    elif choice == 11:
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 11.\n")
