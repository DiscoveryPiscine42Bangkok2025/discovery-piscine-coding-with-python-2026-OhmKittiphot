def end_yet(txt):
    while True:
        if txt == "STOP":
            break
        txt = input("I got that! Anything else? : ")
end_yet(input("What you gotta say? : "))