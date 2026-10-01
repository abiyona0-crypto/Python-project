# This is for tracking expenses
print("Welcome to the Expense Tracker!")

expenses = []

while True:
    print('\n=====MENU=====')
    print('1. Add Expense')
    print('2. View Expenses')
    print('3. View Total Expenses')
    print('4. Exit')

    # Asking for the user's input
    try:
        choice = int(input('Enter your choice: '))
    except ValueError:
        print('Please enter a number between 1 and 4.')
        continue

    # 1. Add expense
    if choice == 1:
        date = input('Enter the date (DD-MM-YYYY): ')
        category = input('Enter the category of expense: ')
        description = input('Enter the description of expense: ')
        try:
            amount = float(input('Enter the amount of expense: '))
        except ValueError:
            print('Invalid amount! Expense not added.')
            continue

        expense = {
            'date': date,
            'category': category,
            'description': description,
            'amount': amount
        }
        expenses.append(expense)
        print('Expense added successfully!')

    # 2. View all the expenses
    elif choice == 2:
        if len(expenses) == 0:
            print('No expenses found!')
        else:
            print('Date\t\tCategory\tDescription\tAmount')
            for expense in expenses:
                print(f"{expense['date']}\t{expense['category']}\t{expense['description']}\t{expense['amount']}")

    # 3. View total expenses
    elif choice == 3:
        total = 0
        for expense in expenses:
            total += expense['amount']
        print(f'Total Expenses: {total}')

    # 4. Exit
    elif choice == 4:
        print('Exiting the Expense Tracker. Goodbye!')
        break

    else:
        print('Invalid choice! Please try again.')