# def get_even_str(input_string):
#     even_str = input_string[::2]
#     return ','.join(even_str)
#
# user_input = input("Enter string: ")
#
# result = get_even_str(user_input)
# print(f"Even characters: {result}")

# def first_and_last(numbers):
#
#     if numbers:
#
#         return numbers[0] == numbers[-1]
#     else:
#
#         return False
#
# print(first_and_last([1, 2, 3, 1]))
# print(first_and_last([5, 6, 7, 8]))
# print(first_and_last([3, 4, 5, 3]))
# print(first_and_last([]))

# str = "Jaba is a good programmer. Be like Jaba"
#
# str_count = str.count("Jaba")
#
# print(f"The substring 'Jaba' appears {str_count} times in the string.")

# num_lines = 5
#
# for i in range(1, num_lines + 1):
#
#     for j in range(i):
#         print(i, end=" ")
#     print()

# def combine_odd_even(lst1, lst2):
#     result_lst = []
#
#     odd_num_lst = [num for num in lst1 if num % 2 != 0]
#     result_lst.extend(odd_num_lst)
#
#     even_num_lst = [num for num in lst2 if num % 2 == 0]
#     result_lst.extend(even_num_lst)
#
#     return result_lst
#
# lst1 = [1, 2, 3, 4, 5]
# lst2 = [6, 7, 8, 9, 10]
#
# result = combine_odd_even(lst1, lst2)
# print(result)

# def multiplication_table(size):
#     for i in range(1, size + 1):
#         for j in range(1, size + 1):
#             print(i * j, end=" ")
#         print()
#
# table_size = 10
#
# multiplication_table(table_size)

# def alphabet_word(word):
#     sorted_word = ''.join(sorted(word))
#     return sorted_word
#
# input_word = "python"
# result = alphabet_word(input_word)
# print(result)