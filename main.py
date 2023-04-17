print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to the Rake Boys Adventure.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
name = input("Who will you be playing as?  Atlas or Max? \n").lower()
if name == "atlas":
  print ("Welcome Atlas!")
if name == "max":
  print ("Welcome Max!")

first = input("The path shows 2 trails! Left into a dark forest and Right into a dark Cave.  Type left or right to proceed.\n").lower()

if first == 'left':
  second = input("the forest has led you to a lake!  Should you swim across? or wait for a boat? type swim or boat to proceed\n").lower()
  if second == "boat":
    third = input("After just a few moments a kind stranger floated by on their boat and picked you up!  The boat happens upon a waterfall!  Will you ask to be let off or pass through the waterfall?  Type off or pass to proceed\n").lower()
    if third == "pass":
      print("Huzzah!  the waterfall was hiding the treasure!  You WIN!\n")
    else:
      print("Oh No-er! a wild pack of Boi-Yo's has attacked!  GAME OVER\n")
  else:
      print("Oh No-er! Floating beaglers overcame you and dragged you down!  GAME OVER\n")
else:
    print("Oh No-er! You fell into the pit of despair!  GAME OVER\n")
