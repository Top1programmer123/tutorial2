# def sum_elements(input_list):
#     total = 0
#     for number in input_list:
#         if number < 5:
#             total += number
#     return total
# my_list = [1,2,3,4,5,6,7,8,9,10]
# result = sum_elements(my_list)
# print(result)


# def common_elements(list1, list2):
#     common_elements = [i for i in list1 if i in list2]
#     return common_elements
# a_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# result = common_elements(a_list, b_list)
# print(result)



# print (""" The question is :-\n Take a list, say for example this one:\n
#   Take two lists, say for example these two:\n
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.
#            And i will program accordingly.\n""")
#
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# c=[]
# for i in range(len(a)):
#     if a[i] in b:
#         c.append(a[i])
# c=set(c)
# print(c)

# def palindrome(a):
#     a = a.lower()
#     if a == a[::-1]:
#         return "is a palindrome"
#     else:
#         return "is not a palindrome"
#
# print(palindrome("palindrome"))
# print(palindrome("racecar"))
#
#
# def is_palindrome(a):
#     new_string = ""
#     reverse_string = ""
#     for letter in a:
#         if letter != " ":
#             new_string += letter.lower()
#             reverse_string = letter.lower() + reverse_string
#
#
#     if new_string == reverse_string:
#         return True
#     return False
#
#
# print(is_palindrome("Never Odd or Even"))
# print(is_palindrome("abc"))
# print(is_palindrome("kayak"))



# list = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
#     958,743, 527]
# for i in list:
#     if i == 237:
#         break;
#     elif i % 2 == 0:
#         print(i)