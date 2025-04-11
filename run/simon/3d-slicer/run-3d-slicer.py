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

# !/usr/bin/env python3
"""
3D Slicer Launcher Script

This professional script checks if the 3D Slicer executable is available
and then launches it. It is assumed that after installation a symbolic link
to 3D Slicer exists (e.g., at /usr/local/bin/slicer).

Usage: Run the script directly:
    python3 launch_3dslicer.py

Author: Your Name
Date: 2025-04-11
License: MIT License
"""

import os
import sys
import shutil
import subprocess


def find_slicer_executable():
    """
    Search for the 3D Slicer executable in the system PATH.
    Returns the path if found, otherwise None.
    """
    slicer_path = shutil.which("slicer")
    return slicer_path


def launch_slicer(slicer_executable):
    """
    Launch 3D Slicer using the given executable path.

    Parameters:
        slicer_executable (str): The full path to the 3D Slicer executable.

    Returns when 3D Slicer terminates.
    """
    print(f"Launching 3D Slicer from: {slicer_executable}")
    try:
        # You can add additional command line arguments to the command list if needed.
        # For example: command = [slicer_executable, "--some-flag", "value"]
        command = [slicer_executable]
        # Running slicer and waiting for it to exit.
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as error:
        print("Error: 3D Slicer did not exit normally.")
        print(f"Details: {error}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("Execution interrupted by the user.")
        sys.exit(0)


def main():
    # Find the Slicer executable
    slicer_executable = find_slicer_executable()
    if not slicer_executable:
        print("Error: 3D Slicer executable not found in your PATH.")
        print("Please ensure that 3D Slicer is installed and that a symbolic link "
              "to the executable (typically 'slicer') exists in /usr/local/bin or your PATH.")
        sys.exit(1)

    # Launch 3D Slicer
    launch_slicer(slicer_executable)


if __name__ == '__main__':
    main()
