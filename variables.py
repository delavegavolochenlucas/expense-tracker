# Variables are a reserved memory location to store a kind of data that your program can manipulate, update and reuse.
# Think of it like a labeled storage box. The label on the box is the variable's name, and the item inside is the variable value. 
# Instead of remembering exact numbers, texts, or data structures, you give them a descriptive name in order to work easily with them.

name = input("What is your name? ")   # Asks the user via input what is his name, and stores the answer given inside the variable "name".
age = int(input("How old are you? "))   # Asks the user via input what is his age, uses the 'int' function to certify if the answer is transformed into an integer (whole number), and stores the data into the variable "age".
print(f"{name} is {age} years old.")   # Prints in the terminal: name is age years old. In reality, 'name' and 'age' will be printed out, respectively, as the values from the "name" and "age" variables.