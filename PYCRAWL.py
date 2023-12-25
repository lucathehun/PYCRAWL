
import time
import runpy
import json


print('''

 ██▓███ ▓██   ██▓ ▄████▄   ██▀███   ▄▄▄       █     █░ ██▓
▓██░  ██▒▒██  ██▒▒██▀ ▀█  ▓██ ▒ ██▒▒████▄    ▓█░ █ ░█░▓██▒
▓██░ ██▓▒ ▒██ ██░▒▓█    ▄ ▓██ ░▄█ ▒▒██  ▀█▄  ▒█░ █ ░█ ▒██░
▒██▄█▓▒ ▒ ░ ▐██▓░▒▓▓▄ ▄██▒▒██▀▀█▄  ░██▄▄▄▄██ ░█░ █ ░█ ▒██░
▒██▒ ░  ░ ░ ██▒▓░▒ ▓███▀ ░░██▓ ▒██▒ ▓█   ▓██▒░░██▒██▓ ░██████▒
▒▓▒░ ░  ░  ██▒▒▒ ░ ░▒ ▒  ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ▓░▒ ▒  ░ ▒░▓  ░
░▒ ░     ▓██ ░▒░   ░  ▒     ░▒ ░ ▒░  ▒   ▒▒ ░  ▒ ░ ░  ░ ░ ▒  ░
░░       ▒ ▒ ░░  ░          ░░   ░   ░   ▒     ░   ░    ░ ░
         ░ ░     ░ ░         ░           ░  ░    ░        ░  ░
         ░ ░     ░
''')


print("""

                                   ....
                                .'' .'''
.                             .'   :
\\\                          .:    :
 \\\                        _:    :       ..----.._
  \\\                    .:::.....:::.. .'         ''.
   \\\                 .'  #-. .-######'     #        '.
    \\\                 '.##'/ ' ################       :
     \\\                  #####################         :
      \\\               ..##.-.#### .''''###'.._        :
       \\\             :--:########:            '.    .' :
        \\\..__...--.. :--:#######.'   '.         '.     :
        :      :  : : '':'-:'':'::        .         '.  .'
        '--- '''..: :    ':    '..'''.      '.        :'
           \\\  :: : :     '      ''''''.     '.      .:
            \\\ ::  : :     '            '.      '      :
             \\\::   : :           ....' ..:       '     '.
              \\\::  : :    .....####\\ .~~.:.             :
               \\\':.:.:.:'#########.===. ~ |.'-.   . '''.. :
                \\\    .'  ########## \ \ _.' '. '-.       '''.
                :\\\  :     ########   \ \      '.  '-.        :
               :  \\\'    '   #### :    \ \      :.    '-.      :
              :  .'\\\   :'  :     :     \ \       :      '-.    :
             : .'  .\\\  '  :      :     :\ \       :        '.   :
             ::   :  \\\'  :.      :     : \ \      :          '. :
             ::. :    \\\  : :      :    ;  \ \     :           '.:
              : ':    '\\\ :  :     :     :  \:\     :        ..'
                 :    ' \\\ :        :     ;  \|      :   .'''
                 '.   '  \\\:                         :.''
                  .:..... \\\:       :            ..''
                 '._____|'.\\\......'''''''.:..'''
                            \\\
""")

# Character creation screen 
## class need to add ascii art 
playerClass = input("""
pick your class 

Wizard      [W]
Knight      [K]
Thief       [T]
Assassin    [A]
Range       [R]
>""").upper()

## Startequipment 
if playerClass == 'W':
    choice = input('choose your starting weapon [s] for staff [b] for book\n>').lower()
    if choice == 's':
        playerEquiptment = 'staff'
    elif choice == 'b':
        playerEquiptment = 'book'
elif playerClass == 'K':
    choice = input('choose your starting weapon [s] for sword [m] for morningstar\n>').lower()
    if choice == 's':
        playerEquiptment = 'sword'
    elif choice == 'm':
        playerEquiptment = 'morningstar'
elif playerClass == 'T':
    choice = input('choose your starting weapon [f] for falchion [d] for dagger\n>').lower()
    if choice == 'f':
        playerEquiptment = 'falchion'
    elif choice == 'd':
        playerEquiptment = 'dagger'
elif playerClass == 'A':
    choice = input('choose your starting weapon [r] for rapier [c] for crossbow\n>').lower()
    if choice == 'r':
        playerEquiptment = 'rapier'
    elif choice == 'c':
        playerEquiptment = 'crossbow'
elif playerClass == 'R':
    choice = input('choose your starting weapon [r] for recursive bow [l] for longbow\n>').lower()
    if choice == 'r':
        playerEquiptment = 'recursiveBow'
    elif choice == 'l':
        playerEquiptment = 'longbow'



## Gravegift
choice = input("""
what have your long gone relatives left you for your afterlife?

mystery potion      [?]
bag of gold         [$]
good luck charm     [*]
>""")

if choice == '?':
    gravegift = 'mysteryPotion'
elif choice == '$':
    gravegift = 'bagOfGold'
elif choice == '*':
    gravegift = 'goodLuckCharm'

print()

playerGender = input("what's your gender [M] for man [W] for woman or [N] non of those 2.\n>").upper()
if playerGender == 'M':
    personalPro = 'he'
    personalPro2 = 'him'
    possesivePro = 'his'
elif playerGender == 'W':
    personalPro = 'she'
    personalPro2 = 'her'
    possesivePro = 'hers'
else: 
    personalPro = 'they'
    personalPro2 = 'them'
    possesivePro = 'theirs'

print()
## Name
playerName = input("please enter your name if you wish to start this Adventure.\n> ")

print() # Move to next line

text = f"""
this is the story of a warrior named {playerName} not much is known about {personalPro2}, since {personalPro} was not born into this world by usual means.
{personalPro} who died long before our mysterious adventure unfolds was sent back into this cruel world by the protective spirits of this world.
"""

for char in text:
    print(char, end='', flush=True)
    time.sleep(0.03)  # Adjust the sleep duration (in seconds) for your preferred speed

print()  # Move to the next line after printing

## Safe player data 
playerData={}
playerData['playerGender'] = playerGender
playerData['playerName'] = playerName
playerData['playerClass'] = playerClass
playerData['playerEquiptment'] = [playerEquiptment, gravegift]

with open("playerData.txt", "w") as file:
    json.dump(playerData, file)

print(playerData)

## Go to next part of story 
if playerClass == 'W':
    runpy.run_path('wizard/firstSteps.py')
elif playerClass == 'K':
    runpy.run_path('knight/firstSteps.py')
elif playerClass == 'T':
    runpy.run_path('thief/firstSteps.py')
elif playerClass == 'A':
    runpy.run_path('assassin/firstSteps.py')
elif playerClass == 'R':
    runpy.run_path('ranger/firstSteps.py')

