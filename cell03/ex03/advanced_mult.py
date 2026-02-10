def adv_mul():
    i = 0
    while i <= 10:
        print(f"Teble de {i}:", end="")
        j = 0
        while j <= 10:
            result = i * j
            print(f" {result}", end="")
            j += 1
        print()
        i += 1
adv_mul()