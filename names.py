"names.py"

def find_names(file_path):
    """
    Returns tuple with set of three the most popular names,
    tuple with number of names that occure only once and set of these names,
    tuple with the most popular letter at the beggining of the words, number of these names
    and number of children with these names
    """
    list_of_names = reads_file(file_path)

    return names_once(list_of_names)

    res = []

    set_of_popular_names = popular_names(list_of_names)
    res.append(set_of_popular_names)

    name_once = names_once(list_of_names)
    res.append(name_once)


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
    for _ in range(3):
        max_value = list(max(list_of_names, key = lambda name: int(name[1])))
        set_of_popular_names.append(max_value[0])
        list_of_names.remove(max_value)
    return set(set_of_popular_names)


def names_once(list_of_names):
    "Returns tuple with num of names that occur only once and set of these names"
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


def 


print(find_names('boy_names'))

# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()
