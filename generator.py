from random import choice, randint, shuffle

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
           'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '#', '$', '%', '&', '*', '(', ')', '+']


def generate_password() -> str:
    nr_letters = randint(8, 10)
    nr_numbers = randint(2, 4)
    nr_symbols = randint(2, 4)

    password_list = []
    password = ""

    for char in range(nr_letters):
        password_list.append(choice(letters))

    for char in range(nr_numbers):
        password_list.append(choice(numbers))

    for char in range(nr_symbols):
        password_list.append(choice(numbers))

    shuffle(password_list)

    for char in password_list:
        password += char

    return password
