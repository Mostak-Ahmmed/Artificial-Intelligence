def swap_tuples(tup1, tup2):
    return tup2, tup1

# Example usage
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple1, tuple2 = swap_tuples(tuple1, tuple2)
print(f"Tuple 1 after swapping: {tuple1}")
print(f"Tuple 2 after swapping: {tuple2}")
