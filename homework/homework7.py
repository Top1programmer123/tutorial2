# def twoSum(nums, target):
#     num_indices = {}
#
#     for i, num in enumerate(nums):
#         complement = target - num
#         if complement in num_indices:
#             return [num_indices[complement], i]
#         num_indices[num] = i
#     return []
# nums = [2, 7, 11, 15]
# target1 = 9
# result1 = twoSum(nums, target1)
# print(result1)
# nums2 = [3, 2, 4]
# target2 = 6
# result2 = twoSum(nums2, target2)
# print(result2)
# nums3 = [3, 3]
# target3 = 6
# result3 = twoSum(nums3, target3)
# print(result3)



def roman_to_int(s):
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    result = 0
    prev_value = 0

    for char in reversed(s):
        value = roman_values[char]
        if value < prev_value:
            result -= value
        else:
            result += value
        prev_value = value
    return result
if __name__ == "__main__":
    print(roman_to_int("IVI"))
    print(roman_to_int("LVIII"))
    print(roman_to_int("MCMXCIV"))




# l1 = [2,4,3]
# temp=l1[1]
# l1[1]=l1[2]
# l1[2]=temp
# print(l1)
#
# sum_l1=0
# for i in l1:
#     sum_l1=sum_l1+1
# print(sum_l1)

# lst2=list(range (1,5))
# # lst1= [i for i in list (range(1-11))]
# temp=True
# index=0
# # print(len(lst2))
# while index<len(lst2):
#     print(index,str('index'))
#     if lst2[index] % 2==0:
#         print(lst2[index])
#     index+=1



# lst=list(range(1,7))
# sum_list=sum(lst)
# print(sum_list)
# lst=list(range(1,21))
# lst2=lst[4:11]
# print(lst2)

# temp=[1,2,3,4]
# temp2=" ".join ([str(i) for i in temp])
# print(temp2)
# def addTwoNumbers(l1, l2):
#     temp=l1[::-1]
#     temp2=l2[::-1]
#     temp3=int(''.join(temp))
#     temp4=int(''.join(temp2))
#     sum_of_numbers=temp3+temp4
#     print(sum_of_numbers)
#     result=[i for i in str(sum_of_numbers)]
#     print(result)
#     temp5=result[::-1]
#     return temp5
# lst = ['10', '11', '12', '13', '14', '15']
# lst2 = ['19', '20', '21']
# print(addTwoNumbers(lst, lst2))




