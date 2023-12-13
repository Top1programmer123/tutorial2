def calculator():
    temp=''
    new_result=0
    values = []
    wrong_inputs = []
    def minus(a,b):
        return a-b
    def plus(a,b):
        return a+b
    def Multiply(a,b):
        return a*b
    def divide(a,b):
        return a/b

    symbols={
        "-":minus,
        '/':divide,
        '+':plus,
        '*':Multiply
    }




    while True:
        user_input = input("Enter a number: ")

        if user_input.lower() == 'exit':
            break

        try:
            value = eval(user_input)
            if not new_result:
                new_result = value
            values.append(value)
            if temp and values[-1]:
                new_result=temp(new_result, value)
        except (SyntaxError, NameError):
            wrong_inputs.append(user_input)
        finally:
            temp=symbols.get(user_input)
    result = sum(values) if values else 0
    print(new_result)
    # print("Result =", result)
    if wrong_inputs:
        print("Wrong inputs =", wrong_inputs)


if __name__ == "__main__":
    calculator()
    print(calculator)
    # print(eval('sum([1,2,3])'))
temp=calculator
print(temp)

# with open
# with: how it works and how we can use it
# f-strings how it works
# formats how it works with strings
