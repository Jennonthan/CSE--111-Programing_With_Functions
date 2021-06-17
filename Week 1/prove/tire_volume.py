'''
Brennon Laney
04/22/21
Prove that you can write a simple Python program that gets input from a user, performs arithmetic, and displays output for the user to see.
'''

#In order to use pi I must import the math library 
import math

pi = math.pi

def calculate_volume(w, a, d):
    v = (pi * (w ** 2) * a * (w * a + 2540 *d) / 10000000)
    return v

#Declare my variables 
width = float(input('Enter the width of the tire in mm (ex 205): '))
aspect_ratio = float(input('Enter the aspect ratio of the tire (ex 60): '))
diameter = float(input('Enter the diameter of the wheel in inches (ex 15): '))

volume = calculate_volume(width, aspect_ratio, diameter)

#print statment
print(f'The approximate volume is {volume:.1f} milliliters')

#These if statments will display if the tire is above avarage or below it.
if volume > 10000:
    print('Your tire has more volume than the avarage tire')
elif volume < 10000:
    print('Your tire has less volume than the avarage tire')
else:
    print('Your tire has the same volume as the avarage tire')