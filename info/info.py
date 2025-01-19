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

# Français | Peharge: Ce code source est publié sous la licence MIT.
#
# Droits d'utilisation:
# Le code source peut être copié, édité et adapté aux besoins individuels.
# Les utilisateurs sont autorisés à utiliser ce code dans leurs propres projets, à des fins privées et commerciales.
# Il est cependant recommandé d'adapter le code uniquement si vous avez des connaissances suffisantes en programmation,
# car les modifications pourraient provoquer des erreurs involontaires ou des risques de sécurité.
#
# Dépendances et frameworks supplémentaires:
# Le code est basé sur l'utilisation de différents frameworks et exécute des fichiers supplémentaires.
# Certains de ces fichiers peuvent installer automatiquement des dépendances supplémentaires requises pour la fonctionnalité.
# Il est fortement recommandé d'effectuer l'installation et la configuration dans un environnement isolé (par exemple un environnement virtuel),
# pour éviter d'éventuels conflits avec les installations de logiciels existantes.
#
# Clause de non-responsabilité:
# L'utilisation du code est entièrement à vos propres risques.
# Peharge n'assume aucune responsabilité pour tout dommage, perte de données, erreurs système ou autres problèmes,
# pouvant découler directement ou indirectement de l'utilisation, de la modification ou de la diffusion du code.
#
# Veuillez lire l'intégralité des termes et conditions de la licence MIT pour vous familiariser avec vos droits et responsabilités.

import os
import subprocess
import re
import sys
import sysconfig
import json
import platform
import cpuinfo
import psutil
import shutil
import time
import socket
import GPUtil

# Farbcodes definieren
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

# Funktion zur Prüfung auf CUDA-Unterstützung
def check_cuda():
    try:
        import torch
        return torch.cuda.is_available()
    except ImportError:
        return False


# Funktion zur Prüfung auf ROCm-Unterstützung
def check_rocm():
    try:
        import tensorflow as tf
        return "ROCm" in tf.__version__
    except ImportError:
        return False

def get_system_info():
    # OS-Informationen
    os_name = platform.system()
    os_version = platform.version()
    os_release = platform.release()
    os_arch = platform.architecture()[0]  # 32-bit oder 64-bit

    # CPU Informationen
    cpu_info = cpuinfo.get_cpu_info()
    cpu_model = cpu_info.get("brand_raw", "N/A")  # CPU-Modell
    cpu_arch = cpu_info.get("arch", "N/A")  # Architektur
    cpu_cores = psutil.cpu_count(logical=False)  # Physische Kerne
    cpu_threads = psutil.cpu_count(logical=True)  # Logische Kerne
    cpu_freq = psutil.cpu_freq().max if psutil.cpu_freq() else "N/A"  # Max Taktfrequenz in MHz

    # RAM Informationen
    ram = psutil.virtual_memory()
    ram_total = round(ram.total / (1024 ** 3), 2)  # in GB
    ram_used = round(ram.used / (1024 ** 3), 2)  # in GB
    ram_free = round(ram.available / (1024 ** 3), 2)  # in GB
    ram_usage = ram.percent  # Prozentuale RAM-Nutzung

    # Swap Informationen
    swap = psutil.swap_memory()
    swap_total = round(swap.total / (1024 ** 3), 2)  # in GB
    swap_used = round(swap.used / (1024 ** 3), 2)  # in GB
    swap_free = round(swap.free / (1024 ** 3), 2)  # in GB

    # Festplatteninformationen
    total_storage, used_storage, free_storage = shutil.disk_usage("/")
    total_storage = round(total_storage / (1024 ** 3), 2)  # in GB
    used_storage = round(used_storage / (1024 ** 3), 2)  # in GB
    free_storage = round(free_storage / (1024 ** 3), 2)  # in GB
    partitions = psutil.disk_partitions()

    # Netzwerkinformationen
    hostname = socket.gethostname()
    try:
        ip_address = socket.gethostbyname(hostname)
    except socket.gaierror:
        ip_address = "Unknown"

    # Netzwerk-Interfaces
    network_interfaces = psutil.net_if_addrs()
    interfaces_info = []
    for interface, addresses in network_interfaces.items():
        interface_details = f"- {interface}:\n"
        for address in addresses:
            if address.family == socket.AF_INET:
                interface_details += f"  - IPv4: {address.address}\n"
            elif address.family == socket.AF_INET6:
                interface_details += f"  - IPv6: {address.address}\n"
            elif address.family == psutil.AF_LINK:
                interface_details += f"  - MAC: {address.address}\n"
        interfaces_info.append(interface_details)
    interfaces_formatted = "\n".join(interfaces_info)

    # Load Average
    if os_name == "Windows":
        load_avg = f"CPU Usage: {psutil.cpu_percent(interval=1)}%"
    else:
        try:
            load_avg_values = os.getloadavg()
            load_avg = f"1m: {load_avg_values[0]}, 5m: {load_avg_values[1]}, 15m: {load_avg_values[2]}"
        except OSError:
            load_avg = "Not available"

    # Uptime des Systems
    uptime_seconds = time.time() - psutil.boot_time()
    uptime_str = time.strftime("%H:%M:%S", time.gmtime(uptime_seconds))

    # Benutzerinformationen
    user_info = psutil.users()
    user_data_formatted = "\n".join([
        f"  - User: {user.name}, Terminal: {user.terminal or 'N/A'}, Started: {time.ctime(user.started)}"
        for user in user_info
    ])

    # Formatierte Ausgabe
    system_info = {
        f"{blue}OS{reset}": f"{os_name} {os_release} (Version: {os_version}), Architecture: {os_arch}",
        f"{blue}Hostname{reset}": f"{hostname}",
        f"{blue}IP Address{reset}": f"{ip_address}",
        f"{blue}CPU{reset}": f"{cpu_model}, Architecture: {cpu_arch}, Cores: {cpu_cores}, Threads: {cpu_threads}, Max Frequency: {cpu_freq} MHz",
        f"{blue}RAM{reset}": f"Total: {ram_total} GB, Used: {ram_used} GB, Free: {ram_free} GB, Usage: {ram_usage}%",
        f"{blue}Swap{reset}": f"Total: {swap_total} GB, Used: {swap_used} GB, Free: {swap_free} GB",
        f"{blue}Storage{reset}": f"Total: {total_storage} GB, Used: {used_storage} GB, Free: {free_storage} GB",
        f"{blue}System Load Average{reset}": load_avg,
        f"{blue}Uptime{reset}": uptime_str,
        f"{blue}Network Interfaces{reset}": f"\n{interfaces_formatted}",
        f"{blue}Disk Partitions{reset}": "\n".join([f"- Part Device: {part.device} Part Mountpoint: {part.mountpoint}" for part in partitions]),
        f"{blue}User Information{reset}": user_data_formatted,
    }

    return system_info

