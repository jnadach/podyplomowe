# Autor: Jan Nadachowski

list1 = [10, 2]
list2 = [10, 1]
list3 = [4, 4, 4]
list4 = [4, 5, 2]


def lists_to_tuples(*args):
    concat_list = []
    dedupe_concat_list = []
    for arg in args:
        concat_list += arg
    for i in concat_list:
        if i not in dedupe_concat_list:
            dedupe_concat_list.append(i)
    dedupe_concat_list.sort()
    return tuple(dedupe_concat_list)


print(lists_to_tuples(list1, list2, list3, list4))
