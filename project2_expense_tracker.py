print("===== EXPENSE TRACKER =====")

total = 0

while True:
    expense = input("Enter expense amount (or type 'quit' to finish): ")

    if expense.lower() == "quit":
        break

    try:
        expense = int(expense)
        total += expense
        print("Current Total:", total)

    except ValueError:
        print("Invalid input! Please enter a valid number.")

print("\n===== EXPENSE SUMMARY =====")
print("Total Spent:", total)
print("Thank you for using Expense Tracker!")