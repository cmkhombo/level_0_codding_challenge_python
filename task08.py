def numbers_to_time(_number):

    _time = _number / 60
    _hours_str = str(_time)
    _hrs, _mins = _hours_str.split(".")
    _hours = int(_hrs)
    _min = 0

    if _number > 0 and _number != 60:
        _min = _number % 60

    if _hours > 1 or _hours == 0:
        _hrs_string = f"{_hours} hours"

    elif _hours == 1 and _min == 0:
        _hrs_string = f"{_hours} hour"

    elif _hours == 1 and _min > 0:
        _hrs_string = f"{_hours} hour"

    if _min > 1 or _min == 0:
        _min_string = f", {_min} minutes"
    else:
        _min_string = f", {_min} minute"

    return _hrs_string + _min_string


print(numbers_to_time(60))
