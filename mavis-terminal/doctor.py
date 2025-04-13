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

"""
Doctor script for MAVIS project
Checks the integrity of the .env file, tests installation of essential tools
(Python, Git, Ollama, FFmpeg, Visual Studio C++ (CL), Rust, WSL, and PowerShell),
and fully scans the project directory.
"""

import os
import subprocess
import sys


def check_file_integrity(file_path):
    """
    Checks whether the specified file exists and is readable.
    Reads a small portion (1 KB) to detect potential read errors.
    """
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                f.read(1024)  # Read 1KB to ensure the file is readable
            return True
        except Exception as e:
            print(f"Error reading '{file_path}': {e}")
            return False
    else:
        print(f"File not found: '{file_path}'")
        return False


def get_command_version(command, args, version_parser=lambda output: output.strip()):
    """
    Runs a command with the given arguments and returns the version.
    Returns None in case of an error.
    """
    try:
        proc = subprocess.run([command] + args, stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE, text=True)
        # Some tools write version info to stderr
        output = proc.stdout if proc.stdout else proc.stderr
        return version_parser(output)
    except Exception as e:
        return None


def check_installation(name, command, args, version_parser=lambda output: output.strip()):
    """
    Checks whether a tool is installed and prints its version.
    """
    print(f"Checking {name}...")
    version = get_command_version(command, args, version_parser)
    if version:
        print(f"  {name} found: {version}")
    else:
        print(f"  {name} NOT found or error retrieving version.")


def scan_directory(root_path):
    """
    Recursively scans the given directory and prints its folder and file structure.
    """
    print(f"Scanning directory: {root_path}")
    for dirpath, dirnames, filenames in os.walk(root_path):
        print(f"\nDirectory: {dirpath}")
        for filename in filenames:
            print(f"  File: {filename}")


def main():
    # Get the current username and build the path
    try:
        username = os.getlogin()
    except Exception:
        username = os.environ.get("USERNAME", "Unknown")

    base_path = f"C:\\Users\\{username}\\PycharmProjects\\MAVIS"
    env_file = os.path.join(base_path, ".env")

    print("=== Doctor Script Started ===\n")

    # 1. Check the .env file
    print("Checking the .env file:")
    if check_file_integrity(env_file):
        print("  .env file is present and readable.\n")
    else:
        print("  Error with the .env file.\n")

    # 2. Check installations and versions
    print("Checking system installations:")

    # Python: Assumes 'python' command works
    check_installation("Python", "python", ["--version"])

    # Git
    check_installation("Git", "git", ["--version"])

    # Ollama
    check_installation("Ollama", "ollama", ["--version"])

    # FFmpeg: Only show the first line (version)
    check_installation("FFmpeg", "ffmpeg", ["-version"], lambda output: output.split('\n')[0])

    # Visual Studio C++:
    # Checks 'cl' – the C/C++ compiler from Visual Studio. Note: environment variables may need to be set.
    check_installation("Visual Studio C++ (CL)", "cl", [],
                       lambda output: output.split('\n')[0] if output else "Unknown version")

    # Rust
    check_installation("Rust (rustc)", "rustc", ["--version"])

    # WSL (Windows Subsystem for Linux)
    check_installation("WSL", "wsl", ["--version"])

    # PowerShell
    def powershell_version_parser(output):
        # Try to extract the line with 'PSVersion'
        for line in output.splitlines():
            if "PSVersion" in line:
                return line.strip()
        return output.strip()

    check_installation("PowerShell", "powershell", ["-Command", "$PSVersionTable.PSVersion"], powershell_version_parser)

    # Note: For "C drivers", it is assumed the Visual Studio C++ compiler (cl) is also used.

    # 3. Scan the project directory
    print("\nScanning the project directory:")
    scan_directory(base_path)

    print("\n=== Doctor Script Finished ===")


if __name__ == "__main__":
    main()
