# def to_dict(lst):
#     return {keys: keys for keys in lst}
# print(to_dict([1, 2, 3, 4]))
# print(to_dict(['grey', (2, 17), 3.11, -4]))

# my_dict = {}
# def biggest_dict(**kwargs):
#     global my_dict
#     my_dict.update(kwargs)
# biggest_dict(k1=22, k2=31, k3=11, k4=91)
# biggest_dict(name='Елена', age=31, weight=61, eyes_color='grey')
# print(my_dict)

# def count_it(sequence):
#     digit_count = {}
#     for digit in sequence:
#         if digit.isdigit():
#             digit = int(digit)
#             if digit in digit_count:
#                 digit_count[digit] += 1
#             else:
#                 digit_count[digit] = 1
#     return digit_count
# print(count_it('1111111111222'))
# print(count_it('123456789012133288776655353535353441111'))
# print(count_it('007767757744331166554444'))


# def multiply_dict(dictionary):
#     result = 1
#     for key, value in dictionary.items():
#         result *= value
#     return result
# my_dictionary = {'data1': 375, 'data2': 567, 'data3': -37, 'data4': 21}
# result = multiply_dict(my_dictionary)
# print(result)
#
# dict = {x: x**3 for x in range(1, 11)}
# print(dict)

