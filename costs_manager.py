company_name = input("What is the name of your company? ")
max_spendings = int(input(f"Would you like the program to alert you when the total spendings of {company_name} reach a certain amount? If yes, please enter the amount. If no, please enter 0. "))
print(f"Initializing the program for {company_name}...")

all_expenses = []
is_accounting_open = True

while is_accounting_open:
    expense_amount = int(input("What is the amount of the expense you want to add? And when you are done, please enter 0: "))

    if expense_amount == 0:
        break
    
    else:
        all_expenses.append(expense_amount)
        if sum(all_expenses) >= max_spendings and max_spendings > 0:
            print(f"Alert! The total spendings for {company_name} have reached ${max_spendings}.")
            break
        number_of_expenses = len(all_expenses)
        print(f"Expense added! You have added {number_of_expenses} expenses so far.")

if len(all_expenses) > 0:
    total_expenses = sum(all_expenses)
    number_of_expenses = len(all_expenses)
    average_expense = total_expenses / number_of_expenses

if number_of_expenses > 1:
    print(f"The total spendings for {company_name} are ${total_expenses}. More precisely, it was a total of {number_of_expenses} expenses, with an average of ${average_expense} per expense.")
    print("Thank you for using our accounting program. Have a great day!")
else:
    print(f"The total spending for {company_name} is ${total_expenses}. More precisely, it was a total of {number_of_expenses} expense, with an average of ${average_expense} per expense.")
    print("Thank you for using our accounting program. Have a great day!")