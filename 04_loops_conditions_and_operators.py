# ---------------------------------------------
# Lesson 4: Loops, Conditions, and Operators
# Based on Engineering Animuthyam - Python DSA Part 3
# ---------------------------------------------
# This file covers:
# - for loops
# - if conditions
# - modulus operator (%)
# - logical operators (or, and)
# - solving simple problems with them
# ---------------------------------------------

# Sample list of numbers (like boxes with values)
numbers = [3, 2, 1, 5, 7, 8, 1, 4, 1, 2, 1, 4, 6]

# ---------------------------------------------
# Problem 1: Count how many times the number 1 appears
# ---------------------------------------------
count_ones = 0

for i in range(len(numbers)):
    if numbers[i] == 1:
        count_ones += 1

print("Total number of 1s:", count_ones)

# Explanation:
# - We used a loop to go through the list one item at a time
# - Inside the loop, we check if the current number is 1
# - If it is, we increase the count by 1 using count_ones += 1

# ---------------------------------------------
# Problem 2: Count numbers divisible by 3
# ---------------------------------------------
count_divisible_by_3 = 0

for num in numbers:
    if num % 3 == 0:
        count_divisible_by_3 += 1

print("Numbers divisible by 3:", count_divisible_by_3)

# Explanation:
# - The modulus operator (%) gives the remainder
# - If num % 3 == 0, it means num is exactly divisible by 3

# ---------------------------------------------
# Problem 3: Count numbers divisible by 3 OR 2
# ---------------------------------------------
count_divisible_by_3_or_2 = 0

for num in numbers:
    if num % 3 == 0 or num % 2 == 0:
        count_divisible_by_3_or_2 += 1

print("Numbers divisible by 3 OR 2:", count_divisible_by_3_or_2)

# Explanation:
# - 'or' checks if at least one condition is true
# - This counts numbers that are divisible by 3 OR divisible by 2

# ---------------------------------------------
# Problem 4: Count numbers divisible by 3 AND 2
# ---------------------------------------------
count_divisible_by_both = 0

for num in numbers:
    if num % 3 == 0 and num % 2 == 0:
        count_divisible_by_both += 1

print("Numbers divisible by BOTH 3 and 2:", count_divisible_by_both)

# Explanation:
# - 'and' checks if both conditions are true
# - This counts numbers that are divisible by both 3 AND 2

# ---------------------------------------------
# Summary:
# - % operator is used to check divisibility
# - if is used to make decisions
# - or means one of the conditions must be true
# - and means both conditions must be true
# - for loop helps you repeat actions on every item in a list
# ---------------------------------------------
