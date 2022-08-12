def numbers_to_time(number):

    time = number / 60
    hours_str = str(time)
    hrs, mins = hours_str.split(".")
    hours = int(hrs)
    min = 0

    if number > 0 and number != 60:
        min = number % 60

    if hours == 1 and min == 0:
        print(f"{hours} hour, {min} minutes")

    elif hours > 1 and min == 0:
        print(f"{hours} hours, {min} minutes")

    elif hours == 1 and min == 1:
        print(f"{hours} hour, {min} minute")

    elif hours == 1 and min > 1:
        print(f"{hours} hour, {min} minutes")

    elif hours > 1 and min > 1:
        print(f"{hours} hours, {min} minutes")

    elif hours == 0 and min == 1:
        print(f"{hours} hours, {min} minute")

    elif hours == 0 and min > 1:
        print(f"{hours} hours, {min} minutes")

    elif hours == 0 and min == 0:
        print(f"{hours} hours, {min} minutes")


(numbers_to_time(1))
