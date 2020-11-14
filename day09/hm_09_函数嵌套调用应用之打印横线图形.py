def print_line(num):
    print('-' * 20, end=f'{num}')
    print()


def print_lines(num):
    for i in range(num):
        print_line(i)


print_lines(5)

