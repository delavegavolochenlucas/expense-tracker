# Here we'll see while loops. They are totally different from a for loop, while loops runs based on a BOOLEAN condition(true or false).
# The logic is all the time like: while this condition is true/false, do the following until it isn't anymore.

# Setting the variable:
countdown = 3   

while countdown > 0:   # While the variable "countdown" value is GREATER than 0, do the following:
    print(f"T-minus {countdown}")   # Prints the at the moment value of the variable "countdown".
    countdown = countdown - 1   # Updates the value of the variable to the at the moment value minus one. And then goes all the way back to the top.

print("Set for launch!")   # After the condition for the loop to finish is met, print this message.