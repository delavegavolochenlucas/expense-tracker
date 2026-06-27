# Lists is a way to store data in an ordered collection of items.
# They have a pre-defined order that won't change unless you reorder them through code.
# The first item starts at [0], the second at [1], and so it goes.
# They are mutable, that means you can add, remove or change things after the list is set through code.

skills = ["BJJ", "Python", "Entrepreneurship", "Startup"]   # The list itself.

skills.append("Money")   # Append stands for add to the end of the list.
skills.pop(1)   # Pop stands for remove by position.
skills[0] = "Coding"   # Changes the first item of the list to "Coding".
print(skills[0])   # Prints the first item.
print(skills[-1])   # -1 stands for the last item of the list.