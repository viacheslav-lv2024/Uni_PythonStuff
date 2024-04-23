def clip(*values, min_=0, max_=1) -> list:
    local_list = []
    for element in values:
        if element < min_:
            local_list.append(min_)
        elif element > max_:
            local_list.append(max_)
        else:
            local_list.append(element)
    return local_list
            