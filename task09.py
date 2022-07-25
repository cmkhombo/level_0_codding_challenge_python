def find_vowels(_str):
    _str_vowels = set()

    _str = _str.lower()
    _list_vowels = ["a", "e", "i", "o", "u"]
    for _char in _str:
        if _char in _list_vowels:
            _str_vowels.add(_char)
    print("Vowels: ", ",".join(_str_vowels))


find_vowels("Umuzi")
