#
# def replace_num(list):
#     # list = [10, 20, 30, 20, 40]
#     for a in range(len(list)):
#         if list[a] == 20:
#            list[a] = 200
#     return sum(list)
# print(replace_num)
# print(replace_num([10, 20, 30, 20, 40]))
# print(replace_num([1, 20, 21]))
# print(replace_num([19, 2, 15]))
# print(replace_num([20, 0, 20]))
# temp=replace_num([12, 2 , 89, 34, 20])
# print(temp)


#   print(list1)
#
# // Execution result
# [1, 200, 21]
# [19, 2, 15]
# [200, 0, 20]


def all_eq(list):
    max_num = 0
    result=[]
    for i in list:

        a = (len(i))
        if a > max_num:
            max_num = a

    for i in list:
        a=(len(i))
        if a<max_num:
            total_underscores=max_num-a
            i=i+"_"*total_underscores

            result.append(i)
        else:result.append(i)
    return result


print(all_eq(['крот', 'белка', 'выхухоль']))
print(all_eq(['a', 'aa', 'aaa', 'aaaa', 'aaaaa']))
print(all_eq(['qweasdqweas', 'q', 'rteww', 'ewqqqqq']))
# ['крот____', 'белка___', 'выхухоль']
# ['a____', 'aa___', 'aaa__', 'aaaa_', 'aaaaa']
# ['qweasdqweas', 'q__________', 'rteww______', 'ewqqqqq____']

# def to_dict(list):
#     result = {str(item): item for item in list}
#     return result
# print(to_dict(['1', '2', 3]))
# print(to_dict(['grey', (2, 17), 3.11, -4]))
# print(to_dict(['qweasdqweas', 'q', 'rteww', 'ewqqqqq']))


# my_dict = {'first_one': 'we can do it'}
#
# def biggest_dict(**kwargs):
#     global my_dict
#     for key, value in kwargs.items():
#         my_dict[key] = value
# biggest_dict(k1=22, k2=31, k3=11, k4=91)
# biggest_dict(name='Jabrayil', age=14, weight=48, eyes_color='brown')
# print(my_dict)

# def count_it(sequence):
#     digits = {}
#     for i in sequence:
#         if i.isdigit():
#             digit = int(i)
#             digits[digit] = digits.get(digit, 0) + 1
#     return digits
# print(count_it('1111111111222'))
# print(count_it('123456789012133288776655353535353441111'))
# print(count_it('007767757744331166554444'))
