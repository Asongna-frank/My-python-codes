# TASK 1

# Define a list of cities in India
india = ["mumbai", "banglore", "chennai", "delhi"]

# Define a list of cities in Pakistan
pakistan = ["lahore","karachi","islamabad"]

# Define a list of cities in Bangladesh
bangladesh = ["dhaka", "khulna", "rangpur"]

# Ask the user to input a city name
city = input("Enter your city name: ")

# Check if the input city is in the list of Indian cities
if city in india:
    # If the city is found in India, print a message saying so
    print(f'{city} is found in India')

# If the city is not found in India, check if it is in the list of Pakistani cities
elif city in pakistan:
    # If the city is found in Pakistan, print a message saying so
    print(f'{city} is found in Pakistan')

# If the city is not found in either India or Pakistan, check if it is in the list of Bangladeshi cities
elif city in bangladesh:
    # If the city is found in Bangladesh, print a message saying so
    print(f'{city} is found in Bangladesh')

# If the city is not found in any of the three lists
else:
    # Print a message indicating that the country of the city is not known
    print(f"From the knowledge I have,\nI don't know which country {city} is found in")
