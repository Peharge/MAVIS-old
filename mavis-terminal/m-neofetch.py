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
import os
import platform
import cpuinfo
import psutil
import shutil
import time
import socket
import subprocess
import pip

from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtGui import QIcon


def format_bytes(byte_value: int) -> float:
    """Helper function to convert bytes to gigabytes."""
    return round(byte_value / (1024 ** 3), 2)


def get_system_info() -> dict:
    """Collects and returns all relevant system information."""
    system_info = {}

    try:
        # OS Information
        system_info['Operating System'] = f"{platform.system()} {platform.release()} ({platform.version()})"
        system_info['Architecture'] = platform.architecture()[0]

        # CPU Information
        cpu_info = cpuinfo.get_cpu_info()
        system_info['CPU Model'] = cpu_info.get("brand_raw", "N/A")
        system_info['CPU Architecture'] = cpu_info.get("arch", "N/A")
        system_info['Cores'] = psutil.cpu_count(logical=False)
        system_info['Threads'] = psutil.cpu_count(logical=True)
        cpu_freq = psutil.cpu_freq()
        system_info['Max Frequency'] = f"{cpu_freq.max if cpu_freq else 'N/A'} MHz"

        # RAM Information
        ram = psutil.virtual_memory()
        system_info['Total RAM'] = f"{format_bytes(ram.total)} GB"
        system_info['Used RAM'] = f"{format_bytes(ram.used)} GB"
        system_info['Free RAM'] = f"{format_bytes(ram.available)} GB"
        system_info['RAM Usage'] = f"{ram.percent}%"

        # Swap Information
        swap = psutil.swap_memory()
        system_info['Total Swap'] = f"{format_bytes(swap.total)} GB"
        system_info['Used Swap'] = f"{format_bytes(swap.used)} GB"
        system_info['Free Swap'] = f"{format_bytes(swap.free)} GB"

        # Disk Information
        total_storage, used_storage, free_storage = shutil.disk_usage("/")
        system_info['Total Storage'] = f"{format_bytes(total_storage)} GB"
        system_info['Used Storage'] = f"{format_bytes(used_storage)} GB"
        system_info['Free Storage'] = f"{format_bytes(free_storage)} GB"

        # Network Information
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        system_info['Hostname'] = hostname
        system_info['IP Address'] = ip_address

        # CPU Usage / Load Average
        if platform.system() == "Windows":
            system_info['CPU Usage'] = f"{psutil.cpu_percent(interval=1)}%"
        else:
            try:
                load_avg = os.getloadavg()
                system_info['Load Average'] = f"1m: {load_avg[0]}, 5m: {load_avg[1]}, 15m: {load_avg[2]}"
            except OSError:
                system_info['Load Average'] = "Not available"

        # System Uptime
        uptime_seconds = time.time() - psutil.boot_time()
        system_info['Uptime'] = time.strftime("%H:%M:%S", time.gmtime(uptime_seconds))

        # User Information
        user_info = psutil.users()
        users = [f"{user.name} (Terminal: {user.terminal or 'N/A'}, started: {time.ctime(user.started)})"
                 for user in user_info]
        system_info['Users'] = ", ".join(users)

        # Additional Information
        system_info['PIP Version'] = pip.__version__
        system_info['PowerShell Version'] = get_powershell_version()
        system_info['WSL Version'] = get_wsl_version()
        system_info['Kernel Version'] = get_kernel_version()
        system_info['WSLg Version'] = get_wslg_version()
        system_info['MSRDC Version'] = get_msrpc_version()
        system_info['Direct3D Version'] = get_direct3d_version()
        system_info['DXCore Version'] = get_dxcore_version()

    except Exception as e:
        system_info['Error'] = f"Error retrieving system information: {e}"

    return system_info


def get_powershell_version():
    try:
        result = subprocess.run(
            ["powershell", "-Command", "$PSVersionTable.PSVersion.ToString()"],
            capture_output=True, text=True, check=True
        )
        return result.stdout.strip()
    except Exception:
        return "Not available"


def get_wsl_version():
    try:
        result = subprocess.run(
            ["wsl", "--version"],
            capture_output=True, text=True, check=True
        )
        return result.stdout.strip().split("\n")[0]
    except Exception:
        return "Not available"


def get_kernel_version():
    try:
        result = subprocess.run(
            ["wsl", "uname", "-r"],
            capture_output=True, text=True, check=True
        )
        return result.stdout.strip()
    except Exception:
        return "Not available"


def get_wslg_version():
    try:
        result = subprocess.run(
            ["wsl", "--version"],
            capture_output=True, text=True, check=True
        )
        # Assumption: WSLg version is in the 5th line
        return result.stdout.strip().split("\n")[4]
    except Exception:
        return "Not available"


def get_msrpc_version():
    try:
        result = subprocess.run(
            ["wsl", "--version"],
            capture_output=True, text=True, check=True
        )
        # Assumption: MSRDC version is in the 7th line
        return result.stdout.strip().split("\n")[6]
    except Exception:
        return "Not available"


