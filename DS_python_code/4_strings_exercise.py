# TASK 1
street = 'Mile 16'
city = 'Buea'
country = 'Cameroon'

# Storing the string in such a way that each variable appears in a new line
address_method_1 = street + '\n' + city + '\n' + country  # using the + operator to store the string
address_method_2 = f'{street}\n{city}\n{country}'  # using the f-string operator to store the string

print('Using + operator:', '\n' + address_method_1)
print('\n' + 'Using f-string operator:', '\n' + address_method_2)

# TASK 2
text = 'Earth revolves around the sun'
print('\n' + text[6:14])  # printing 'revolves' using the slice operator
print(text[-3:])  # printing 'sun' using negative index

# TASK 3
fruits = 5
vegetables = 8

# using f-string to print certain variable values in a string
print('\n' + f'I eat {vegetables} veggies and {fruits} fruits daily')

# TASK 4
s = 'maine 200 banana khaye'

# printing a corrected text by using the replace() to correct the text
s = s.replace('200','10').replace('banana','samosa')
print('\n' + s)