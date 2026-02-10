def age(userAge):
    print(f"You are currently {userAge} old.")
    for i in range(1, 4):
            year = i * 10
            print(f"In {year} years, you'll be {userAge + year} years old")
age(int(input("Please tell me your age: ")))