def check_python_interpreter():
    # Den Pfad zum Python-Interpreter definieren
    python_path = r'C:\Users\%USERNAME%\PycharmProjects\MAVIS\.env\Scripts\python.exe'
    python_path = os.path.expandvars(python_path)  # Variablen im Pfad expandieren

    print(f"\nPython Information:\n-----------------------------------\nChecking for Python interpreter at: {python_path}")

    # Definiere, wie oft der Versuch wiederholt werden soll
    attempts = 5
    for attempt in range(attempts):
        if os.path.exists(python_path):
            try:
                print(f"Attempt {attempt + 1} of {attempts}: Trying to start Python interpreter...")
                # Versuche, die Version des Python-Interpreters zu bekommen
                result = subprocess.run([python_path, '--version'], capture_output=True, text=True)

                if result.returncode == 0:
                    # Erfolg: Ausgabe der Python-Version
                    print(f"{green}Python interpreter started successfully: {result.stdout.strip()}{reset}")
                    print(f"Interpreter path: {python_path}")
                    print(f"Interpreter version: {result.stdout.strip()}")

                    # Weitere Details zur virtuellen Umgebung:
                    check_pip_version(python_path)
                    list_installed_packages(python_path)
                    display_venv_environment_variables(python_path)
                    display_venv_details(python_path)

                    # Detaillierte Systeminformationen
                    display_system_info()

                    break  # Interpreter erfolgreich gestartet, verlasse die Schleife
                else:
                    print(f"{red}Error starting Python interpreter: {result.stderr.strip()}{reset}")
            except Exception as e:
                # Ausnahmebehandlung, falls der Versuch fehlschlägt
                print(f"{red}Error running Python interpreter: {e}{reset}")
                print(f"Python path: {python_path}")
        else:
            # Falls der Python-Interpreter nicht gefunden wird
            print(f"{red}Python interpreter not found at: {python_path}{reset}")
            break  # Verlasse die Schleife, wenn der Interpreter nicht gefunden wurde

        # Optional: Füge eine Verzögerung hinzu, bevor der Versuch erneut unternommen wird
        if attempt < attempts - 1:  # Verzögerung nach dem letzten Versuch vermeiden
            print(f"Retrying in 2 seconds...\n")
            time.sleep(2)


