def sort(list):
    """
    Просто находится меньший элемент и ставится в начало
    :param list: исходный массив
    :return: отсортированный массив
    """
    for i in range(len(list) - 1):
        minimum = min(list[i:])

        buf, list[i] = list[i], minimum

        for k in range(i + 1, len(list)):
            if minimum == list[k]:
                list[k] = buf
                break

    return list
