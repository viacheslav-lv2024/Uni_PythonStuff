def sort(elements: list, ascending: bool = True):
    if ascending:
        for i in range(len(elements) - 1):
            for j in range(i, len(elements)):
                if elements[i] > elements[j]:
                    elements[i], elements[j] = elements[j], elements[i] # changing values of 2 variables without adding a new var
    else:
        for i in range(len(elements) - 1):
            for j in range(i, len(elements)):
                if elements[i] < elements[j]:
                    elements[i], elements[j] = elements[j], elements[i]

        