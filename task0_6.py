def maximum(*args):
    max_num = args[0]

    for num in args:
        if num > max_num:
            max_num = num
    return max_num


print(maximum(-34, -3, -40, -78, -100))
