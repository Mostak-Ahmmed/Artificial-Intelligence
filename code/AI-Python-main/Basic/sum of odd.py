def sum_odd_even(numbers):
    sum_odd = sum(n for n in numbers if n % 2 != 0)
    sum_even = sum(n for n in numbers if n % 2 == 0)
    return sum_odd, sum_even

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_odd, sum_even = sum_odd_even(numbers)
print(f"Sum of odd numbers: {sum_odd}")
print(f"Sum of even numbers: {sum_even}")
