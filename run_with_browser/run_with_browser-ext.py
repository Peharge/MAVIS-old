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

import subprocess
import webbrowser
import os
import platform
import logging
from datetime import datetime

# Configuration
URL = "http://127.0.0.1:5000/"
EDGE_PATHS = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"
]

# Console color definitions
red = "\033[91m"
green = "\033[92m"
yellow = "\033[93m"
blue = "\033[94m"
reset = "\033[0m"
bold = "\033[1m"

# Logging setup
logging.basicConfig(filename="client_log.txt", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

# Enable ANSI support for Windows
if os.name == "nt":
    os.system("")

# Helper functions
def log_and_print(message, level="info"):
    """Logs and prints the message."""
    colors = {"info": blue, "success": green, "warning": yellow, "error": red}
    print(f"{colors.get(level, reset)}{message}{reset}")
    if level == "error":
        logging.error(message)
    elif level == "warning":
        logging.warning(message)
    else:
        logging.info(message)

def find_edge():
    """Searches for Edge installations."""
    for path in EDGE_PATHS:
        if os.path.exists(path):
            return path
    return None

def open_edge(url):
    """Tries to open Edge."""
    edge_path = find_edge()
    if edge_path:
        try:
            # Open Edge in app mode
            subprocess.Popen([edge_path, "--app=" + url])
            log_and_print("Microsoft Edge has been successfully opened.", "success")
            return True
        except (subprocess.SubprocessError, PermissionError) as e:
            log_and_print(f"Error opening Edge: {e}", "error")
    else:
        log_and_print("Microsoft Edge not found.", "warning")
    return False

def open_default_browser(url):
    """Opens the URL in the default browser."""
    try:
        webbrowser.open(url, new=2)  # new=2 opens in a new tab/window
        log_and_print(f"Default browser has been opened: {url}", "success")
    except webbrowser.Error as e:
        log_and_print(f"Error opening default browser: {e}", "error")

# Main logic
def main():
    log_and_print("\nClient Information:", "info")
    log_and_print("----------------------", "info")

    username = os.getenv('USERNAME') or os.getenv('USER') or "Unknown User"

    log_and_print(f"Username: {username}", "info")

    # Open Edge or default browser
    if not open_edge(URL):
        log_and_print("Edge not available. Using default browser...", "warning")
        open_default_browser(URL)

    log_and_print(f"Flask server is running at: {URL}", "info")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        log_and_print(f"Unexpected error: {e}", "error")
