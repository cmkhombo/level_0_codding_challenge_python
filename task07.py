def celsius_to_fahrenheit(_celsius):
    _fahrenheit = (_celsius * 9) / 5 + 32
    return _fahrenheit


def fahrenheit_to_celsius(_fahrenheit):
    _celsius = (5 / 9) * (_fahrenheit - 32)
    return _celsius


print(celsius_to_fahrenheit(13))
print(fahrenheit_to_celsius(50))
