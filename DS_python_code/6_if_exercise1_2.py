# TASK 2

# Lists of cities in India, Pakistan, and Bangladesh
india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

# Input of two cities from the user
city_1 = input("Please enter the 1st city: ")
city_2 = input("Please enter the 2nd city: ")

# Conditional checks to see if both cities are in the same country
if city_2 in india and city_1 in india:
    # If both cities are in India, this message will be printed
    print('Both cities are in India')
elif city_2 in pakistan and city_1 in pakistan:
    # If both cities are in Pakistan, this message will be printed
    print('Both cities are in Pakistan')
elif city_2 in bangladesh and city_1 in bangladesh:
    # If both cities are in Bangladesh, this message will be printed
    print('Both cities are in Bangladesh')
else:
    # If the cities do not belong to the same country, this message will be printed
    print('They don\'t belong to the same country')
