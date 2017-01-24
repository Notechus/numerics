import random


def generate_account_number():
    number = ''
    for i in range(0, 26):
        number += str(random.randint(0, 9))
    print(number)


generate_account_number()
