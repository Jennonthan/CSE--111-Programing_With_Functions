'''
Brennon Laney
04/27/21
Checkpoint 
purpose: Improve your understanding of calling built-in functions and functions that are in a standard Python module.
A manufacturing company needs a program that will help its employees pack manufactured items into boxes for shipping.
Write a Python program named boxes.py that asks the user for two integers:  1) the number of manufactured items and
2) the number of items that the user will pack per box. Your program must compute and print the number of boxes
necessary to hold the items. This must be a whole number. Note that the last box may be packed with fewer items
than the other boxes.
'''

import math

def find_box_count(items, items_in_box):
    box = items / items_in_box
    # remainder = items % items_in_box
    # if remainder > 0:
    #     box += 1
    box_count = math.ceil(box)

    return box_count

# Setting the variables to the unsers input
items = int(input('Enter the number of items: '))

items_in_box = int(input('Enter the number of items per box: '))

number_of_boxes = find_box_count(items, items_in_box)

#print statement
print(f'For {items} items, packing {items_in_box} items in each box, you will need {number_of_boxes} boxes.')