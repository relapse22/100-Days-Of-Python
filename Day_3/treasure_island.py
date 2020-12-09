voodoo_man = ('''
                     ,
               ._  \/, ,|_
               -\| \|;|,'_
               `_\|\|;/-.
                `_.\|/._  
               ,'__   __`.
              / /_ | | _\ \ 
             / ((o)| |(o)) \ 
             |  `--/ \--'  |
       ,--.   `.   '-'   ,'
      (O..O)    `.uuuuu,'
       \==/     _|nnnnn|_
      .'||`. ,-' \_____/ `-.
       _||,-'      | |      `.
      (__)  _,-.   ; |   .'.  `.
      (___)'   |__/___\__|  \(__)
      (__)     :::::::::::  (___)
        ||    :::::::::::::  (__)
        ||    :::::::::::::
             __|   | | _ |__
            (_(_(_,' '._)_)_)
''')

treasure = ('''
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

print(treasure)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

answer1 = input("You walk up to a bridge do you go ** left ** or ** right **. ").lower()
if answer1 == "left":
    answer2 = input("You've come to a lake you see a island in the middle do you ** Wait ** to wait for a boat or do you ** Swim ** to the island. ").lower()
    if answer2 == "wait":
        answer3 = input("You have arrived at the island you see there are 3 doors a ** Red ** ** Yellow ** ** Blue ** pick a door and find the treasure! ").lower()
        if answer3 == "blue":
            print(voodoo_man)
            print("You walk into a room full of fire. The door slams shut. GameOver!")
        elif answer3 == "yellow":
            print(voodoo_man)
            print("You walk into a room full of beasts. GameOver!")
        elif answer3 == "red":
            print(treasure)
            print("You have found the trasure well done. You Win!")
        else:
            print("You chose a door that does not exist. GameOver!")
    else:
        print(voodoo_man)
        print("You start to swim and a giant croc comes and gobbles you up. GameOver!")
else:
    print(voodoo_man)
    print("You fell into a hole. GameOver!")
