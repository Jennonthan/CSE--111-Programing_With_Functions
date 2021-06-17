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
can_cost = [
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
  for x in range(0, 12):
    name = can_name[x]
    radius = float(can_radius[x])
    height = float(can_height[x])
    cost = can_cost[x]
    surface_area = float(cylinder_surface_area(radius, height))
    volume = cylinder_volume(radius, height)
    efficiency = storage_efficiency(volume, surface_area)
    cost_eff = storage_efficiency(volume, cost)
    print(f"{name} - {efficiency:.1f} - {cost_eff:.1f}")

def storage_efficiency(volume, surface_area):
  storage_efficiency = volume / surface_area
  return storage_efficiency

def cost_efficiency(volume, cost):
  cost_efficiency = volume / cost  
  return cost_efficiency

def cylinder_volume(radius, height):
  volume = pi * (radius**2) * height
  return volume

def cylinder_surface_area(radius,height):
  surface_area = 2 * pi * radius * (radius + height)
  return surface_area

main()
