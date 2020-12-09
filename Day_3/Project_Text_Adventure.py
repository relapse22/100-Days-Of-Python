# Christmas Terminal Text Game 
# Find all the presents and help save Christmas
import time as t

print("Welcome to relaspe22's Christmas text game.")
print("You are sent to the Northpole to help santa build all the toys for Christmas")

tree = ('''
                /\                      
               <()>               _._
                /\              ,'`_'`.
             i,'  `.i           )`(_),(
             `,-'  .O    ()     `.,_.,'     ()
            ,O_, `._`.__.||._______________.||.________
          .`'  .  O `'.---.---.---.---.---.---.---.--.-'
         O`'`-i `.' `-'O.-'-.-'-.-'-.-'-.-'-.-'-.-'-.|
         ,' _,'    O ._`.-.-'-.-'-.-'-.-'-.-'-.-'-.-'|
        i`'O    `-' i_  `'i---'---'---'---'.--:-.-'-.|
       `._,-'   i`.'    `.,':::::::::::::::|._|-'-.-'|
      `.'    `-'     `O'  `,'--------------+'_|-.-'-.|
      ,-'_.`O   `._,'  ,-.`-.____________ :|._|-'-.-'|
     O.'  i ,'`- .   `O .i`-O\_  -._ =-' \:|._|-.-'-.|
   ,'_,-'.._    ,.`-._   ,`._`._`-____,o_/:|._|-'-.-'|
    _.._''  _`-'|::|__`-' ''-.'\-------/\--'. |-.-'-.|
 ,''//_/|,''  _/[__]\   ``._____``.          `'-'---''
(   //_\/`-..|//|_.=;=..|__||__||  )
 `._     .=;;=.   |_|_| |__||__||,'
    `--..|=||=|___|_|_|__....--'  ''')

angelina = ('''
   ,---,                                          ,--,                                     
  '  .' \                                       ,--.'|     ,--,                            
 /  ;    '.          ,---,                      |  | :   ,--.'|         ,---,              
:  :       \     ,-+-. /  |  ,----._,.          :  : '   |  |,      ,-+-. /  |             
:  |   /\   \   ,--.'|'   | /   /  ' /   ,---.  |  ' |   `--'_     ,--.'|'   |  ,--.--.    
|  :  ' ;.   : |   |  ,"' ||   :     |  /     \ '  | |   ,' ,'|   |   |  ,"' | /       \   
|  |  ;/  \   \|   | /  | ||   | .\  . /    /  ||  | :   '  | |   |   | /  | |.--.  .-. |  
'  :  | \  \ ,'|   | |  | |.   ; ';  |.    ' / |'  : |__ |  | :   |   | |  | | \__\/: . .  
|  |  '  '--'  |   | |  |/ '   .   . |'   ;   /||  | '.'|'  : |__ |   | |  |/  ," .--.; |  
|  :  :        |   | |--'   `---`-'| |'   |  / |;  :    ;|  | '.'||   | |--'  /  /  ,.  |  
|  | ,'        |   |/       .'__/\_: ||   :    ||  ,   / ;  :    ;|   |/     ;  :   .'   \ 
`--''          '---'        |   :    : \   \  /  ---`-'  |  ,   / '---'      |  ,     .-./ 
                             \   \  /   `----'            ---`-'              `--`---'     
                              `--`-'                                              
''')

print(tree, "\n")
choice1 = input("As you are walking into the workshop you notice its slippery, 'Continue' or 'say' something to a elf: ").lower()
if choice1 == "continue":
    print("As you are walking into the workshop you slip over onto your backside OUCH! Gameover.")
elif choice1 == "say":
    print("You notice a elf outside eating a candycane. You ask him for help and you place a mat for safty")
    t.sleep(1)
    print("Good work sed the elf. could you pass me the wooden hammer on my workbench? you see a metal hammer on the a bench closer than the elf's workbench")
    choice2 = input("grab the 'wooden' or 'metal' hammer: ").lower()
    if choice2 == "wooden":
        print("You walk all the way over to the elf's bench and travel back to him with the hammer.")
        t.sleep(1)
        choice3 = input("You see Santa at the corner of your eye. 'run' over to him or 'shout' his name: ")
        if choice3 == "run":
            print("As you are running to santa one of the elf bump into you and you fall on your backside. Gameover!")
        elif choice3 == "shout":
            print("You shout out to Santa he looks over with a big smile and starts walking towards you.")
            t.sleep(1)
            finalChoice = input("HoHoHo says Santa. have you been helping in the workshop?: ").lower()
            if finalChoice == "yes":
                print("WOW! so kind you will get all the presents you desire for all your hard work I admire. You Win!")
            elif finalChoice == "no":
                print("Well well well. on the naughty list you go! but all can be changed in a quick mo! Gameover.")
            elif finalChoice == "maybe":
                print("Maybe? so that must mean one thing. Gameover!")
            elif finalChoice == "love":
                print(angelina)
            else:
                print("Thats is not a right input, you came so far sorry. Gameover!")
        else:
            print("That is not a right thing to input. Gameover!")
    elif choice2 == "metal":
        print("You grab the metal hammer and a 6ft 300 pound elf grunts at you and chucks you out the workshop. Gameover!")
    else:
        print("That is not a right thing to input. Gameover!")
else:
    print("That is not a right thing to input. Gameover!")



