def identify_unique(dupl_list):
    list1 = []
    for i in dupl_list:
        if i in list1:
            continue
        elif i not in list1:
            list1.append(i)

    return list1

list_with_duplicates = [1,1,1,1,2,2,2,3,3,3,3,4,4,5]

print(identify_unique(list_with_duplicates))
