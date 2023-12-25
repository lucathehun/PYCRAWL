import json
import runpy
import os

# Define default player data
default_player_data = {
    'playerGender': '',
    'playerName': '',
    'playerClass': '',
    'playerEquiptment': '',
    'gameStage': ''
}

# Try to load player data from file, use default if file is empty or not found
try:
    with open("playerData.txt", "r") as file:
        playerData = json.load(file)
except (json.JSONDecodeError, FileNotFoundError):
    playerData = default_player_data

# Execute the appropriate Python file based on the game stage
if playerData['gameStage'] == '':
    # Get the directory of the current script (startGame.py)
    dir_path = os.path.dirname(os.path.abspath(__file__))

    # Construct the relative path to PYCRAWL.py
    pycrawl_path = os.path.join(dir_path, 'PYCRAWL.py')

    # Run PYCRAWL.py using its relative path
    runpy.run_path(pycrawl_path)
else:
    # Get the directory of the current script (startGame.py)
    dir_path = os.path.dirname(os.path.abspath(__file__))

    # Construct the relative path to PYCRAWL.py
    gameStage_path = os.path.join(dir_path, playerData['gameStage'])

    # Run PYCRAWL.py using its relative path
    runpy.run_path(gameStage_path)

