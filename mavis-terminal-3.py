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

import sys
import getpass
import os
import subprocess
import threading
import time

sys.stdout.reconfigure(encoding='utf-8')
user_name = getpass.getuser()

# Farbcodes definieren (kleingeschrieben)
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


def print_banner():
    print(f"""
{blue}      ██╗     █╗      {reset}
{blue}     ████╗   ███╗     {reset}   ███╗   ███╗ █████╗ ██╗   ██╗██╗███████╗    ████████╗███████╗██████╗ ███╗   ███╗██╗███╗   ██╗ █████╗ ██╗     
{blue}    ██████╗  ████╗    {reset}   ████╗ ████║██╔══██╗██║   ██║██║██╔════╝    ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║████╗  ██║██╔══██╗██║     
{blue}   ████████╗  ████╗   {reset}   ██╔████╔██║███████║██║   ██║██║███████╗       ██║   █████╗  ██████╔╝██╔████╔██║██║██╔██╗ ██║███████║██║     
{blue}  ████╔█████╗  ████╗  {reset}   ██║╚██╔╝██║██╔══██║╚██╗ ██╔╝██║╚════██║       ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║██║╚██╗██║██╔══██║██║     
{blue} ████╔╝╚█████╗  ████╗ {reset}   ██║ ╚═╝ ██║██║  ██║ ╚████╔╝ ██║███████║       ██║   ███████╗██║  ██║██║ ╚═╝ ██║██║██║ ╚████║██║  ██║███████╗
{blue} ╚═══╝  ╚███╔╝  ╚═══╝ {reset}   ╚═╝     ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚═╝╚══════╝       ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝
{blue}         ╚█╔╝         {reset}
{blue}          ╚╝          {reset}    
""")
    print(f"A warm welcome, {blue}{user_name}{reset}, to MAVIS!")


def set_python_path():
    python_path = f"C:\\Users\\{os.getlogin()}\\PycharmProjects\\MAVIS\\.env\\Scripts\\python.exe"
    os.environ["PYTHON_PATH"] = python_path
    print(f"PYTHON_PATH set to {python_path}")


def run_command(command, shell=False):
    python_path = f"C:\\Users\\{os.getlogin()}\\PycharmProjects\\MAVIS\\.env\\Scripts\\python.exe"

    # Sicherstellen, dass pip-Befehle den richtigen Python-Pfad verwenden
    if 'pip' in command:
        command = [python_path, "-m", "pip"] + command[1:]

    process = subprocess.Popen(command, shell=shell, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    def read_stream(stream, output_list):
        for line in iter(stream.readline, ''):
            output_list.append(line)
        stream.close()

    stdout_lines = []
    stderr_lines = []
    threading.Thread(target=read_stream, args=(process.stdout, stdout_lines), daemon=True).start()
    threading.Thread(target=read_stream, args=(process.stderr, stderr_lines), daemon=True).start()

    while process.poll() is None or stdout_lines or stderr_lines:
        while stdout_lines:
            print(stdout_lines.pop(0), end='', flush=True)
        while stderr_lines:
            print(stderr_lines.pop(0), end='', flush=True, file=sys.stderr)
        time.sleep(1 / 24)  # 24 FPS Aktualisierung

    # Letzte Zeile sicherstellen
    while stdout_lines:
        print(stdout_lines.pop(0), end='', flush=True)
    while stderr_lines:
        print(stderr_lines.pop(0), end='', flush=True, file=sys.stderr)


def handle_special_commands(user_input):
    commands = {
        "mavis-env-install": "mavis-terminal-3\\install-mavis-3.py",
        "mavis-env-update": "mavis-terminal-3\\install-mavis-3.py",
        "update-mavis": "mavis-terminal-3\\update-repository-windows.py",
        "mavis-security": "mavis-terminal-3\\security-check.py",
        "mavis-info": "mavis-terminal-3\\info.py",
        "run-mavis": "run-mavis-3-all.bat"
    }

    if user_input in commands:
        script_path = f"C:\\Users\\{os.getlogin()}\\PycharmProjects\\MAVIS\\{commands[user_input]}"
        run_command(["python", script_path] if not user_input.endswith(".bat") else [script_path], shell=True)
        return True
    return False


def main():
    print_banner()
    set_python_path()
    default_dir = f"C:\\Users\\{os.getlogin()}\\PycharmProjects\\MAVIS\\"

    while True:
        try:
            # Den aktuellen Arbeitsordner anzeigen
            current_dir = os.getcwd()
            user_input = input(f"{current_dir}> ").strip()  # Eingabeaufforderung zeigt den aktuellen Ordner an

            if user_input.lower() == "exit":
                break
            elif handle_special_commands(user_input):
                continue
            elif user_input.startswith("powershell "):
                run_command(user_input, shell=True)
            else:
                run_command(user_input.split())

            # Sicherstellen, dass alle Ausgaben abgeschlossen sind, bevor die nächste Eingabeaufforderung erscheint
            sys.stdout.flush()
            sys.stderr.flush()

        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print(f"Error: {str(e)}", file=sys.stderr)


if __name__ == "__main__":
    main()
