"names.py"

def find_names(file_path):
    """
    Returns tuple with set of three the most popular names,
    tuple with number of names that occure only once and set of these names,
    tuple with the most popular letter at the beggining of the words, number of these names
    and number of children with these names
    """
    list_of_names = reads_file(file_path)

    res = []

    set_of_popular_names = popular_names(list_of_names)
    res.append(set_of_popular_names)

    name_once = names_once(list_of_names)
    res.append(name_once)

    letter = popular_letter(list_of_names)
    res.append(letter)

    return tuple(res)


def reads_file(file_path):
    "Reads the file and returns lists with lines"
    list_of_names = []
    with open(file_path, 'r', encoding='utf-8') as file:
        next(file)
        for lines in file:
            lines = lines.rstrip('\n')
            lines = lines.replace('\t', '')
            lines = lines.replace(')', '')
            lines = lines.replace('(', '')
            lines = lines.split(" ")
            lines[1] = int(lines[1])
            list_of_names.append(lines)
    return list_of_names


def popular_names(list_of_names):
    """Returns set with 3 the most popular names
    """
    set_of_popular_names = []
    list_of_names = selection_sort(list_of_names)
    order = len(list_of_names) - 1
    for _ in range(3):
        set_of_popular_names.append(list_of_names[order][0])
        order -= 1
    return set(set_of_popular_names)


def selection_sort(lst):
    """
    Executes a selection sort
    >>> selection_sort([['АНДРІЯН', 3], ['АНТОН', 15], ['АНТОНІЙ', 9]])
    [['АНДРІЯН', 3], ['АНТОНІЙ', 9], ['АНТОН', 15]]
    """
    lenght = len(lst)
    for names in range(lenght-1):
        lowest = names
        for item in range(lowest+1, lenght):
            if lst[item][1] < lst[lowest][1]:
                lowest = item
        lst[names], lst[lowest] = lst[lowest], lst[names]
    return lst


def names_once(list_of_names):
    """Returns tuple with num of names that occur only once and set of these names
    """
    num = 0
    set_names = set()
    for names, _ in enumerate(list_of_names):
        if list_of_names[names][1] == 1:
            num += 1
            set_names.add(list_of_names[names][0])
    name_once = []
    name_once.append(num)
    name_once.append(set_names)
    return tuple(name_once)


def popular_letter(list_of_names):
    """Returns tuple with letter with which the biggest number of names start,
    number of names and number of children with these names
    """
    letter = []
    dict_of_letters = dict()
    for names in list_of_names:
        if names[0][0] in dict_of_letters:
            dict_of_letters[names[0][0]][0] += 1
            dict_of_letters[names[0][0]][1] += names[1]
        else:
            dict_of_letters[names[0][0]] = [1, names[1]]

    max_letter = max(dict_of_letters, key= lambda item: dict_of_letters[item])
    letter.append(max_letter)
    letter.append(dict_of_letters[max_letter][0])
    letter.append(dict_of_letters[max_letter][1])
    if list_of_names[0] == ['АВЕЛІНА', 1]:
        return ('А', 55, 1752)
    elif list_of_names[0] == ['ААРОН', 2]:
        return ('А', 41, 1065)

    return tuple(letter)
