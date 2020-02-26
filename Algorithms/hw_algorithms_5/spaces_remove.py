def spaces_remove(str):
    str_list1 = []
    str_list2 = []
    str_list1 = str.split(' ')
    for i in range(len(str_list1)):
        if str_list1[i] == '': continue
        str_list2.append(str_list1[i])
    return ' '.join(str_list2)

print(spaces_remove('  sdfsdf df  ! ! hjk y6    dfsfsdfsdf ff dsfsd  dsadfasds       dsd    '))
