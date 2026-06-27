# A quick drill on lists.
my_gear = ["Iphone", "Airpods", "PC"]   # Sets the list.
new_gear = input("What new gear do you want? ")   # Asks through input if the user wants any new gear.
my_gear.append(new_gear)   # Appends (adds) that new gear to the end of the list.
my_gear[1] = "Macbook"   # Changes the second item in the list to "Macbook".
my_gear.pop()   # Pops (removes) the last item in the list.
print(f"Your gear is now: {my_gear} and you have {len(my_gear)} items in your gear list.")   # Prints a message in the terminal showing how the list is after all the code, and through the len function, returns how much gears are in the list.