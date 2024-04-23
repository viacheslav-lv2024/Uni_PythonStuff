input_string = input('Enter comma-separated elements: ')
element_check = ""
integer_list = []
int_dictionary = {}
rest_list = []
input_string += "," # this comma is added because without it the last element isn't added in either of two lists

for element in input_string:
    if element != ",":
        element_check += element
    else:
        if element_check.isdecimal():
            integer_list.append(int(element_check))
        else:
            rest_list.append(element_check)
        element_check = ""

for element in integer_list:
    int_dictionary.update({element: 0})
for element in integer_list:
    if element in int_dictionary:
        int_dictionary[element] += 1

print('integers:', integer_list)
print('counts:', int_dictionary)
print('rest:', rest_list)