# def longestCommonPrefix(strs):
#     strs.sort()
#     print(strs)
#     ans = ""
#     first = strs[0]
#     last = strs[-1]
#     print(min(len(first), len(last)))
#     for i in range(min(len(first), len(last))):
#         if first[i] != last[i]:
#             return ans
#         ans += first[i]
#     return ans


#
# strs = ["flower", "funder", "flight"]
# strs=["ab ",'a',"acb"]
# def longestCommonPrefix(strs):
#     if not strs:
#         return ''
#
#     l = len(strs[0])
#     for i in range(1, len(strs)):
#         length = min(l, len(strs[i]))
#         while length > 0 and strs[0][0:length] != strs[i][0:length]:
#             length = length - 1
#             if length == 0:
#                 return ''
#     return strs[0][0:length]
#
# print(longestCommonPrefix(strs))


def isValid(s):
    temp = []
    bracket_mapping = {')': '(', '}': '{', ']': '['}
    print(bracket_mapping.values())
    print(bracket_mapping)

    for char in s:
        if char in bracket_mapping.values():
            temp.append(char)
        elif char in bracket_mapping:
            if not temp or temp.pop() != bracket_mapping[char]:
                return False
    return not temp
print(isValid("()"))
print(isValid("(]"))
print(isValid("{[]}"))
temp=0
# if temp:
#     print('true')
# if not temp:
#     print("not temp")
