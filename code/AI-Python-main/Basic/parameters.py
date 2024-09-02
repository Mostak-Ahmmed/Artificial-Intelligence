def find_sum(*args):
    return sum(args)


numbers = (1, 2, 3, 4, 5)
total_sum = find_sum(*numbers)
print(f"The sum of the numbers {numbers} is: {total_sum}")
