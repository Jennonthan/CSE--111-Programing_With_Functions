'''
Brennon Laney
05/04/21
Purpose: Many vehicle owners record the fuel efficiency of their vehicles as a
way to track the health of the vehicle. If the fuel efficiency of a vehicle
suddenly drops, there is probably something wrong with the engine or drive 
train of the vehicle. In the United States, fuel efficiency for gasoline 
powered vehicles is calculated as miles per gallon. In most other countries, 
fuel efficiency is calculated as liters per 100 kilometers.

The formula for computing fuel efficiency in miles per gallon is the following:

mpg = 
end − start
gallons
where start and end are both odometer values in miles and gallons is a fuel 
amount in U.S. gallons.

The formula for converting miles per gallon to liters per 100 kilometers 
is the following:

lp100k = 
235.215/mpg
'''


def miles_per_gallon(start_miles, end_miles, amount_gallons):
    """Compute and return the average number of miles
    that a vehicle traveled per gallon of fuel.

    Parameters
        start_miles: An odometer value in miles.
        end_miles: Another odometer value in miles.
        amount_gallons: A fuel amount in U.S. gallons.
    Return: Fuel efficiency in miles per gallon.
    """
    mpg = (end_miles - start_miles) / amount_gallons

    return mpg


def lp100k_from_mpg(mpg):
    """Convert miles per gallon to liters per 100
    kilometers and return the converted value.

    Parameter mpg: A value in miles per gallon
    Return: The converted value in liters per 100km.
    """

    lp100k = 235.215 / mpg
    return lp100k


def main():
    # Get an odometer value in U.S. miles from the user.
    starting_odometer = float(input('Enter the first odometer reading (in miles): '))

    # Get another odometer value in U.S. miles from the user.
    ending_odometer = float(input('Enter the second odometer reading (in miles): '))

    # Get a fuel amount in U.S. gallons from the user.
    fuel_amount = float(input('Enter the amount of fuel used (in gallons): '))

    # Call the miles_per_gallon function and store
    # the result in a variable named mpg.
    mpg = miles_per_gallon(starting_odometer, ending_odometer, fuel_amount)

    # Call the lp100k_from_mpg function to convert the
    # miles per gallon to liters per 100 kilometers and
    # store the result in a variable named lp100k.
    lp100k = lp100k_from_mpg(mpg)

    # Round the miles per gallon to one digit after the decimal.
    mpg = round(mpg, 2)

    # Round the liters per 100 km to two digits after the decimal.
    lp100k = round(lp100k, 2)

    # Display the results for the user to see.
    print(f'{mpg} miles per gallon')
    print(f'{lp100k} liters per 100 kilometers')

    pass



# Call the main function so that
# this program will start executing.
main()