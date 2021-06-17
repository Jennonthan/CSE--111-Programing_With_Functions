'''
Brennon Laney, 
04/29/21
You work for a retail store that wants to increase sales on
Tuesday and Wednesday, which are the store's slowest sales 
days. On Tuesday and Wednesday, if a customer's subtotal is 
$50 or greater, the store will discount the customer's subtotal by 10%.
'''
# Import the datatime module so that
# it can be used in this program.
from datetime import datetime

# Call the now() method to get the current date and
# time as a datetime object from the computer's clock.
current_date_and_time = datetime.now()

# Call the isoweekday() method to get the day of
# the week from the current_date_and_time object.
weekday = current_date_and_time.isoweekday()

price = None
subtotal = 0

# subtotal = float(input("Please enter the subtotal: "))

while price != "done":
  price = input("What is the price? ")
  if price != "done":
    quantity = int(input("How much do you want? "))
    price1 = float(price)
    subtotal = price1 * quantity
    print(f"Your subtotal is: ${subtotal}")

if (weekday == 2 or weekday == 3):
  if subtotal >= 50:
    discount = subtotal * 0.1 
    subtotal -= (subtotal*.1)
    print(f"Discount amount: ${discount:.2f}")
  else: 
    amount = 50 - subtotal
    print(f"You need to spend ${amount:.2f} in order to get the discount")
    

salestax = subtotal * .06 
total =  subtotal + salestax
print(f"Sales tax amount: ${salestax:.2f}")
print(f"Total: ${total:.2f}")