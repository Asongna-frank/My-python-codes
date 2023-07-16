# TASK 1
length = 92
width = 48.8
area = length * width
print('Area =:', area)

# TASK 2
packets_of_chips = 9
cost_per_packet = 1.49
amount_paid = 20
balance = amount_paid - (packets_of_chips * cost_per_packet)
print('Balance =' + " $" + str(balance))

# TASK 3
length_square = 5.5
cost_per_square_feet = 500
area_square = length_square ** 2
total_cost = area_square * cost_per_square_feet
print('Total cost =', total_cost)

# TASK 4
num = 59
original = num
rem = 0
i = 0
while num > 0:
    rem = rem + (num % 2) * (10 ** i)
    num = num // 2
    i = i + 1
print('The binary of', original, "is", rem)
