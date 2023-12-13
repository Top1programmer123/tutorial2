def plus(a, b):
    return a + b


def minus(a, b):
    return a - b


def divide(a, b):
    return a / b


def multiple(a, b):
    return a * b


operators = {
    "plus": plus,
    "+": plus,
    "-": minus,
    "/": divide,
    "*": multiple

}


def enter_number():
    try:
        x = int(input("Enter a number:", ))
    except ValueError:
        print("wrong input, try again")
        x = enter_number()
    return x


def enter_operator():
    y = input("enter an operator:")
    if  y== "q":
        return y
    if operators.get(y):
        return y
    else:
        print("The operator is incorrect ")
        y = enter_operator()
    return y


def calculator():
    result=enter_number()

    while True:
        operator=enter_operator()
        if operator=="q":
            break
        method=operators.get(operator)
        number = enter_number()
        result=method(result,number)
    print(result)
#
calculator()
