def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9) / 5 + 32
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius


print(celsius_to_fahrenheit(13))
print(fahrenheit_to_celsius(50))
