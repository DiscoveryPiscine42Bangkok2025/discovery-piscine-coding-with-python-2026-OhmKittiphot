#!/usr/bin/env python3
def multiplication(num):
    for i in range(10):
        print(i, "x", num, "=", i*num)
        i += 1
multiplication(int(input()))