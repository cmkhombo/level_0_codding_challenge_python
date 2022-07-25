import math


def numbers_to_time(_number):
    _hours = math.floor(_number / 60)

    _min = 0

    if _number > 0 and _number != 60:
        _min = _number % 60

    if _hours > 1 or _hours == 0:
        _hrs_string = "{} Hours"

    elif _hours == 1 and _min == 0:
        _min = 60
        _hours = 0
        _hrs_string = "{} Hours"

    elif _hours == 1 and _min > 0:
        _hrs_string = "{} Hour"

    if _min > 1 or _min == 0:
        _min_string = ", {} Minutes"
    else:
        _min_string = ", {} Minute"

    return _hrs_string.format(_hours) + _min_string.format(_min)


print(numbers_to_time(71))
