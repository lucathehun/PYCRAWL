
import json

# Reading from a file
with open("playerData.txt", "r") as file:
    playerData = json.load(file)

playerData['gameStage']='/wizard/firstSteps.py'

print('''
Story idk yet.
''')

## playerData = playerName, playerClass, playerEquiptment, ganeStage

with open("playerData.txt", "w") as file:
    json.dump(playerData, file)

