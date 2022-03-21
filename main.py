from Convsersion_fn import inttoroman, romantoint


def convert_int():
    print('\nThis program coverts integers to their roman equivalent')
    print('Integer must be between 1 and 3999 ')
    print("Enter 'Quit' to end the program")
    while True:
        integer = input('ENTER AN INTEGER: ')
        if integer.lower() == 'quit':
            print('Thanks for trying out the program. Bye!')
            break
        try:  # raises error in the case of a wrong input
            answer = inttoroman(int(integer))
        except ValueError:
            print('Wrong Input!')
        else:
            print(answer)


def convert_roman():
    print('\nThis program coverts roman numerals to integer')
    print('Enter Quit to end the program')
    while True:
        u_roman = input('Enter a Roman Numeral:')
        if u_roman.lower() == 'quit':
            print('Thanks for trying out the program. Bye!')
            break
        try:  # raises error in the case of a wrong input
            answer = romantoint(u_roman.upper())
        except KeyError:
            print('Wrong Input!')
        else:
            print(answer)


print('Welcome to Roman Numeral Converter')
print('Enter 1 to Convert Integer to Roman Numeral')
print('Enter 2 to Convert Integer to Roman Numeral')
while True:
    try:
        response = int(input('Option:'))
        if response == 1:
            convert_int()
        elif response == 2:
            convert_roman()
        break
    except ValueError:
        print('wrong Input!')


