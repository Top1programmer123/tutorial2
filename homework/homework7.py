# def twoSum(nums, target):
#     num_indices = {}  # Dictionary to store the numbers and their indices
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
print(roman_to_int("III"))
print(roman_to_int("LVIII"))
print(roman_to_int("MCMXCIV"))





