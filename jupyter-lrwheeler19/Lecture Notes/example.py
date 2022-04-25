# A module is code that is intended to be imported into another session
# Typically filled with function definitions

# A script is code that is inteded to be ran directly

# Ask the user for input
my_num = int(input("How many repeats do you want?"))

# Do a for loop and print positive message
for i in range(my_num):
    print(f"{i:>3d}: You are awesome")

# Print a closing message
print("Exiting now.")