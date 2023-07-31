# TASK 3

# Asks for user input for their sugar level and converts the input to an integer
sugar_level = int(input("Provide your sugar level: "))

# Checks if the sugar level provided is less than 80
if sugar_level < 80:
    # If the sugar level is less than 80, the user is informed that their sugar level is low
    print("Your sugar level is LOW")
# Checks if the sugar level provided is more than 100
elif sugar_level > 100:
    # If the sugar level is more than 100, the user is informed that their sugar level is high
    print("Your sugar level is HIGH")
else:
    # If the sugar level is neither less than 80 nor more than 100,
    # the user is informed that their sugar level is normal
    print("Your sugar level is NORMAL")
