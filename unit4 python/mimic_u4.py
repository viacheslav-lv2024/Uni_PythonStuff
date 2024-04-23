lst = [0,1,2,3,4,5,6,7]
num_sublists = int(input())
main_list = []

for i in range(num_sublists): #creation of a nested list with num_sublists number of lists
    main_list.append([])
    
for i in range(len(lst)):
    main_list[i%num_sublists].append(lst[i])

print(main_list)