def get_fourth_elements(tup):
    if len(tup) < 4:
        return "The tuple is too short to have a 4th element."
    
    fourth_from_start = tup[3]
    fourth_from_end = tup[-4]
    
    return fourth_from_start, fourth_from_end

# Example usage
example_tuple = (10, 20, 30, 40, 50, 60, 70, 80)
result = get_fourth_elements(example_tuple)

if isinstance(result, tuple):
    print(f"The 4th element from the beginning is: {result[0]}")
    print(f"The 4th element from the end is: {result[1]}")
else:
    print(result)
