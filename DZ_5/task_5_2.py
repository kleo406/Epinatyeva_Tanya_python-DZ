def my_gen(start, end):
    my_generator = (num for num in range(start, end + 1, 2))
    return my_generator
print(*my_gen(1, 15), sep=', ')
