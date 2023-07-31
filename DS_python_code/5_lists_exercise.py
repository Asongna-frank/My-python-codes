# TASK 1
"""Let us say your expense for every month are listed below,
January - 2200
February - 2350
March - 2600
April - 2130
May - 2190
Create a list to store these monthly expenses and using that find out"""
monthly_expenses = [2200, 2350, 2600, 2130, 2190]

# Q1. In Feb, how many dollars you spent extra compare to January?
extra = monthly_expenses[1] - monthly_expenses[0]
print('Etra:', extra)

# Q2. Find out your total expense in first quarter (first three months) of the year.
total_expense = monthly_expenses[0] + monthly_expenses[1] + monthly_expenses[2]
print(f'Total expense: ${total_expense}')

# Q3. Find out if you spent exactly 2000 dollars in any month.
print(f'Presence of 2000 in expenses: {2000 in monthly_expenses}')

# Q4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
monthly_expenses.append(1980)
print(monthly_expenses)

# Q5. You returned an item that you bought in the month of April and
#     got a refund of 200$. Make a correction to your monthly expense list based on this
monthly_expenses[3] = monthly_expenses[3] - 200
print(monthly_expenses)


# TASK 2
# You have a list of your favourite marvel super heroes.
heroes = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']

# Q1. Length of the list
print(f'\n\n The length of the list is: {len(heroes)}')

# Q2. Add 'black panther' at the end of this list
heroes.append('black panther')
print(f'\n{heroes}')

# Q3. You realize that you need to add 'black panther' after 'hulk',
#   so remove it from the list first and then add it after 'hulk'
heroes.remove('black panther')
heroes.insert(3, 'black panther')
print(f'\n{heroes}')

# Q4. Now you don't like thor and hulk because they get angry easily :)
#   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#   Do that with one line of code.
heroes[1:3] = ['doctor strange']
print(f'\n{heroes}')

# Q5. Sort the heroes list in alphabetical order
# (Hint. Use dir() functions to list down all functions available in list)
heroes.sort()
print(f'\n{heroes}')
