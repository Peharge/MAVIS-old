import os
import subprocess

def check_command_installed(command):
    """
    Checks if a command-line tool is installed (e.g., ollama).
    :param command: Command name to check.
    :return: True if installed, False otherwise.
    """
    try:
        result = subprocess.run(["which" if os.name != "nt" else "where", command],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        return result.returncode == 0
    except Exception as e:
        print(f"Error checking command {command}: {e}")
        return False

def check_model_with_ollama(model_name):
    """
    Checks if a specific model is available in ollama.
    :param model_name: The name of the model to check.
    :return: True if available, False otherwise.
    """
    try:
        result = subprocess.run(["ollama", "show", model_name],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                text=True)
        if result.returncode == 0:
            print(f"Model information for {model_name}:\n{result.stdout}")
            return True
        else:
            print(f"Model {model_name} is not available: {result.stderr}")
            return False
    except Exception as e:
        print(f"Error checking model {model_name} with ollama: {e}")
        return False

def install_model_with_ollama(model_name):
    """
    Installs a model using ollama if available.
    :param model_name: The name of the model to install.
    """
    try:
        print(f"Attempting to install model {model_name} with ollama...")
        result = subprocess.run(["ollama", "run", model_name],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                text=True)
        if result.returncode == 0:
            print(f"Model {model_name} installed successfully.")
        else:
            print(f"Failed to install model {model_name}: {result.stderr}")
    except Exception as e:
        print(f"Error installing model {model_name}: {e}")

if __name__ == "__main__":
    # Check if ollama is installed
    ollama_installed = check_command_installed("ollama")
    if ollama_installed:
        print("Ollama is installed.")
    else:
        print("Ollama is not installed. Please install it to proceed.")

    # Check if llama3.2-vision is installed
    llama_installed = check_model_with_ollama("llama3.2-vision")
    if llama_installed:
        print("llama3.2-vision is installed.")
    else:
        print("llama3.2-vision is not installed.")
        if ollama_installed:
            install_model_with_ollama("llama3.2-vision")
