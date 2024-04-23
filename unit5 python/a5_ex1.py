def sub_summarize(nested: list, sub_sums: list) -> int:
    summ = 0
    for element in nested:
        if isinstance(element, list):
            sub_sum = sub_summarize(element, sub_sums)
            summ += sub_sum
        elif isinstance(element, int):
            summ += element
    else:
        sub_sums.append(summ)
    return summ