def get_direct3d_version():
    try:
        result = subprocess.run(
            ["wsl", "--version"],
            capture_output=True, text=True, check=True
        )
        # Assumption: Direct3D version is in the 9th line
        return result.stdout.strip().split("\n")[8]
    except Exception:
        return "Not available"


def get_dxcore_version():
    try:
        result = subprocess.run(
            ["wsl", "--version"],
            capture_output=True, text=True, check=True
        )
        # Assumption: DXCore version is in the 11th line
        return result.stdout.strip().split("\n")[10]
    except Exception:
        return "Not available"


class NeofetchWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MAVIS Neofetch")
        self.resize(900, 600)
        self.init_ui()
        # Use a timer to update the info every 5 seconds in the main thread,
        # since retrieving system information should be fast enough.
        self.update_timer = QtCore.QTimer(self)
        self.update_timer.timeout.connect(self.update_system_info)
        self.update_timer.start(5000)

    def init_ui(self):
        splitter = QtWidgets.QSplitter(QtCore.Qt.Orientation.Horizontal)
        self.setCentralWidget(splitter)

        user = os.getenv("USERNAME") or os.getenv("USER")
        icon_path = f"C:/Users/{user}/PycharmProjects/MAVIS/icons/mavis-logo.ico"
        self.setWindowIcon(QIcon(icon_path))

        # Left side: Display image
        self.image_label = QtWidgets.QLabel()
        self.image_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        image_path = os.path.join("C:\\", "Users", os.getlogin(), "PycharmProjects", "MAVIS", "icons", "mavis-logo-3d.ico")
        pixmap = QtGui.QPixmap(image_path)
        if pixmap.isNull():
            self.image_label.setText("No image found.\nPlease provide the image at\n'img_1.png'.")
        else:
            self.image_label.setPixmap(pixmap.scaled(400, 600,
                                                     QtCore.Qt.AspectRatioMode.KeepAspectRatio,
                                                     QtCore.Qt.TransformationMode.SmoothTransformation))
        splitter.addWidget(self.image_label)

        # Right side: System information as formatted HTML
        self.info_text = QtWidgets.QTextEdit()
        self.info_text.setReadOnly(True)
        font = QtGui.QFont("Courier New", 10)
        self.info_text.setFont(font)
        splitter.addWidget(self.info_text)

        # Initial update
        self.update_system_info()

    def update_system_info(self):
        info = get_system_info()
        html = """
        <html>
            <head>
                <style>
                    body { font-family: 'Courier New', monospace; font-size: 10pt; }
                    table { border-collapse: collapse; width: 100%; }
                    th, td { text-align: left; padding: 8px; border-bottom: 1px solid #ddd; }
                    th { background-color: #2c3e50; color: #ffffff; }
                    tr:nth-child(even) { background-color: rgba(255, 255, 255, 0.1); }
                </style>
            </head>
            <body>
                <h2 style="color:#ffffff;">System Information</h2>
                <table>
        """
        for key, value in info.items():
            html += f"<tr><th>{key}</th><td>{value}</td></tr>"
        html += """
                </table>
            </body>
        </html>
        """
        self.info_text.setHtml(html)


def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet("""
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

        QLabel#HeaderLabel {
            font-size: 18px;
            font-weight: bold;
            padding: 8px;
        }

        QPlainTextEdit {
            background-color: transparent;
            font-family: 'Consolas', monospace;
            color: #ffffff;
            border: none;
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

        QStatusBar {
            background: #1b2631;
            padding: 4px;
        }

        QScrollArea {
            border: none;
            background-color: transparent;
        }

        QScrollBar:vertical {
            background-color: transparent;
            width: 10px;
            border-radius: 5px;
        }

        QScrollBar::handle:vertical {
            background-color: #ffffff;
            min-height: 20px;
            border-radius: 5px;
        }

        QScrollBar::add-line:vertical,
        QScrollBar::sub-line:vertical {
            background: transparent;
        }

        QScrollBar::up-arrow:vertical,
        QScrollBar::down-arrow:vertical {
            background: transparent;
        }

        QScrollBar::add-page:vertical,
        QScrollBar::sub-page:vertical {
            background: transparent;
        }

        QScrollBar:horizontal {
            background-color: transparent;
            height: 10px;
            border-radius: 5px;
        }

        QScrollBar::handle:horizontal {
            background-color: #ffffff;
            min-width: 20px;
            border-radius: 5px;
        }

        QScrollBar::add-line:horizontal,
        QScrollBar::sub-line:horizontal {
            background: transparent;
        }

        QScrollBar::left-arrow:horizontal,
        QScrollBar::right-arrow:horizontal {
            background: transparent;
        }

        QScrollBar::add-page:horizontal,
        QScrollBar::sub-page:horizontal {
            background: transparent;
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
    """)
    window = NeofetchWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
