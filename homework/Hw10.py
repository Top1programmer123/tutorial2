# primes=[]
# for possiblePrime in range(2, 21):
#
#     isPrime=True
#     for num in range (2, possiblePrime):
#         if possiblePrime % num==0:
#             isPrime=False
#     if isPrime:
#         primes.append(possiblePrime)

# number = 10
# second_number = 10
# first_array = [2]
# second_array = [1,2,3]
#
# if number > 1:
#     print("1")
#
# if first_array:
#     print("2")
#
# if len(second_array) == 3:
#     print("3")
#
# if len(first_array) + len(second_array) == 4:
#     print("0")
#
# if first_array and first_array[0] == 2:
#     print("5")
#
# if second_number:
#     print("6")

# def spinWords(sentence):
#     words = sentence.split()
#     for i in range(len(words)):
#         if len(words[i]) >= 5:
#             words[i] = words[i][::-1]
#     result = ' '.join(words)
#     return result
#
#
# print(spinWords("Hey fellow warriors"))
# print(spinWords("This is a test"))
# print(spinWords("This is another test"))

# def is_prime(num):
#     if num < 2:
#         return False
#
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#
#     return True
#
#
# print(is_prime(1))
# print(is_prime(2))
# print(is_prime(-1))
# print(is_prime(13))
# print(is_prime(16))

# def count_bits(n):
#     return bin(n).count('1')
#
#
# result = count_bits(1234)
# print(result)
# def add_line_numbers(lines):
#     return [f"{i + 1}: {line}" for i, line in enumerate(lines)]
#
#
# print(add_line_numbers([]))
# print(add_line_numbers(["a", "b", "c"]))
#
#
# def get_sum(a, b):
#     return sum(range(min(a, b), max(a, b) + 1))
#
#
# print(get_sum(1, 0))
# print(get_sum(1, 2))
# print(get_sum(0, 1))
# print(get_sum(1, 1))
# print(get_sum(-1, 0))
# print(get_sum(-1, 2))
#
#
# def longest(s1, s2):
#     return ''.join(sorted(set(s1 + s2)))
#
#
# a = "xyaabbbccccdefww"
# b = "xxxxyyyyabklmopq"
# print(longest(a, b))
#
# a = "abcdefghijklmnopqrstuvwxyz"
# print(longest(a, a))
#
#
# def expanded_form(num):
#     num_str = str(num)
#     result = []
#     for i, digit in enumerate(num_str[::-1]):
#         if digit != '0':
#             result.append(str(int(digit) * 10 ** i))
#     return ' + '.join(result[::-1])
#
#
# print(expanded_form(12))
# print(expanded_form(42))
# print(expanded_form(70304))
#
#
# def maskify(cc):
#     return "#" * max(0, len(cc) - 4) + cc[-4:]
#
#
# print(maskify("4556364607935616"))
# print(maskify("64607935616"))
# print(maskify("1"))
# print(maskify(""))
# print(maskify("Skippy"))
# print(maskify("Nananananananananananananananana Batman!"))
#
#
# def alphabet_position(text):
#     return ' '.join(str(ord(char) - 96) for char in text.lower() if char.isalpha())
#
#
# print(alphabet_position("The sunset sets at twelve o' clock."))
