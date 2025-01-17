import subprocess
import webbrowser
import time
import os
import platform

# ANSI color codes
red = "\033[91m"
green = "\033[92m"
yellow = "\033[93m"
blue = "\033[94m"
magenta = "\033[95m"
cyan = "\033[96m"
white = "\033[97m"
black = "\033[30m"
orange = "\033[38;5;214m"
reset = "\033[0m"
bold = "\033[1m"

# Enable ANSI escape sequence support on Windows
if os.name == "nt":
    os.system("")

# Get the username from the environment variable
username = os.getenv('USERNAME')

# Paths
ollama_path = f"C:\\Users\\{username}\\AppData\\Local\\Programs\\Ollama\\ollama app.exe"
url = "http://127.0.0.1:5000/"

# Start Ollama
try:
    subprocess.Popen([ollama_path], shell=True)
    print(f"{green}Ollama has been started.{reset}")
except FileNotFoundError:
    print(f"{red}Error: Ollama not found at {ollama_path}{reset}")
    exit(1)
except Exception as e:
    print(f"{red}Unexpected error: {e}{reset}")
    exit(1)

# Wait to give Ollama enough time to start
time.sleep(5)

# Open the browser
try:
    webbrowser.open(url)
    print(f"The browser has been opened and the URL {yellow}{url}{reset} has been called.")

    # Get browser information
    browser_name = webbrowser._tryorder[0] if webbrowser._tryorder else 'Unknown browser'

    # Check if the browser is Edge
    if "windows-default" not in browser_name.lower():
        print(f"{yellow}Warning: You are not using Microsoft Edge.{reset}")
        print(f"{yellow}There may be issues. It is recommended to use Edge for optimal performance.{reset}")
    else:
        print(f"{green}You are using Microsoft Edge. No issues expected.{reset}")

    print(f"Browser: {browser_name}")
    print("\nFlask information:")
    print("-----------------------------------")

except Exception as e:
    print(f"{red}Error opening browser: {e}{reset}")
