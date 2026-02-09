def mult(num1, num2):
    result = num1 * num2
    print(num1, "x", num2, "=", result)
    if result < 0:
        print("The result is negative")
    elif result > 0:
        print("The result is positive")
    else:
        print("The result is positive and negative")
mult(int(input("Enter the first number: ")), int(input("Enter the second number: ")))