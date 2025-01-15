import subprocess
import webbrowser
import time
import os

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

# Get the username from the environment variable
username = os.getenv('USERNAME')

# Paths
ollama_path = f"C:\\Users\\{username}\\AppData\\Local\\Programs\\Ollama\\ollama app.exe"
url = "http://127.0.0.1:5000/"

# Start Ollama
try:
    subprocess.Popen([ollama_path])
    print(f"{green}Ollama has been started.{reset}")
except FileNotFoundError:
    print(f"{red}Error: Ollama not found at {ollama_path}{reset}")
    exit(1)

# Wait to give Ollama enough time to start
time.sleep(5)

# Open the browser
webbrowser.open(url)
print(f"The browser has been opened and the URL {url} has been called.")
