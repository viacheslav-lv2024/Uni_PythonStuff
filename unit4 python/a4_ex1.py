def split_list(lst: list, num_sublists: int) -> list:
    if num_sublists == 0:
        return lst
    main_list = []
    for i in range(num_sublists):  # creation of a nested list with num_sublists number of lists
        main_list.append([])

    for i in range(len(lst)):
        main_list[i % num_sublists].append(lst[i])

    return main_list
