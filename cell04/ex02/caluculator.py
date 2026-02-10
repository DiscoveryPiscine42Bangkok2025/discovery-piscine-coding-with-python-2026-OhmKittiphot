#!/usr/bin/env python3
def cal(num1, num2):
    print("Thank you!")
    print(f"{num1} + {num2} = {num1 + num2}")
    print(f"{num1} - {num2} = {num1 - num2}")
    print(f"{num1} / {num2} = {num1 // num2}")
    print(f"{num1} * {num2} = {num1 * num2}")
cal(int(input("Give me the first number: ")), int(input("Give me the secound number: ")))