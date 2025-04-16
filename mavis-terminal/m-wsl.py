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
WSL Information Tool - Professional PyQt6 Application
-------------------------------------------------------

This program provides comprehensive details regarding the Windows Subsystem for Linux (WSL)
and displays all information in a modern, professional user interface.
It retrieves all available data about WSL, including status, installed Linux distributions,
and the WSL version. The application is implemented using PyQt6 and utilizes a custom stylesheet
for a sleek appearance. External shell commands are executed asynchronously in separate threads
to ensure a smooth and responsive UI.

Features:
    • Displays the current WSL status (using "wsl --status").
    • Lists all installed Linux distributions with detailed information (via "wsl --list --verbose").
    • Additionally shows the WSL version (via "wsl --version").
    • Updates information asynchronously without blocking the user interface.
    • Tabbed interface: Separate tabs for WSL status, distributions, and version.
    • Status bar displaying the last refresh time and error messages.
    • Comprehensive logging to support debugging and maintenance.
    • Modern, non-terminal based appearance.

Prerequisites:
    - Windows 10/11 with WSL installed.
    - The "wsl" command must be available in the system PATH.
    - Python 3.x and PyQt6 installed.
    - For a windowed (non-console) experience, the application can be run as a .pyw file or packaged as a Windows executable using PyInstaller (--noconsole).

Usage:
    Run this script directly to launch the modern WSL information interface.
