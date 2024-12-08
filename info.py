# Englisch | Peharge: This source code is released under the MIT License.
#
# Usage Rights:
# The source code may be copied, modified, and adapted to individual requirements.
# Users are permitted to use this code in their own projects, both for private and commercial purposes.
# However, it is recommended to modify the code only if you have sufficient programming knowledge,
# as changes could cause unintended errors or security risks.
#
# Dependencies and Additional Frameworks:
# The code relies on the use of various frameworks and executes additional files.
# Some of these files may automatically install further dependencies required for functionality.
# It is strongly recommended to perform installation and configuration in an isolated environment
# (e.g., a virtual environment) to avoid potential conflicts with existing software installations.
#
# Disclaimer:
# Use of the code is entirely at your own risk.
# Peharge assumes no liability for damages, data loss, system errors, or other issues
# that may arise directly or indirectly from the use, modification, or redistribution of the code.
#
# Please read the full terms of the MIT License to familiarize yourself with your rights and obligations.

# Deutsch | Peharge: Dieser Quellcode wird unter der MIT-Lizenz veröffentlicht.
#
# Nutzungsrechte:
# Der Quellcode darf kopiert, bearbeitet und an individuelle Anforderungen angepasst werden.
# Nutzer sind berechtigt, diesen Code in eigenen Projekten zu verwenden, sowohl für private als auch kommerzielle Zwecke.
# Es wird jedoch empfohlen, den Code nur dann anzupassen, wenn Sie über ausreichende Programmierkenntnisse verfügen,
# da Änderungen unbeabsichtigte Fehler oder Sicherheitsrisiken verursachen könnten.
#
# Abhängigkeiten und zusätzliche Frameworks:
# Der Code basiert auf der Nutzung verschiedener Frameworks und führt zusätzliche Dateien aus.
# Einige dieser Dateien könnten automatisch weitere Abhängigkeiten installieren, die für die Funktionalität erforderlich sind.
# Es wird dringend empfohlen, die Installation und Konfiguration in einer isolierten Umgebung (z. B. einer virtuellen Umgebung) durchzuführen,
# um mögliche Konflikte mit bestehenden Softwareinstallationen zu vermeiden.
#
# Haftungsausschluss:
# Die Nutzung des Codes erfolgt vollständig auf eigene Verantwortung.
# Peharge übernimmt keinerlei Haftung für Schäden, Datenverluste, Systemfehler oder andere Probleme,
# die direkt oder indirekt durch die Nutzung, Modifikation oder Weitergabe des Codes entstehen könnten.
#
# Bitte lesen Sie die vollständigen Lizenzbedingungen der MIT-Lizenz, um sich mit Ihren Rechten und Pflichten vertraut zu machen.

import platform
import psutil
import os
import shutil
import subprocess
import GPUtil
import re
import sys
import pip
import flask
import matplotlib
import numpy
from importlib.metadata import version
import plotly
import sympy
import torch

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

print ("""                                            
███╗   ███╗ █████╗ ██╗   ██╗██╗███████╗
████╗ ████║██╔══██╗██║   ██║██║██╔════╝
██╔████╔██║███████║██║   ██║██║███████╗
██║╚██╔╝██║██╔══██║╚██╗ ██╔╝██║╚════██║
██║ ╚═╝ ██║██║  ██║ ╚████╔╝ ██║███████║
╚═╝     ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚═╝╚══════╝
                  """)

print(f"""🎉 A warm welcome from Peharge 🎉\n""")

def check_cuda():
    try:
        output = subprocess.check_output(["nvidia-smi"], stderr=subprocess.STDOUT, universal_newlines=True)
        return True if "CUDA" in output else False
    except Exception:
        return False

def check_rocm():
    try:
        output = subprocess.check_output(["rocm-smi"], stderr=subprocess.STDOUT, universal_newlines=True)
        return True if "ROCm" in output else False
    except Exception:
        return False

def get_system_info():
    os_name = platform.system()
    os_version = platform.version()
    os_release = platform.release()
    cpu = platform.processor()
    ram = round(psutil.virtual_memory().total / (1024 ** 3), 2)  # in GB

    total_storage, used_storage, free_storage = shutil.disk_usage("/")
    total_storage = round(total_storage / (1024 ** 3), 2)  # in GB
    free_storage = round(free_storage / (1024 ** 3), 2)  # in GB

    gpus = GPUtil.getGPUs()
    gpu_info = [(gpu.name, gpu.memoryTotal) for gpu in gpus]

    cuda_support = check_cuda()
    rocm_support = check_rocm()

    return {
        "OS": f"{blue}{os_name} {os_release} {reset}(Version: {os_version})",
        "CPU": f"{blue}{cpu}{reset}",
        "RAM": f"{blue}{ram} GB{reset}",
        "Storage": f"Total: {blue}{total_storage} GB{reset}, {blue}Free: {free_storage} GB{reset}",
        "GPU": gpu_info,
        "CUDA Support": f"{blue}{cuda_support}{reset}",
        "ROCm Support": f"{blue}{rocm_support}{reset}"
    }

def get_versions():
    python_version = sys.version.split()[0]
    pip_version = version("pip")
    flask_version = version("flask")
    numpy_version = numpy.__version__
    matplotlib_version = matplotlib.__version__
    plotly_version = plotly.__version__
    sympy_version = sympy.__version__
    math_version = "Built-in (no versioning)"
    torch_version = torch.__version__

    return {
        "Python": python_version,
        "Pip": pip_version,
        "Flask": flask_version,
        "Numpy": numpy_version,
        "Matplotlib": matplotlib_version,
        "Plotly": plotly_version,
        "sympy": sympy_version,
        "torch": torch_version,
        "Math": math_version
    }

def mavis_compatibility(ram, cuda_support, rocm_support):
    if ram < 8:
        return f"{red}MAVIS is not supported on this system{reset}"
    elif 8 <= ram < 15:
        return f"{red}MAVIS in limited mode is supported{reset}"
    elif 15 < ram < 63:
        return f"{green}MAVIS 11B is supported{reset}"
    elif ram > 64:
        return f"{green}MAVIS 90B is supported{reset}"

def remove_color_codes(text):
    return re.sub(r'\033\[[0-9;]*m', '', text)

def main():
    system_info = get_system_info()
    versions = get_versions()

    print("System Information:")
    print("-------------------")
    for key, value in system_info.items():
        if key == "GPU":
            if value:
                print(f"{key}: {', '.join([f'{gpu[0]} ({gpu[1]} MB)' for gpu in value])}")
            else:
                print(f"{key}: No GPU detected")
        else:
            print(f"{key}: {value}")

    ram_str = remove_color_codes(system_info["RAM"])
    ram = float(ram_str.split()[0])

    cuda_support = check_cuda()
    rocm_support = check_rocm()

    compatibility = mavis_compatibility(ram, cuda_support, rocm_support)
    gpu_or_cpu = "GPU" if cuda_support or rocm_support else "CPU"

    print("\nPackage Versions:")
    print("-------------------")
    for key, value in versions.items():
        print(f"{key}: {blue}{value}{reset}")

    print("\nCompatibility and Execution Mode:")
    print("-----------------------------------")
    print(compatibility)
    print(f"Execution Mode: {blue}{gpu_or_cpu}{reset}")

    print("\nFlask information:")
    print("-----------------------------------")

if __name__ == "__main__":
    main()