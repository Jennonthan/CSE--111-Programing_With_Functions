
'''
Brennon Laney
05/13/21
'''

from math import pi

can_name = [
"#1 Picnic","#1 Tall","#2","#2.5","#3 Cylinder","#5", "#6Z","#8Z short","#10","#211","#300","#303"
]
can_radius = [
  6.83,
  7.78,
  8.73,
  10.32,
  10.79,
  13.02,
  5.40,
  6.83,
  15.72,
  6.83,
  7.62,
  8.10,  	
]
can_height = [
  10.16,	
  11.91,
  11.59,
  11.91,
  17.78,
  14.29,
  8.89,
  7.62,
  17.78,
  12.38,11.27,
  11.11
]
cost = [
  0.28, 
  0.43, 
  0.45, 
  0.61, 
  0.86, 
  0.83, 
  0.22,
  0.26,
  1.53,
  0.34, 
  0.38, 
  0.42, 
]

def main():

  #This will make it so that later we can pull things from the lists above in order
  for x in range(0, 12):

    name = can_name[x]
    radius = can_radius[x]
    height = can_height[x]
    surface_area = cylinder_surface_area(radius, height) 
    volume = cylinder_volume(radius,height)
    storage_efficiency = volume / surface_area
    print(f"{name} - {storage_efficiency:.1f}")




def cylinder_volume(radius, height):
  '''
  This is meant to calculate the volume of the cylinder
    radius: radius of the cylinder
    height: height of the cylinder
  return the volume
  '''
  volume = pi * (radius**2) * height
  return volume



def cylinder_surface_area(radius,height):
  '''
  This is calculates the surface area of the cylinder
    radius: radius of the cylinder
    height: height of the cylinder
  return the surface area
  '''
  surface_area = 2 * pi * radius * (radius + height)
  return surface_area

main()
