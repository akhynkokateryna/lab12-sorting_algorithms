"algorithms.py"

def linear_search(list_of_values, value):
    """
    Executes the linear search and returns its index if its found, else returns -1
    >>> linear_search(['mom', 'dad'], 'dad')
    1
    >>> linear_search(['mom', 'dad'], 'aunt')
    -1
    """
    if value in list_of_values:
        for index, item in enumerate(list_of_values):
            if item == value:
                return index
    else:
        return -1


def merge_sort(lst):
    """
    Splits main list into lists with two elements and sends them to merge function
    >>> merge_sort([5, 10, 6, 8, 15, 2, 9, 20])
    [2, 5, 6, 8, 9, 10, 15, 20]
    """
    if len(lst) > 1:
        mid = len(lst) // 2
        lst1, lst2 = lst[:mid], lst[mid:]
        merge_sort(lst1)
        merge_sort(lst2)
        return merge(lst1, lst2, lst)

def merge(lst1, lst2, lst):
    "Executes merge sorting using lists from merge_sort function"
    index1 = index2 = index = 0
    len1, len2 = len(lst1), len(lst2)

    while index1 < len1 and index2 < len2:
        if lst1[index1] < lst2[index2]:
            lst[index] = lst1[index1]
            index1 += 1
        else:
            lst[index] = lst2[index2]
            index2 += 1
        index += 1

    while index1 < len(lst1):
        lst[index] = lst1[index1]
        index1 += 1
        index += 1

    while index2 < len(lst2):
        lst[index] = lst2[index2]
        index2 += 1
        index += 1

    return lst


def binary_search(list_of_values, value):
    """
    Executes binary search and returns index of element if its found, else returns -1
    >>> binary_search([5, 10, 6, 8], 8)
    3
    >>> binary_search([5, 10, 6, 8], 12)
    -1
    """
    if value in list_of_values:
        initial = 0
        right = len(list_of_values)
        while initial != right + 1:
            medium = (initial + right) // 2
            if list_of_values[medium] < value:
                initial = medium + 1
            else:
                right = medium - 1
        if 0 <= initial < len(list_of_values) and list_of_values[initial] == value:
            return initial
    else:
        return -1


def selection_sort(lst):
    """
    Executes a selection sort
    >>> selection_sort([5, 10, 6, 8])
    [5, 6, 8, 10]
    """
    lenght = len(lst)
    for nums in range(lenght-1):
        lowest = nums
        for item in range(lowest+1, lenght):
            if lst[item] < lst[lowest]:
                lowest = item
        lst[nums], lst[lowest] = lst[lowest], lst[nums]
    return lst


def quick_sort(lst):
    """
    Executes a quick sort
    >>> quick_sort([5, 10, 6, 8])
    [5, 6, 8, 10]
    """
    less = []
    more = []
    key = lst[0]
    for item in lst:
        if item < key:
            less.append(item)
        elif item > key:
            more.append(item)
    if len(less)>0:
        less = quick_sort(less)
    if len(more)>0:
        more = quick_sort(more)
    return less + [key] + more
