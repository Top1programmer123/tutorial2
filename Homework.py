# def volume_of_ball (x):
#     result = 3/4*3.14*x**3
#
#     if  result <10:
#      return print("small ball")
#     elif result>10:
#         return 'Big ball'
#     else:
#         return ("ball equals to 10")
#     return result
# print(volume_of_ball(1))

def numbers_operations(x,y,z):
     if z=='+':
          return x+y
     elif z=='-':
          return x-y
     elif z=='*':
          return x*y
     elif z=='/':
          return x/y
     elif z=='**':
          return x**y

     else:
          return ('unknown operation')

# print(numbers_operations(2,3,'+'))#5
# print(numbers_operations(2,3,'-'))#-1
# print(numbers_operations(2,3,'*'))#6
x=int(input("Enter your number:"))
y=int(input("Enter your number:"))
z=str(input())
# print(xzy)
result=(numbers_operations(x,y,z))
print(result)
numbers_operations(x,y,z)


# x="'Hello world'"
# print (x)







# def welcome(name, location):
#     print("Hi", name, "welcome to", location)
#
# welcome('Erik', 'this tutorial')


# def say_hi(name):
#     print('Hi, ' + name)
#
# print("Let's greet the entire world")
# say_hi('world')
#
#
# def abc_school(name):
#     print('Huseynov,  ' + name)
#
# print('The most hard working student is:')
# abc_school('Jabrayil')



