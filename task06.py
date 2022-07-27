def maximum(*args):
    _max_num = args[0]

    for _num in args:
        if _num > _max_num:
            _max_num = _num
    return _max_num


print(maximum(-34, -3, -40, -78, -100))
