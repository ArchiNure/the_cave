def hello(num1, num2, operation):
    if operation == "add":
        print(num1 + num2)
    if operation == "substract":
        print(num1 - num2)
    if operation == "mutiply":
        print(num1 * num2)
    if operation == "power":
        print(num1 ** num2)
    if operation == "divide":
        print("Result:")
        print(num1 // num2)
        print("Rest:")
        print(num1 % num2)
        print("Decimal result:")
        print(num1 / num2)


hello(11, 3, "add")
