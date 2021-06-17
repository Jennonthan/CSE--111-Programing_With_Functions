'''
Brennon Laney
04/30/21

'''

#I imported date instead of datetime because datetime gives you the date and time
from datetime import date, timedelta

#Date gives only the month day and year
current_date_and_time = date.today()

#In order to use pi I must import the math library 
import math

pi = math.pi

def calculate_volume(w, a, d):
    v = (pi * (w ** 2) * a * (w * a + 2540 *d) / 10000000)
    return v

#This will open the file for the duration of the with statment 
with open('volumes.txt', 'at') as information_file:

    #Declare my variables 
    width = int(input('Enter the width of the tire in mm (ex 205): '))
    aspect_ratio = int(input('Enter the aspect ratio of the tire (ex 60): '))
    diameter = int(input('Enter the diameter of the wheel in inches (ex 15): '))

    #Calculating the Volume and Radius
    volume = calculate_volume(width, aspect_ratio, diameter)
    radius = (float(diameter) / 2)


    #Here I compiled the information into one string to make it easier
    information =(f'{current_date_and_time}, {width}, {aspect_ratio}, {diameter}, {volume:.1f}')

    #Add everything to the file
    print(information, file = information_file)
    print('The radius of the tire is:', file = information_file)
    print(radius, file = information_file)