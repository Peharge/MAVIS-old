#!/bin/bash

USERNAME=$(whoami)
PYTHON_PATH="/home/$USERNAME/PycharmProjects/MAVIS/.env/bin/python"
SCRIPT_PATH_1="/home/$USERNAME/PycharmProjects/MAVIS/main/main-macos-linux.py"

if [[ ! -f "$PYTHON_PATH" ]]; then
    echo "Error: Python interpreter not found: $PYTHON_PATH"
    exit 1
fi

if [[ ! -f "$SCRIPT_PATH_1" ]]; then
    echo "Error: Script not found: $SCRIPT_PATH_1"
    exit 1
fi

"$PYTHON_PATH" "$SCRIPT_PATH_1"

echo
echo "The scripts have been executed, Ollama has been started, and the browser has been opened."
read -p "Press any key to exit."
