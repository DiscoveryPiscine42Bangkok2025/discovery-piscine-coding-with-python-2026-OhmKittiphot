def check_number(num_str):
    if num_str.isdigit():
        print("This number is an integer.")
    else:
        n = float(num_str)
        if n == int(n):
            print("This number is an integer.")
        else:
            print("This number is a decimal.")
check_number(input("Give me a number : "))