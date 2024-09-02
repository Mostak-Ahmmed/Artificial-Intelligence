def sum_divisible_by_3_not_5():
    return sum(n for n in range(50, 101) if n % 3 == 0 and n % 5 != 0)

result = sum_divisible_by_3_not_5()
print(f"Sum of numbers between 50 and 100 divisible by 3 and not by 5: {result}")
