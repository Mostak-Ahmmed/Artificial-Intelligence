def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

numbers = input("Enter numbers: ").split()

numbers = [int(num) for num in numbers]
result = sum_numbers(*numbers)
print("Sum:", result)
