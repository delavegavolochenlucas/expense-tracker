# My first code related to i/o (input and output).

# Ways to deal with an i/o file: 
# w(write) that opens the file to write something and erase anything that was inside it
# r(read) opens the file just to read it
# a(add) adds something to the end of the file.

# Writing a new file:
with open ("my_spendings.txt", "w", encoding="utf-8") as f:   # Opens(or creates) a new file named "my_spendings.txt", deals with it using w(write), and uses utf-8 for a greater understanding of languages, and saves it as a variable temporalily named "f".
    f.write("Lucas's spending file:\n")   # Uses the .write() method to write something inside the text file. \n is to jump a line. Same thing for the following three lines.
    f.write("====================\n")
    f.write("Spotify Premium: 24 reais.\n")
    f.write("Uber to school: 17 reais.\n")
print("File saved successfully!")   # Prints that the file was saved successfully after all the writing and closing the file for now.

# Reading the file:
with open("my_spendings.txt", "r", encoding="utf-8") as f:   # Uses r(read) to read the file "my_spendings.txt" using utf-8 and saves it as a temporarily variable named "f".
    content = f.read()   # Sets a variable named "content", which its data is all the things inside "f", that is "my_spendings.txt". We get the info inside the txt file via the .read() method.
print("\nWhat is inside this file:")   # Prepares a print for what is inside this file.
print(content)   # Prints the data of the variable content.

# Appending(add) something to the file:
with open("my_spendings.txt", "a", encoding="utf-8") as f:   # Uses a(add/append) to add something to the end of the file "my_spending.txt" using utf-8 and saves it as a temporarily variable named "f".
    f.write("Lunch: 30 reais.\n")   # Uses the .write() method to write this inside the file. The main difference from w(write) to a(add/append) is that we are not deleting something using a, only with w we do it.
print("One more thing added to the file!")   # Prints that one more thing was added to the file.

# Reading it again after all the changes:
with open("my_spendings.txt", "r", encoding="utf-8") as f:   # Uses r(read) to read the file now after all changes made, uses utf-8 and again saves it as a temporarily variable named "f".
    print("File after the changes:\n")   # Prepares the print to how the file looks like after all changes.
    print (f.read())   # Prints what is inside "f", that is "my_spendings.txt" via the .read() method.