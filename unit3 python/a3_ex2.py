user_input = input('Enter element or \'x\' when done: ')
all_elements = []
sorted_elements = []

while user_input != 'x':
    all_elements.append(user_input)
    user_input = input('Enter element or \'x\' when done: ')

for element in all_elements:
    if not (element in sorted_elements):
        sorted_elements.append(element)

sorted_elements.sort()

print('all:', all_elements)
print('unique (sorted):', sorted_elements)
        
