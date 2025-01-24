#!/bin/bash

USERNAME=$(whoami)
PYTHON_PATH="/home/$USERNAME/PycharmProjects/MAVIS/.env/bin/python"
SCRIPT_PATH_1="/home/$USERNAME/PycharmProjects/MAVIS/info/info-start-mavis-1-3-code-pro.py"
SCRIPT_PATH_2="/home/$USERNAME/PycharmProjects/MAVIS/install/install.py"
SCRIPT_PATH_update="/home/$USERNAME/PycharmProjects/MAVIS/update/update-repository-windows.py"
SCRIPT_PATH_3="/home/$USERNAME/PycharmProjects/MAVIS/install/install-ollama-mavis-1-3-code-pro.py"
SCRIPT_PATH_4="/home/$USERNAME/PycharmProjects/MAVIS/info/info.py"
PYTHON_SCRIPT_PATH="/home/$USERNAME/PycharmProjects/MAVIS/run_with_browser/run_with_browser.py"
SCRIPT_PATH_5="/home/$USERNAME/PycharmProjects/MAVIS/mavis-1-3-main-code-pro.py"

# Check if Python interpreter exists
if [ ! -f "$PYTHON_PATH" ]; then
    echo "Error: Python interpreter not found: $PYTHON_PATH"
    exit 1
fi

# Check if script 1 exists
if [ ! -f "$SCRIPT_PATH_1" ]; then
    echo "Error: Script not found: $SCRIPT_PATH_1"
    exit 1
fi

"$PYTHON_PATH" "$SCRIPT_PATH_1"

# Check if script 2 exists
if [ ! -f "$SCRIPT_PATH_2" ]; then
    echo "Error: Script not found: $SCRIPT_PATH_2"
    exit 1
fi

"$PYTHON_PATH" "$SCRIPT_PATH_2"

# Check if update script exists
if [ ! -f "$SCRIPT_PATH_update" ]; then
    echo "Error: Script not found: $SCRIPT_PATH_update"
    exit 1
fi

"$PYTHON_PATH" "$SCRIPT_PATH_update"

# Check if script 3 exists
if [ ! -f "$SCRIPT_PATH_3" ]; then
    echo "Error: Script not found: $SCRIPT_PATH_3"
    exit 1
fi

"$PYTHON_PATH" "$SCRIPT_PATH_3"

# Check if script 4 exists
if [ ! -f "$SCRIPT_PATH_4" ]; then
    echo "Error: Script not found: $SCRIPT_PATH_4"
    exit 1
fi

"$PYTHON_PATH" "$SCRIPT_PATH_4"

# Check if python script path exists
if [ ! -f "$PYTHON_SCRIPT_PATH" ]; then
    echo "Error: Python script not found: $PYTHON_SCRIPT_PATH"
    exit 1
fi

"$PYTHON_PATH" "$PYTHON_SCRIPT_PATH"

# Check if script 5 exists
if [ ! -f "$SCRIPT_PATH_5" ]; then
    echo "Error: Script not found: $SCRIPT_PATH_5"
    exit 1
fi

"$PYTHON_PATH" "$SCRIPT_PATH_5"

echo
echo "The scripts have been executed, Ollama has been started, and the browser has been opened."
echo "Press any key to exit."
read -n 1 -s
