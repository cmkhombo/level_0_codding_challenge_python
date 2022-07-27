def area_of_triangle(_first_num, _second_num, _third_num):
    _sides = (_first_num + _second_num + _third_num) / 2

    _area = (
        _sides * (_sides - _first_num) * (_sides - _second_num) * (_sides - _third_num)
    ) ** 0.5

    print(_area)


area_of_triangle(6, 4, 3)
