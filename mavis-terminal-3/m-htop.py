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
import psutil
import time
import os
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem, QProgressBar, \
    QHeaderView, QScrollArea
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QFont, QIcon


class SystemMonitor(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Advanced System Monitor")
        self.setGeometry(100, 100, 800, 500)
        self.setStyleSheet("background-color: black; color: white;")

        # Set application icon dynamically
        user = os.getenv("USERNAME") or os.getenv("USER")
        icon_path = f"C:/Users/{user}/PycharmProjects/MAVIS/icons/mavis-logo.ico"
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))

        main_layout = QVBoxLayout()

        # CPU Progress Bar
        self.cpu_label = QLabel("CPU Usage: 0%")
        self.cpu_label.setFont(QFont("Arial", 14))
        self.cpu_label.setStyleSheet("color: #94bfff;")
        self.cpu_progress = QProgressBar()
        self.cpu_progress.setStyleSheet(
            "QProgressBar { background-color: #222; color: white; } QProgressBar::chunk { background-color: #94bfff; }")
        main_layout.addWidget(self.cpu_label)
        main_layout.addWidget(self.cpu_progress)

        # Memory Usage
        self.memory_label = QLabel("Memory Usage: 0GB / 0GB")
        self.memory_label.setFont(QFont("Arial", 14))
        self.memory_label.setStyleSheet("color: white;")
        self.memory_progress = QProgressBar()
        self.memory_progress.setStyleSheet(
            "QProgressBar { background-color: #222; color: white; } QProgressBar::chunk { background-color: #94bfff; }")
        main_layout.addWidget(self.memory_label)
        main_layout.addWidget(self.memory_progress)

        # Disk Usage
        self.disk_label = QLabel("Disk Usage: 0GB / 0GB")
        self.disk_label.setFont(QFont("Arial", 14))
        self.disk_label.setStyleSheet("color: #94bfff;")
        self.disk_progress = QProgressBar()
        self.disk_progress.setStyleSheet(
            "QProgressBar { background-color: #222; color: white; } QProgressBar::chunk { background-color: #ffcc00; }")
        main_layout.addWidget(self.disk_label)
        main_layout.addWidget(self.disk_progress)

        # Network Usage
        self.network_label = QLabel("Network: Sent 0MB / Received 0MB")
        self.network_label.setFont(QFont("Arial", 14))
        self.network_label.setStyleSheet("color: white;")
        main_layout.addWidget(self.network_label)

        # Process Table with Scrollbar
        self.process_table = QTableWidget()
        self.process_table.setColumnCount(4)
        self.process_table.setHorizontalHeaderLabels(["PID", "Name", "CPU %", "Mem %"])
        self.process_table.setStyleSheet("color: white; background-color: #222;")
        self.process_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        # Adding Scroll Area
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.process_table)
        self.scroll_area.setStyleSheet("""
            QScrollArea {
                border: none;
                background-color: none;
            }
            
            QScrollBar:vertical {
                background-color: none;
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
                background: none;
            }
            
            QScrollBar::up-arrow:vertical,
            QScrollBar::down-arrow:vertical {
                background: none;
            }
            
            QScrollBar::add-page:vertical,
            QScrollBar::sub-page:vertical {
                background: none;
            }
            
            QScrollBar::add-line:horizontal,
            QScrollBar::sub-line:horizontal {
                background: none;
            }
            
            QScrollBar::left-arrow:horizontal,
            QScrollBar::right-arrow:horizontal {
                background: none;
            }
            
            QScrollBar::add-page:horizontal,
            QScrollBar::sub-page:horizontal {
                background: none;
            }
        """)
        main_layout.addWidget(self.scroll_area)

        self.setLayout(main_layout)

        # Timer for updates
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_metrics)
        self.timer.start(1000)  # Update every second

    def update_metrics(self):
        # Update CPU Usage
        cpu_usage = psutil.cpu_percent()
        self.cpu_label.setText(f"CPU Usage: {cpu_usage}%")
        self.cpu_progress.setValue(int(cpu_usage))

        # Update Memory Usage
        mem = psutil.virtual_memory()
        mem_percent = int(mem.percent)
        self.memory_label.setText(
            f"Memory Usage: {mem.used / 1024 ** 3:.2f}GB / {mem.total / 1024 ** 3:.2f}GB ({mem_percent}%)")
        self.memory_progress.setValue(mem_percent)

        # Update Disk Usage
        disk = psutil.disk_usage('/')
        disk_percent = int(disk.percent)
        self.disk_label.setText(
            f"Disk Usage: {disk.used / 1024 ** 3:.2f}GB / {disk.total / 1024 ** 3:.2f}GB ({disk_percent}%)")
        self.disk_progress.setValue(disk_percent)

        # Update Network Usage
        net = psutil.net_io_counters()
        self.network_label.setText(
            f"Network: Sent {net.bytes_sent / 1024 ** 2:.2f}MB / Received {net.bytes_recv / 1024 ** 2:.2f}MB")

        # Update Process Table
        processes = sorted(psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']),
                           key=lambda p: p.info['cpu_percent'], reverse=True)[:20]
        self.process_table.setRowCount(len(processes))
        for row, proc in enumerate(processes):
            self.process_table.setItem(row, 0, QTableWidgetItem(str(proc.info['pid'])))
            self.process_table.setItem(row, 1, QTableWidgetItem(proc.info['name']))
            self.process_table.setItem(row, 2, QTableWidgetItem(f"{proc.info['cpu_percent']}%"))
            self.process_table.setItem(row, 3, QTableWidgetItem(f"{proc.info['memory_percent']:.2f}%"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SystemMonitor()
    window.show()
    sys.exit(app.exec())
