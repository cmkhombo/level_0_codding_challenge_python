def area_of_triangle(first_num, second_num, third_num):
    sides = (first_num + second_num + third_num) / 2

    area = (
        sides * (sides - first_num) * (sides - second_num) * (sides - third_num)
    ) ** 0.5

    print(area)


area_of_triangle(6, 4, 3)
