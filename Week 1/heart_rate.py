'''
Brennon laney
04/22/21
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum.
'''

def calculate_max_heartrate(age):
    max_heartrate = 220 - age
    return max_heartrate

#Declairing variables
age = int(input('Please enter your age: '))


max_heartrate = calculate_max_heartrate(age)

#Calculate the max and the min of what your heart rate should be
max_heartrate_min = max_heartrate * 0.65
max_heartrate_max = max_heartrate * 0.85

#print statements
print(f'When you exercise to strengthen your heart,')
print(f'you should keep your heart rate between {max_heartrate_min:.0f} and {max_heartrate_max:.0f} beats per minute.')