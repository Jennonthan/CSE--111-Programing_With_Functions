'''
Brennon Laney
Team activity
06/03/21
'''

import random

def main():
    numbers_list = [16.2, 75.1, 52.3]
    # This prints the list
    print(numbers_list)

    # Runs the function which adds 1 random number to the list
    append_random_numbers(numbers_list)
    print(numbers_list)

    # Runs the function which adds 3 numbers to the list
    append_random_numbers(numbers_list, 3)
    print(numbers_list)

def append_random_numbers(numbers_list, quantity = 1):
    '''
    This function will take 2 arguments but the argument quantity has 
    1 as its set value. The function will randomly select random numbers.
    The amount of random numbers is equal to the quantity. The number
    will also be between 1 and 100

        numbers_list: This imports the library so that it can be used
        
        quantity: This is the amount of numbers you want generated, the
        default is 1

    return: There isn't one
    '''
    for _ in range(0, quantity):
        number = random.uniform(1, 100)
        number = round(number, 1)
        numbers_list.append(number)

    


main()
