"""
Write a Python program named fitness.py that does the following:
1. Asks the user to enter four values:
    a. gender
    b. birthdate in this format: YYYY-MM-DD
    c. weight in US pounds
    d. height in US inches
2. Converts the weight from pounds to kilograms (1 lb = 0.45359237 kg).
3. Converts inches to centimeters (1 in = 2.54 cm).
4. Calculates age, BMI, and BMR.
5. Prints age, weight in kg, height in cm, BMI, and BMR.
"""



# Import datetime so that it can be
# used to compute a person's age.
from datetime import datetime
gender = None

def main():
  # Get the user's gender, birthdate, height, and weight.
  gender = input("What is your gender? (M or F): ")
  birth = input("What is your birthdate? (YYYY-MM-DD): ")
  weight = float(input("What is your weight in US pounds?: "))
  height = float(input("What is your height in US inches?: "))

  # Call the compute_age, kg_from_lb, cm_from_in, body_mass_index,
  # and basal_metabolic_rate functions as needed.

  # Print the results for the user to see.

  age = compute_age(birth)
  body_weight = kg_from_lb(weight)
  centimeters = cm_from_in(height)
  bmi = body_mass_index(body_weight, centimeters)
  bmr = basal_metabolic_rate(gender, body_weight, centimeters, age)
  
  print(f"Age (years): {age}")
  print (f"Weight (kg): {body_weight:.2f}")
  print (f"Height (cm): {centimeters:.1f}")
  print(f"Body mass index: {bmi:.1f}")
  print(f"Basal metabolic rate (kcal/day): {bmr:.0f}")
  pass


def compute_age(birth):
  """Compute and return a person's age in years.

  Parameter birth: a person's birthdate stored as
      a string in this format: YYYY-MM-DD
  Return: a person's age in years.
  """
  birthday = datetime.strptime(birth, "%Y-%m-%d")
  today = datetime.now()

  # Compute the difference between today and the birthday in years.
  years = today.year - birthday.year

  # If necessary, subtract one from the difference.
  if birthday.month > today.month or \
      (birthday.month == today.month and birthday.day > today.day):
      years -= 1

  return years


def kg_from_lb(lb):
  """Convert a mass in pounds to kilograms.
  Parameter lb: a mass in US pounds.
  Return: the mass in kilograms
  """
  body_weight = lb * 0.45359237
  return body_weight

def cm_from_in(inch):
  """Convert a length in inches to centimeters.
  Parameter inch: a length in inches.
  Return: the length in centimeters.
  """
  centimeters = inch * 2.54
  
  return centimeters


def body_mass_index(weight, height):
  """Calculate and return a person's body mass index (bmi).
  Parameters:
      weight must be in kilograms.
      height must be in centimeters.
  Return: a person's body mass index.
  """
  bmi = (weight * 10000) / (height ** 2)
  return bmi


def basal_metabolic_rate(gender, body_weight, centimeters, age):
  """Calculate and return a person's basal metabolic rate (bmr).
  Parameters:
      weight must be in kilograms.
      height must be in centimeters.
      age must be in years.
  Return: a person's basal metabolic rate in kcal per day.
  """
  if gender.lower() == "m" or gender.lower() == "male":
    bmr = 88.362 + (13.397 * body_weight) + (4.799 * centimeters) - (5.677 * age)

  elif gender.lower() == "f" or gender.lower() == "female":
    bmr = 447.593 + (9.247 * body_weight) + (3.098 * centimeters) - (4.330 * age)

  else:
    print("An error has occured.")
    
  return bmr

# Call the main function so that
# this program will start executing.
main()