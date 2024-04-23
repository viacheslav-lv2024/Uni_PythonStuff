def binary_search(sorted_list: list, number: int, high=200, low=0):
    center = (high+low)//2
    if sorted_list[center] == number:
        return center
    elif sorted_list[center] < number:
        return binary_search(sorted_list, number, high=high, low=center) 
    elif sorted_list[center] > number:
        return binary_search(sorted_list, number, high=center, low=low)


arb_list = range(100, 201)
print(arb_list)
print("LIST LOADED")
print(binary_search(arb_list, int(input("Which number do you want to search? "))))
            