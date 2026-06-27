# This code is an improved version of the cost manager for companies. We are using dictionaries instead of lists now.
company_name = input("What is your company name? ")   # Input asking the name of the company and storing it into the variable "company_name".
max_spendings = int(input(f"Would you like the program to send you an alert when the spendings of {company_name} reach a certain amount? Please insert the amount, and if no, please type 0. Thank you. "))   # Input asking how much should be the amount of spendings to send an alert when it is reached or exceeded, and stores it into the "max_spendings" variable.
print(f"Initializing the program for {company_name}....")   # Print saying the program will start to run.

all_expenses = {}   # Setting the empty dictionary "all_expenses".
is_accounting_open = True   # A boolean variable set to true. Will be used as reference to the loop.

while is_accounting_open:   # The actual loop, here the logic is: while the current condition of the variable "is_accounting_open" is being met, do the following:
    expense_name = input("What did you spend money on? (Type done when you are finished please.) ")   # Asks via input what did the user company spend money on, and stores the answer into the variable "expense_name". When the user is finished, he types done.

    if expense_name.lower() == 'done':   # A conditional that uses the .lower() to convert the answer stored into the "expense_name" variable into a full lowercase answer, and after it is done, the word 'done' is the result, do the following:
        break   # Stops the loop immediately.

    expense_amount = int(input(f"How much did you spend on {expense_name}? "))   # Asks via input and convert the answer into a integer how much did the user spend on the expense he typed right before, and stores it into the "expense_amount" variable.

    all_expenses[expense_name] = expense_amount   # After it is all done, go inside the "all_expenses" dictionary, place a key that will be named after the data of "expense_name" and the value that will be represented with the data inside "expense_amount".
    current_total = sum(all_expenses.values())   # Sets the variable "current_total", that its data is the sum of all the values of the whole dictionary, that are gotten from the .values() method, which ignores the keys and gets only the values.

    if current_total >= max_spendings and max_spendings > 0:   # If the variable "current_total" data is GREATER THAN the data of "max_spendings" AND "max_spendings" data is GREATER THAN 0, do the following:
        print(f"Alert! The total spendings of {company_name} have reached or exceeded ${max_spendings}. (Current total: ${current_total})")   # Prints the alert message and shows the current total of all spendings added to that moment.
        break   # Stops the loop immediately.

number_of_expenses = len(all_expenses)   # Sets the variable "number_of_expenses", which its data is equal to the number of pairs(keys and values) inside the dictionary "all_expenses".

if number_of_expenses > 0:   # If the data of the variable "number_of_expenses" is GREATER THAN 0, do the following:
    total_expenses = sum(all_expenses.values())   # Sets the variable "total_expenses", which its data is equal to the sum of all the data inside every key of the dictionary "all_expenses". That info is collected via the .values() method.
    average_expense = total_expenses / number_of_expenses   # Sets the variable "average_expense", which its data is equal to the division of the "total_expenses" variable data to the "number_of_expenses" data.
    grammatical_word = "expenses" if number_of_expenses > 1 else "expense"   # Sets tha variable "grammatical_word", which its data is 'expenses' when the "number_of_expenses" data is GREATER THAN 1, and 'expense' when it isn't. We use conditionals to check it.

    print(f"\nThe total spendings for {company_name} were ${total_expenses}.")   # Prints how much were the total expenses of the company. 
    print(f"More precisely, it was a total of {number_of_expenses} {grammatical_word}, with an average of ${average_expense:.2f} per expense.")   # Prints how many expenses were using the correct grammatical form via the "grammatical_word" variable, and the average of all of it with two decimal numbers no matter what using the :.2f format specifier.

    print("Here is your full expense breakdown:")   # Prints the first part of the full breakdown.
    for item, cost in all_expenses.items():   # Starts a for loop to get the data from the dictionaries, in this case, its keys and values.
        print(f" - {item}: ${cost}")   # Prints it all up until the dictionary ends.

    print("\nThank you for using our program. Have a great day!")   # Prints a thank you message.
    
else:   # If the above condition is FALSE, do the following:
    print("\nNo expenses were recorded. Have a great day!")   # Prints a message saying there were no expenses added.

filename = f"expenses_{company_name}.txt"

with open(filename, "w", encoding="utf-8") as f:
    f.write(f"Expense report - {company_name}\n")
    f.write("===================================\n\n")

    for item, cost in all_expenses.items():
        f.write(f"{item}: ${cost}\n")

    if number_of_expenses > 0:
        f.write(f"\nTotal spendings: ${total_expenses}\n")
        f.write(f"Number of expenses: {number_of_expenses}\n")

print(f"\nReport successfully saved as '{filename}'.")