# Problem 10: Remove duplicates from a list
# Find and fix the error

numbers = [1, 2, 2, 3, 4, 4, 5]
uniques = []
for num in numbers:
    if num not in uniques:
        uniques.append(num)
print("Unique numbers:",uniques)
