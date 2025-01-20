#!/bin/bash

USERNAME=$(whoami)
PYTHON_PATH="/home/$USERNAME/PycharmProjects/MAVIS/.env/bin/python"
SCRIPT_PATH_1="/home/$USERNAME/PycharmProjects/MAVIS/info/info-start-mavis-1-3-math.py"
SCRIPT_PATH_2="/home/$USERNAME/PycharmProjects/MAVIS/install/install.py"
SCRIPT_PATH_3="/home/$USERNAME/PycharmProjects/MAVIS/install/install-ollama-mavis-1-3-math.py"
SCRIPT_PATH_4="/home/$USERNAME/PycharmProjects/MAVIS/info/info.py"
PYTHON_SCRIPT_PATH="/home/$USERNAME/PycharmProjects/MAVIS/run_with_browser/run_with_browser.py"
SCRIPT_PATH_5="/home/$USERNAME/PycharmProjects/MAVIS/main/mavis-1-3-main-math.py"

if [[ ! -f "$PYTHON_PATH" ]]; then
    echo "Error: Python interpreter not found: $PYTHON_PATH"
    exit 1
fi

if [[ ! -f "$SCRIPT_PATH_1" ]]; then
    echo "Error: Script not found: $SCRIPT_PATH_1"
    exit 1
fi

"$PYTHON_PATH" "$SCRIPT_PATH_1"

if [[ ! -f "$SCRIPT_PATH_2" ]]; then
    echo "Error: Script not found: $SCRIPT_PATH_2"
    exit 1
fi

"$PYTHON_PATH" "$SCRIPT_PATH_2"

if [[ ! -f "$SCRIPT_PATH_3" ]]; then
    echo "Error: Script not found: $SCRIPT_PATH_3"
    exit 1
fi

"$PYTHON_PATH" "$SCRIPT_PATH_3"

if [[ ! -f "$SCRIPT_PATH_4" ]]; then
    echo "Error: Script not found: $SCRIPT_PATH_4"
    exit 1
fi

"$PYTHON_PATH" "$SCRIPT_PATH_4"

if [[ ! -f "$PYTHON_SCRIPT_PATH" ]]; then
    echo "Error: Python script not found: $PYTHON_SCRIPT_PATH"
    exit 1
fi

"$PYTHON_PATH" "$PYTHON_SCRIPT_PATH"

if [[ ! -f "$SCRIPT_PATH_5" ]]; then
    echo "Error: Script not found: $SCRIPT_PATH_5"
    exit 1
fi

"$PYTHON_PATH" "$SCRIPT_PATH_5"

echo
echo "The scripts have been executed, Ollama has been started, and the browser has been opened."
read -p "Press any key to exit."