def check_pip_version(python_path):
    """Überprüfen Sie die Pip-Version in der virtuellen Umgebung."""
    try:
        result = subprocess.run([python_path, '-m', 'pip', '--version'], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"{green}pip version: {result.stdout.strip()}{reset}")
        else:
            print(f"{red}Error checking pip version: {result.stderr.strip()}{reset}")
    except Exception as e:
        print(f"{red}Error checking pip version: {e}{reset}")


def list_installed_packages(python_path):
    """Listet alle installierten Pakete in der virtuellen Umgebung auf."""
    try:
        result = subprocess.run([python_path, '-m', 'pip', 'list'], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"{green}Installed packages:\n{result.stdout.strip()}{reset}")
        else:
            print(f"{red}Error listing installed packages: {result.stderr.strip()}{reset}")
    except Exception as e:
        print(f"{red}Error listing installed packages: {e}{reset}")


def display_venv_environment_variables(python_path):
    """Umgebungsvariablen für die virtuelle Umgebung anzeigen."""
    venv_path = os.path.dirname(os.path.dirname(python_path))  # Der Pfad zur venv
    print(f"Virtual environment path: {venv_path}")

    # Auflisten der wichtigsten Umgebungsvariablen
    try:
        env_vars = os.environ.copy()
        venv_vars = {key: env_vars[key] for key in env_vars if venv_path in env_vars.get(key, '')}
        print(f"{green}Virtual environment-related environment variables:{reset}")
        for key, value in venv_vars.items():
            print(f"{key}: {value}")
    except Exception as e:
        print(f"{red}Error displaying environment variables: {e}{reset}")


def display_venv_details(python_path):
    """Zeigen Sie zusätzliche Venv-Details an, wie den Speicherort von ausführbaren Dateien und Bibliotheken."""
    try:
        venv_path = os.path.dirname(os.path.dirname(python_path))  # Der Pfad zur venv
        executables_path = os.path.join(venv_path, 'Scripts')
        libraries_path = os.path.join(venv_path, 'Lib', 'site-packages')

        print(f"Virtual environment executables path: {executables_path}")
        print(f"Virtual environment libraries path: {libraries_path}")
        print(f"Python executable: {python_path}")

        # Zusätzliche Systemdetails
        print(f"\nSystem Python paths:\n-----------------------------------")
        for path in sys.path:
            print(path)
    except Exception as e:
        print(f"{red}Error displaying virtual environment details: {e}{reset}")


def display_system_info():
    """Detaillierte Systeminformationen anzeigen."""
    try:
        system_info = {
            # "OS": platform.system(),
            # "OS Version": platform.version(),
            # "OS Architecture": platform.architecture(),
            "Python Implementation": platform.python_implementation(),
            "Python Version": platform.python_version(),
            "Processor": platform.processor(),
            "Machine Type": platform.machine(),
            "System Configuration": platform.uname(),
            "Python Config (sysconfig)": sysconfig.get_config_vars()
        }

        print(f"\nSystem Information from Python:\n-----------------------------------")
        print(json.dumps(system_info, indent=4))
    except Exception as e:
        print(f"{red}Error displaying system Information: {e}{reset}")

def mavis_compatibility(ram):
    # Konvertiere den Gesamt-RAM in GB
    ram_gb = ram.total / (1024 ** 3)  # ram.total gibt den Gesamt-RAM in Bytes

    if ram_gb < 8:
        return f"{red}MAVIS is not supported on this system{reset}"
    elif 8 <= ram_gb <= 14:
        return f"{red}MAVIS in limited mode is supported{reset}"
    elif 15 <= ram_gb <= 64:
        return f"{green}MAVIS 11B is supported{reset}"
    elif ram_gb > 64:
        return f"{green}MAVIS 90B is supported{reset}"

def remove_color_codes(text):
    return re.sub(r'\033\[[0-9;]*m', '', text)

import psutil

def main():
    # Holen der Systeminfos (inkl. RAM)
    ram = psutil.virtual_memory()  # Das ganze psutil-Objekt, nicht nur der float-Wert
    print("\nSystem Information:")
    print("-------------------")
    for key, value in get_system_info().items():
        print(f"{key}: {value}")

    check_python_interpreter()

    # Kompatibilität basierend auf dem RAM-Objekt prüfen
    compatibility = mavis_compatibility(ram)

    print("\nCompatibility and Execution Mode:")
    print("-----------------------------------")
    print(compatibility)

    print("\nClient Information:")
    print("-----------------------------------")

if __name__ == "__main__":
    main()