"""

import sys
import subprocess
import logging
import os
from datetime import datetime

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QTextEdit, QPushButton, QLabel, QTabWidget, QMessageBox, QStatusBar
)
from PyQt6.QtCore import Qt, QRunnable, QThreadPool, pyqtSignal, QObject

# Configure logging for debugging purposes
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Custom Qt StyleSheet for a modern, professional look
# Using 'Segoe UI' to avoid missing glyph issues.
STYLE_SHEET = """
QWidget {
    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #1b2631, stop:1 #0f1626);
    color: #FFFFFF;
    font-family: 'Segoe UI', sans-serif;
    font-size: 14px;
}
QLineEdit {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #2c3e50, stop:1 #1c2833);
    border: 1px solid #778899;
    border-radius: 5px;
    padding: 5px;
    color: #FFFFFF;
}
QPushButton {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #2c3e50, stop:1 #1c2833);
    border: none;
    border-radius: 5px;
    padding: 5px 10px;
    color: #FFFFFF;
}
QPushButton:hover {
    background-color: #1c2833;
}
QTabWidget::pane {
    border: 1px solid #778899;
    border-radius: 8px;
}
QTabBar::tab {
    background: transparent;
    padding: 8px;
    margin: 2px;
    border-top-left-radius: 6px;
    border-top-right-radius: 6px;
}
QTabBar::tab:selected {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #34495e, stop:1 #1c2833);
    color: #FFFFFF;
}
QTextEdit {
    background-color: transparent;
    border: 1px solid #778899;
    border-radius: 8px;
    font-family: 'Courier New', monospace;
    font-size: 12px;
    padding: 8px;
}
QLabel {
    font-size: 16px;
    padding: 4px;
}
QStatusBar {
    background-color: #1b2631;
    color: #FFFFFF;
}
"""

def run_command(cmd: list[str]) -> tuple[str, str]:
    """
    Executes a system command and returns the stdout and stderr outputs.

    Args:
        cmd (list[str]): Command and arguments as a list.

    Returns:
        tuple[str, str]: (stdout, stderr). On error, stderr contains the error message.
    """
    try:
        logger.info("Executing command: %s", " ".join(cmd))
        result = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        return result.stdout.strip(), ""
    except subprocess.CalledProcessError as e:
        error_msg = f"Error executing {' '.join(cmd)}: {e.stderr.strip()}"
        logger.error(error_msg)
        return "", error_msg
    except FileNotFoundError:
        error_msg = f"Command not found: {cmd[0]}"
        logger.error(error_msg)
        return "", error_msg

def get_wsl_status() -> str:
    """
    Retrieves the current WSL status using 'wsl --status'.

    Returns:
        str: Command output or error message.
    """
    status, error = run_command(["wsl", "--status"])
    if error:
        return f"Error retrieving WSL status:\n{error}"
    return status

def get_installed_distros() -> str:
    """
    Retrieves the installed WSL distributions with detailed information.

    Returns:
        str: Command output or error message.
    """
    distros, error = run_command(["wsl", "--list", "--verbose"])
    if error:
        return f"Error retrieving installed distributions:\n{error}"
    return distros

def get_wsl_version() -> str:
    """
    Retrieves the WSL version using 'wsl --version'.

    Returns:
        str: Command output or error message.
    """
    version, error = run_command(["wsl", "--version"])
    if error:
        return f"Error retrieving WSL version:\n{error}"
    return version

class WorkerSignals(QObject):
    """
    Defines signals for a worker thread.
    """
    finished = pyqtSignal(str)  # Emitted when execution is complete with the result
    error = pyqtSignal(str)     # Emitted when an error occurs

class Worker(QRunnable):
    """
    Worker thread for executing a function asynchronously.
    """
    def __init__(self, fn, *args, **kwargs):
        super().__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

    def run(self) -> None:
        """
        Executes the function with the provided arguments.
        """
        try:
            result = self.fn(*self.args, **self.kwargs)
            self.signals.finished.emit(result)
        except Exception as e:
            err = f"Unexpected error: {str(e)}"
            logger.exception(err)
            self.signals.error.emit(err)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MAVIS WSL Information")
        self.resize(900, 700)
        self.threadpool = QThreadPool()
        logger.info("Multithreading with maximum %d threads", self.threadpool.maxThreadCount())
        self.init_ui()

        # Example paths: Set application icon from a designated directory.
        user = os.getenv("USERNAME") or os.getenv("USER")
        self.repo_path = f"C:/Users/{user}/PycharmProjects/MAVIS"
        icon_path = f"C:/Users/{user}/PycharmProjects/MAVIS/icons/mavis-logo.ico"
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))

    def init_ui(self):
        # Main widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # Header label
        header = QLabel("MAVIS WSL and Linux Distribution Information")
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(header)

        # Tabbed interface: WSL Status, Distributions, and WSL Version
        self.tabs = QTabWidget()
        self.tab_status = QWidget()
        self.tab_distros = QWidget()
        self.tab_version = QWidget()

        # Layout for WSL Status tab
        status_layout = QVBoxLayout()
        self.text_status = QTextEdit()
        self.text_status.setReadOnly(True)
        status_layout.addWidget(self.text_status)
        self.tab_status.setLayout(status_layout)

        # Layout for Distributions tab
        distros_layout = QVBoxLayout()
        self.text_distros = QTextEdit()
        self.text_distros.setReadOnly(True)
        distros_layout.addWidget(self.text_distros)
        self.tab_distros.setLayout(distros_layout)

        # Layout for WSL Version tab
        version_layout = QVBoxLayout()
        self.text_version = QTextEdit()
        self.text_version.setReadOnly(True)
        version_layout.addWidget(self.text_version)
        self.tab_version.setLayout(version_layout)

        # Add tabs to the widget
        self.tabs.addTab(self.tab_status, "WSL Status")
        self.tabs.addTab(self.tab_distros, "Distributions")
        self.tabs.addTab(self.tab_version, "WSL Version")
        main_layout.addWidget(self.tabs)

        # Refresh button with centered layout
        button_layout = QHBoxLayout()
        self.btn_refresh = QPushButton("Refresh Information")
        self.btn_refresh.clicked.connect(self.update_info)
        button_layout.addStretch(1)
        button_layout.addWidget(self.btn_refresh)
        button_layout.addStretch(1)
        main_layout.addLayout(button_layout)

        # Status bar for displaying last update time and errors
        self.statusbar = QStatusBar()
        self.setStatusBar(self.statusbar)

        # Initial update
        self.update_info()

    def update_info(self):
        """
        Updates all displayed information (WSL Status, Distributions, WSL Version)
        asynchronously and shows the current timestamp in the status bar.
        """
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.statusbar.showMessage(f"Refreshing information (Timestamp: {current_time})...")

        # Worker for WSL status
        status_worker = Worker(get_wsl_status)
        status_worker.signals.finished.connect(self.handle_status_result)
        status_worker.signals.error.connect(lambda err: self.handle_error("WSL Status", err))
        self.threadpool.start(status_worker)

        # Worker for installed distributions
        distros_worker = Worker(get_installed_distros)
        distros_worker.signals.finished.connect(self.handle_distros_result)
        distros_worker.signals.error.connect(lambda err: self.handle_error("Distributions", err))
        self.threadpool.start(distros_worker)

        # Worker for WSL version
        version_worker = Worker(get_wsl_version)
        version_worker.signals.finished.connect(self.handle_version_result)
        version_worker.signals.error.connect(lambda err: self.handle_error("WSL Version", err))
        self.threadpool.start(version_worker)

    def handle_status_result(self, result: str):
        self.text_status.setPlainText(result)
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.statusbar.showMessage(f"Last updated: {current_time}", 5000)
        logger.info("WSL Status updated successfully.")

    def handle_distros_result(self, result: str):
        self.text_distros.setPlainText(result)
        logger.info("Distributions updated successfully.")

    def handle_version_result(self, result: str):
        self.text_version.setPlainText(result)
        logger.info("WSL Version updated successfully.")

    def handle_error(self, source: str, error_msg: str):
        self.statusbar.showMessage(f"Error updating {source}.", 5000)
        logger.error("Error updating %s: %s", source, error_msg)
        QMessageBox.critical(self, f"{source} Update Error",
                             f"An error occurred while updating {source}:\n{error_msg}",
                             QMessageBox.StandardButton.Ok)

def main():
    """
    Initializes the application and starts the PyQt6 event loop.
    """
    app = QApplication(sys.argv)
    app.setStyleSheet(STYLE_SHEET)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
