def find_second_highest(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    return unique_numbers[-2]

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
second_highest = find_second_highest(numbers)
print(f"Second highest number: {second_highest}")
