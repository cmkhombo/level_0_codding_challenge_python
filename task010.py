def common_letters(_str_one, _str_two):
    _str_one_lower = _str_one.lower()
    _str_two_lower = _str_two.lower()
    print(
        "Common letters:",
        ",".join(set.intersection(set(_str_one_lower), set(_str_two_lower))),
    )


common_letters("House", "Computers")
