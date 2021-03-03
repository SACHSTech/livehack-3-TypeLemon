"""
--------------------------------------------------------
Name: problem2.py
Purpose: Allows Tony the DoorDash Driver to enter the distance he travels each day. Provides him a summary of how many days it took to surpass 100km driven and his average driven per day.

Author: Yeh.A

Created: 03/03/2021
--------------------------------------------------------
"""
print("***** Welcome to the DoorDash Distance Tracker! *****")
print(" ")

print("** Travel Log **")

#asks the user how far they travelled each day until the sum is greater than 100
#counts number of days for each time the while loop is runned through
total = 0
num_days = 0

while total <= 100:
  daily_travelled = int(input("Enter the distance travelled for the day (km): "))
  total = total + daily_travelled
  num_days = num_days + 1

print(" ")

print("** Summary **")

#outputs the number of days it took to drive more than 100km
print("It took", num_days, "days to surpass 100km driven.")
#rounds and outputs the average distance to nearest km/whole number 
average = int(total/num_days)
print("The average distance driven per day is", average, "km.")