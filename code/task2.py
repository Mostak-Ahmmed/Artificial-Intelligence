
def get_elements(tuplex):
  
    fourth_from_start = tuplex[3]

    fourth_from_end = tuplex[-4]

    return fourth_from_start, fourth_from_end


user_input = input("Enter elements of the tuple : ")
tuplex = tuple(user_input.split(','))
result = get_elements(tuplex)

print("Output:", result)
