def numbers_to_time(number):

    time = number / 60
    hours_str = str(time)
    hrs, _mins = hours_str.split(".")
    hours = int(hrs)
    min = 0

    if number > 0 and number != 60:
        min = number % 60

    if hours > 1 or hours == 0:
        hrs_string = f"{hours} hours"

    elif hours == 1 and min == 0:
        hrs_string = f"{hours} hour"

    elif hours == 1 and min > 0:
        hrs_string = f"{hours} hour"

    if min > 1 or min == 0:
        min_string = f", {min} minutes"
    else:
        min_string = f", {min} minute"

    return f"{hrs_string}{min_string}"


print(numbers_to_time(60))
