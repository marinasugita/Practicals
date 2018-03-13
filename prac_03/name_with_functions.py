def main():
    name = input('Enter name: ')
    while name.strip(' ') == '':
        print('Invalid name!')
        name = input('Enter name: ')
    print(name[1::2])


main()
