def common_letters(str_one, str_two):
    str_one_lower = str_one.lower()
    str_two_lower = str_two.lower()
    print(
        "Common letters:",
        ",".join(set.intersection(set(str_one_lower), set(str_two_lower))),
    )


common_letters("House", "Computers")
