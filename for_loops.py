# Loop is a structure to execute a block of code repeatedly until a specific condition is met, or all items in a collection have been processed.
# We usually use loops to copy and past a block of code several times, we just use a loop to automate it efficently.
# The type "for" of loops are used when you want to read a sequence(like a list, dictionary, a string, or a range of numbers).

# Reading a list:
guests = ["Lucas", "Mateo", "Leonardo"]   # Here we set a list with three guest names.

for name in guests:   # The loop is set right here. He will go to the list "guests", pick the first item, put inside the variable "name", and print it. After that, he will go to the list again, pick the next item, and update the variable "name" with it. And so goes on until the list is finished.
    print(f"Hello, {name}! You are invited to my party.")   # He will print this message 3 times because there are 3 items inside our list. Each message will be different because the variable name is updated everytime the loop reads the list and picks the next item.

# Using the range() function. Used to repeat integer numbers a specific number of times.
for attempt in range(1,5):   # The loop is set. The logic here is: "start counting at 1, and keep going as long as the number is LESS than 5".
    print(f"Attempt number {attempt}")   # Prints out the logic above until it reaches 5, then the loop stops, because the condition was met for it to end.

# Reading a dictionary:
user_profile = {
    "username": "coder123",
    "country": "Brazil",                # Here we set a normal dictionary, with keys and values.
    "language": "Portuguese",
}
# Through ONLY the key:
for key in user_profile:   # Not that complicated, when you ask to Python for .... in user_profile for DICTIONARIES, the default behavior is to give you only the KEY. So the loop goes over to the dictionary, grabs the key, put inside the variable "key", goes back to the loop, picks the next key, updates the variable, and so goes on up unitl the dictionary is finished.
    print(key)   # Prints all the three keys.

# Through the key AND value:
for key, value in user_profile.items():   # Here, the logic is: the .items() method temporarily transforms our dictionary into a list-like collection of tuples(pairs). So, our dictionary will look like this [ ("username", "coder123"), ...] and so goes on up until the last key and value. Then, we pick the first item in our list-like FIRST pair, in this case "username", and put it inside the variable "key", and pick the second item in our list-like FIRST PAIR and put it inside the variable "value". And so goes on to the second and third pair in this case.
    print(f"The profile {key} holds the value {key}")   # Prints both the keys and values of the whole dictionary right now.