
#!/bin/bash
# Find the directory the script is in
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

cd "$DIR"
# Run the Python script using its relative path
python3 "$DIR/startGame.py"
