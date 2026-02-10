import math

def roundUP(user_data):
    n = float(user_data)
    result = math.ceil(n)
    print(result)
roundUP(input("Give me a number: "))