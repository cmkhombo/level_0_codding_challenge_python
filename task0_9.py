def find_vowels(str):
    str_vowels = set()

    str = str.lower()
    list_vowels = ["a", "e", "i", "o", "u"]
    for char in str:
        if char in list_vowels:
            str_vowels.add(char)
    print("Vowels: ", ", ".join(str_vowels))


find_vowels("Umuzi")
