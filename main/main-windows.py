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

# Version-Details
version_details = {
    "mavis-1-2-main": f"With {red}Xc++ 2 11B{reset} or {green}Llama3.2 11B{reset} +16GB RAM +23GB storage (Works with one CPU) {blue}22B{reset}",
    "mavis-1-2-math": f"With {red}Xc++ 2 11B{reset} or {green}Llama3.2 11B{reset} + {green}Qwen 2.5 14B{reset} +16GB RAM +23GB storage (Works with one CPU) {blue}27B{reset}",
    "mavis-1-2-code": f"With {red}Xc++ 2 11B{reset} or {green}Llama3.2 11B{reset} + {green}Qwen 2.5 Coder 14B{reset} +16GB RAM +23GB storage (Works with one CPU) {blue}27B{reset}",
    "mavis-1-2-math-pro": f"With {red}Xc++ 2 90B{reset} or {green}Llama3.2 90B{reset} + {green}QwQ{reset} +64GB RAM +53GB storage (Works with one CPU) {blue}122B{reset}",
    "mavis-1-2-code-pro": f"With {red}Xc++ 2 90B{reset} or {green}Llama3.2 90B{reset} + {green}Qwen 2.5 Coder 32B{reset} +64GB RAM +53GB storage (Works with one CPU) {blue}122B{reset}",
    "mavis-1-2-mini": f"With {red}Xc++ 2 11B{reset} or {green}Llama3.2 11B{reset} + {green}Qwen 2.5 0.5B{reset} +16GB RAM +13GB storage (Works with one CPU) {blue}11.5B{reset}",
    "mavis-1-2-mini-mini": f"With {red}Xc++ 2 11B{reset} or {green}Llama3.2 11B{reset} + {green}smollm:135m{reset} +16GB RAM +33GB storage (Works with one CPU) {blue}11.0135B{reset}",
    "mavis-1-2-3-main": f"With {red}Xc++ 2 11B{reset} or {green}Llama3.2 11B{reset} + {green}Phi4{reset} +16GB RAM +23GB storage (Works with one CPU) {blue}27B{reset}",
    "mavis-1-3-main": f"With {red}Xc++ 2 11B{reset} or {green}Qwen2 VL 7B{reset} + {green}Llama 3.3{reset} +64GB RAM +53GB storage (Works with one CPU) {blue}77B{reset}",
    "mavis-1-3-math": f"With {red}Xc++ 2 11B{reset} or {green}Qwen2 VL 7B{reset} + {green}Qwen 2.5 14B{reset} +16GB RAM +33GB storage (Works with one CPU) {blue}21B{reset}",
    "mavis-1-3-code": f"With {red}Xc++ 2 11B{reset} or {green}Qwen2 VL 7B{reset} + {green}Qwen 2.5 Coder{reset} 14B +16B RAM +33GB storage (Works with one CPU) {blue}21B{reset}",
    "mavis-1-3-math-pro": f"With {red}Xc++ 2 90B{reset} or {green}Qwen2 VL 72B{reset} + {green}Qwen 2.5 Coder{reset} 32B +64GB RAM +53GB storage (Works with one CPU) {blue}104B{reset}",
    "mavis-1-4-math": f"With {red}Xc++ 2 90B{reset} or {green}QvQ{reset} + {green}QwQ{reset} +64GB RAM +53GB storage (Works with one CPU) {blue}104B{reset}",
}

def run_batch_file(batch_name: str) -> None:
    """
    Führt die Batch-Datei aus, indem der vollständige Dateiname zusammengebaut wird.
    """
    file_name = os.path.join(
        os.path.expanduser("~"),
        "PycharmProjects",
        "MAVIS",
        f"run-{batch_name}.bat"
    )
    try:
        result = subprocess.run(file_name, shell=True, check=True, text=True, capture_output=True)
        print(f"{green}The batch file '{file_name}' was executed successfully.{reset}\n")
        print(f"Output:\n{result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"{red}Error executing file '{file_name}':{reset}\n{e.stderr}")
    except Exception as e:
        print(f"{red}Unexpected error occurred:{reset} {e}\n")

def display_versions() -> dict:
    """
    Zeigt alle Versionen und zugehörigen Batch-Dateien ohne 'run-' und '.bat'.
    """
    print(f"All MAVIS versions are available here:\n")

    grouped_versions = {}
    for batch_name, details in version_details.items():
        version = details.split("With")[0].strip()  # Gruppiere nach Hauptversion
        if version not in grouped_versions:
            grouped_versions[version] = []
        grouped_versions[version].append(batch_name)

    for i, (version, batch_files) in enumerate(grouped_versions.items(), 1):
        print(f"{i}. {version}")
        for j, batch_file in enumerate(batch_files, 1):
            print(f"   {j}. {batch_file}")
        print()

    return version_details

def show_version_details(batch_name: str) -> None:
    """
    Zeigt Details zu einer bestimmten Version an.
    """
    if batch_name in version_details:
        print(f"Details for {blue}{batch_name}:{reset}\n")
        print(f"{version_details[batch_name]}\n")
    else:
        print(f"{red}No details found for {reset}{blue}{batch_name}{reset}{red}.{reset}\n")

def get_user_input(versions: dict) -> None:
    """
    Fragt den Benutzer nach der gewünschten Aktion.
    """
    while True:
        print("\nOptions:")
        print("1. Run a MAVIS batch file")
        print("2. Show details of a MAVIS version")
        print("3. Exit")

        choice = input(f"Enter your choice (1/2/3): ").strip()

        if choice == "1":
            user_input = input(f"Enter a MAVIS batch file name: ").strip()
            if user_input in versions:
                run_batch_file(user_input)
            else:
                print(f"{red}Invalid batch file name. Please try again.{reset}\n")

        elif choice == "2":
            user_input = input(f"Enter a MAVIS batch file name to view details: ").strip()
            show_version_details(user_input)

        elif choice == "3":
            print(f"{green}Goodbye!{reset}")
            break

        else:
            print(f"{red}Invalid choice. Please select 1, 2, or 3.{reset}\n")

if __name__ == "__main__":
    versions = display_versions()
    get_user_input(versions)
