def to25(num):
    if num > 25:
        print("Error")
    else:
        for i in range(num, 26):
            print("Inside the loop, my variable is", num)
            num += 1
to25(int(input()))