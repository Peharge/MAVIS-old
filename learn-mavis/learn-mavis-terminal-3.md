<p align="center">
    <img src="https://github.com/Peharge/MAVIS/blob/main/readme-img/mavis-terminal-3-banner.png" alt="mavis" width="800" style="margin: 10px;">
</p>

# _**Mavis Terminal - Command Reference and Setup Guide**_

## **Overview**  
Mavis Terminal is a powerful command-line interface designed to streamline development, system monitoring, and AI model execution. This document provides a comprehensive list of available commands, along with usage guidelines for `pip` and PowerShell.  

---

## **Command Reference**  

Below is a structured list of available commands and their corresponding functions:  

### **Environment Setup & Updates**  
| Command | Description |
|---------|-------------|
| `env install` | Installs the Mavis environment, ensuring all dependencies are correctly set up. |
| `install env` | Equivalent to `env install`, used for environment setup. |
| `mavis env install` | Alternative command for installing the Mavis environment. |
| `env update` | Updates the Mavis environment to the latest version. |
| `update env` | Alternative command for updating the Mavis environment. |
| `mavis env update` | Another equivalent command for updating the Mavis environment. |
| `update` | Fetches and applies the latest updates for the Mavis repository. |
| `mavis update` | Alternative command for updating the Mavis repository. |
| `update mavis` | Equivalent to `mavis update`. |

### **System & Security**  
| Command | Description |
|---------|-------------|
| `security` | Performs a security check to identify vulnerabilities in the system. |
| `mavis security` | Alternative command for security checks. |
| `securitycheck` | Executes a security check to ensure system integrity. |
| `info` | Displays system and environment details related to Mavis. |
| `mavis info` | Alternative command for retrieving system information. |
| `info mavis` | Equivalent to `mavis info`. |
| `neofetch` | Retrieves system hardware and software information in a concise format. |

### **Development & Execution**  
| Command | Description |
|---------|-------------|
| `jupyter` | Launches a Jupyter Notebook instance for interactive computing. |
| `run jupyter` | Alternative command to start Jupyter Notebook. |
| `run mavis-1-5-main` | Executes the primary Mavis 1.5 module. |
| `run mavis-1-5-math` | Runs the mathematics-focused Mavis 1.5 module. |
| `run mavis-1-5-math-pro` | Executes the advanced mathematics module of Mavis 1.5. |
| `run mavis-1-5-math-ultra` | Runs the ultra-performance mathematics module of Mavis 1.5. |
| `run mavis-1-5-code` | Executes the coding-related Mavis 1.5 module. |
| `run mavis-3-main` | Launches the core Mavis 3 module. |

### **AI Model Execution**  
| Command | Description |
|---------|-------------|
| `run deepseek-r1:14b` | Runs the DeepSeek model version R1 with 14 billion parameters. |
| `run deepseek-r1:70b` | Executes the DeepSeek R1 model with 70 billion parameters. |
| `run llama3.1:70b` | Runs the LLaMA 3.1 model with 70 billion parameters. |
| `run llama3.1:405b` | Launches the LLaMA 3.1 model with 405 billion parameters. |
| `run mistral` | Executes the Mistral AI model for advanced natural language processing. |
| `run phi4` | Starts the Phi-4 AI model for computational tasks. |
| `run qwen2.5:14b` | Runs the Qwen 2.5 model with 14 billion parameters. |

### **Package Installation & System Tools**  
| Command | Description |
|---------|-------------|
| `install ollama mavis-3-main` | Installs the Ollama package required for the Mavis 3 main module. |
| `install ollama mavis-1-5-math` | Installs the necessary Ollama dependencies for Mavis 1.5 math module. |
| `grafana` | Starts the Grafana visualization and monitoring tool. |
| `run grafana` | Alternative command to launch Grafana. |
| `install grafana` | Installs and runs Grafana. |
| `account` | Manages user account settings within the Mavis system. |

### **Help & Documentation**  
| Command | Description |
|---------|-------------|
| `help` | Displays the list of available commands and their descriptions. |
| `run mavis` | Initializes the Mavis installer for system-wide setup. |

---

## **Using `pip` for Package Management**  

`pip` (Python Package Installer) is the standard package manager for Python. It allows users to install and manage dependencies required by Python applications.  

### **Basic Commands**  
- **Check if `pip` is installed:**  
  ```sh
  python -m pip --version
  ```
- **Upgrade `pip` to the latest version:**  
  ```sh
  python -m pip install --upgrade pip
  ```
- **Install a package:**  
  ```sh
  pip install <package_name>
  ```
- **Uninstall a package:**  
  ```sh
  pip uninstall <package_name>
  ```
- **List installed packages:**  
  ```sh
  pip list
  ```
- **Check for outdated packages:**  
  ```sh
  pip list --outdated
  ```
- **Update all outdated packages:**  
  ```sh
  pip install --upgrade $(pip list --outdated | awk 'NR>2 {print $1}')
  ```

---

## **Introduction to PowerShell**  

PowerShell is a powerful scripting language and command-line shell designed for system administration and automation on Windows.  

### **Common PowerShell Commands**  
| Command | Description |
|---------|-------------|
| `Get-Help` | Displays help information about PowerShell commands. |
| `Get-Process` | Lists currently running processes. |
| `Get-Service` | Shows the status of system services. |
| `Get-Command` | Displays all available PowerShell commands. |
| `Set-ExecutionPolicy RemoteSigned` | Allows running scripts on the system. |
| `Start-Process` | Launches a new process. |
| `Stop-Process -Name <process_name>` | Terminates a running process. |
| `New-Item -ItemType File -Path "C:\example.txt"` | Creates a new file. |
| `Remove-Item "C:\example.txt"` | Deletes a specified file. |

### **Running a Python Script in PowerShell**  
To execute a Python script using PowerShell, navigate to the script's directory and run:  
```powershell
python script_name.py
```

### **Running Mavis in PowerShell**  
Navigate to the Mavis directory and execute:  
```powershell
python mavis-installer-3-main-windows.py
```
