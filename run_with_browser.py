import subprocess
import webbrowser
import time
import os

# Get the username from the environment variable
username = os.getenv('USERNAME')

# Paths
ollama_path = f"C:\\Users\\{username}\\AppData\\Local\\Programs\\Ollama\\ollama app.exe"
url = "http://127.0.0.1:5000/"

# Start Ollama
try:
    subprocess.Popen([ollama_path])
    print("Ollama has been started.")
except FileNotFoundError:
    print(f"Error: Ollama not found at {ollama_path}")
    exit(1)

# Wait to give Ollama enough time to start
time.sleep(5)

# Open the browser
webbrowser.open(url)
print(f"The browser has been opened and the URL {url} has been called.")
