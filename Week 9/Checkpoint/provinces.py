'''
Brennon Laney
03/14/21
Checkpoint: 

'''

places= []

with open('provinces.txt', 'rt') as povinces:
    for provence in povinces:
        # print(provence)
        places.append(provence.strip())


    # This gets rid of the first and last item
    places.pop(71)
    places.pop(0)

    # I had to set this variable before the for loop
    alberta_count = 0

    # This for loop goes from a range of 0 to one less then 
    #the amount of items in the list places. These numbers
    #represnt the index
    for i in range(0, (len(places) - 1)):

        # If the item with the index of i is equal to 'AB' it
        #will replace it with 'Alberta'
        if places[i] == 'AB':
            places[i] = 'Alberta'
        print(places[i])

        # For every 'Alberta' it will add 1 to the alberta_count
        #variable
        if places[i] == 'Alberta':
            alberta_count += 1


    print(f'Alberta is in the list {alberta_count} times')

    # for place in places:
    #     print(place)






    # length = len(places)
    # print(length)

    # length = len(places)
    # print(length)