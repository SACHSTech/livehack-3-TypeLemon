"""
--------------------------------------------------------
Name: problem1.py
Purpose: Allows user to enter wins and losses for six games and determines which group they are in.

Author: Yeh.A

Created: 03/03/2021
--------------------------------------------------------
"""
print("***** Tournament Tracker *****")
print(" ")

#asks the user six times if they won or lost the game
#counts the number of times they entered "W" for each win
total = 0

for i in range(6):
  win_loss = input("Did you win or lose? (W or L): ")
  for char in win_loss:
    if char == "W":
      total = total + 1
  
print(" ")

#determines group placement depending on number of wins
if total == 5 or total == 6:
  print("Your team is in Group 1!")

if total == 3 or total == 4:
  print("Your team is in Group 2!")

if total == 1 or total == 2:
  print("Your team is in Group 3!")

if total == 0:
  print("Sorry, your team is eliminated from the tournament.")