def item_in_common(list1,list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False
