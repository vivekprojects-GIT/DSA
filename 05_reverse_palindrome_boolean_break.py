# ---------------------------------------------
# Lesson 5: Reverse, Palindrome, Boolean, Break
# ---------------------------------------------
# This file covers:
# - How to reverse a string
# - How to check if a string is a palindrome
# - Using boolean variables (True/False)
# - How and why to use break inside a loop
# ---------------------------------------------


# ---------------------------------------------
# Problem 1: Reverse a string
# Example: "notebook" becomes "koobeton"
# ---------------------------------------------

input_string = "notebook"
reversed_string = ""

# Loop through the string from last to first character
for index in range(len(input_string) - 1, -1, -1):
    reversed_string += input_string[index]  # Add each character to the new string

print("Reversed string:", reversed_string)

# 💡 Explanation:
# - The string is read in reverse using range(start, stop, step)
# - We go from the last character (len-1) to the first (0), one step at a time (-1)
# - Each character is added to a new string


# ---------------------------------------------
# Problem 2: Check if a string is a palindrome (Method 1)
# A palindrome is the same forward and backward
# Examples: "madam", "racecar", "level"
# ---------------------------------------------

word_to_check = "madam"
reversed_word = ""

# Reverse the word manually using a loop
for index in range(len(word_to_check) - 1, -1, -1):
    reversed_word += word_to_check[index]

# Compare reversed word with the original
if word_to_check == reversed_word:
    print("Yes, it is a palindrome (Method 1)")
else:
    print("No, it is not a palindrome (Method 1)")

# 💡 Explanation:
# - We build a reversed string
# - If the reversed string is the same as the original, it's a palindrome


# ---------------------------------------------
# Problem 3: Check if a string is a palindrome (Method 2)
# This time, we compare letters from front and back
# ---------------------------------------------

word_to_check = "level"
is_palindrome = True  # Boolean variable, initially assume it's a palindrome

# Only need to check up to the middle of the string
for i in range(len(word_to_check) // 2):
    # Compare character from start and end
    if word_to_check[i] != word_to_check[len(word_to_check) - i - 1]:
        is_palindrome = False  # Mismatch found
        break  # Exit the loop early

# Final decision
if is_palindrome:
    print("Yes, it is a palindrome (Method 2)")
else:
    print("No, it is not a palindrome (Method 2)")

# 💡 Explanation:
# - Check one character from the front and one from the end in each loop
# - If a mismatch is found, set `is_palindrome` to False and stop
# - This method is faster and uses less memory


# ---------------------------------------------
# Summary:
# - You can reverse a string using a loop and string concatenation
# - Palindromes are strings that read the same forward and backward
# - Two ways to check palindromes:
#     1. Reverse and compare
#     2. Use indexes from both ends and compare
# - Boolean values (True/False) store decisions
# - The `break` keyword helps you exit a loop early if a condition is met
# ---------------------------------------------
