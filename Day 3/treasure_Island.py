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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("You're at a crossroads with two paths ahead.")
print("To your right, there's a sign that says, 'Safe, but boring.'")
print("To your left, a trail filled with adventure awaits,")
print("But whispers caution, 'Choose wisely or regret.'")
print("To find the hidden treasure that few have claimed,")
print("Which path should you take? (Type 'left' or 'right')")
left_or_right = input("Your choice. ")
left_or_right = left_or_right.lower()
if left_or_right == "right":
    print("You fell into a hole, broke your ankle, and died of exposure. Game over.")
elif left_or_right == "left":
    print("You find yourself at the edge of a shimmering lake. The water looks inviting, and you can hear the sounds of splashing. You have two choices: You can swim across the lake, where the surface glistens like a treasure. Or, you can wait by the shore, where you can observe the creatures that inhabit the water.")
    swim_or_wait = input("Swim or Wait? ")
    swim_or_wait = swim_or_wait.lower()
    if swim_or_wait == "swim":
        print("You were attacked by a gang of rabid trout. Game Over.")
    elif swim_or_wait == "wait":
        print("Three doors have now magically appeared. Each door has something written on it.")
        print("The red door has 'HJKX BY JTXH' etched on it.")
        print("The blue door has 'HJKX BY EJTXS' etched on it.")
        print("The yellow door has 'YVXH VX HJKXHU' etched on it.")
        door = input("Which door do you choose? Red, Blue, or Yellow? ")
        door = door.lower()
        if door == "red":
            print("Burned by fire. Game Over.")
        elif door == "blue":
            print("Eaten by beasts. Game Over.")
        elif door == "yellow":
            print ("You Win!")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout. Game Over.")
else:
    print("Fall into a hole. Game over.")