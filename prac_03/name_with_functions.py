def main():
    name = input('Enter name: ')
    while name.strip() == '':
        print('Please enter a valid name.')
        name = input('Enter name: ')
    step = int(input('Enter steps: '))
    print_name(name, step)


def print_name(name, step):
    print(name[::step])


main()
