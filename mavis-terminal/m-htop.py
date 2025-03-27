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
import os
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QFrame, QLabel, QProgressBar,
    QTableWidget, QTableWidgetItem, QHeaderView, QScrollArea, QLineEdit, QPushButton, QMenu, QMessageBox
)
from PyQt6.QtCore import QTimer, Qt, QPoint
from PyQt6.QtGui import QFont, QIcon

class AdvancedSystemMonitor(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Advanced System Monitor")
        self.setGeometry(100, 100, 1000, 600)
        self.setStyleSheet(self.get_stylesheet())

        # Dynamically set the application icon
        user = os.getenv("USERNAME") or os.getenv("USER")
        icon_path = f"C:/Users/{user}/PycharmProjects/MAVIS/icons/mavis-logo.ico"
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))

        # Main layout
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(15, 15, 15, 15)
        main_layout.setSpacing(10)

        # Upper metrics in separate "cards"
        metrics_layout = QHBoxLayout()
        metrics_layout.setSpacing(20)
        self.cpu_card = self.create_metric_card("CPU Usage", "#94bfff")
        self.mem_card = self.create_metric_card("Memory Usage", "#94bfff")
        self.disk_card = self.create_metric_card("Disk Usage", "#ffcc00")
        self.net_card = self.create_metric_card("Network", "#7ed321")
        metrics_layout.addWidget(self.cpu_card)
        metrics_layout.addWidget(self.mem_card)
        metrics_layout.addWidget(self.disk_card)
        metrics_layout.addWidget(self.net_card)
        main_layout.addLayout(metrics_layout)

        # Process filter bar
        filter_layout = QHBoxLayout()
        self.filter_input = QLineEdit()
        self.filter_input.setPlaceholderText("Filter process name...")
        self.filter_input.textChanged.connect(self.filter_processes)
        refresh_button = QPushButton("Refresh")
        refresh_button.clicked.connect(self.update_metrics)
        filter_layout.addWidget(self.filter_input)
        filter_layout.addWidget(refresh_button)
        main_layout.addLayout(filter_layout)

        # Process table with scroll area
        self.process_table = QTableWidget()
        self.process_table.setColumnCount(4)
        self.process_table.setHorizontalHeaderLabels(["PID", "Name", "CPU %", "Mem %"])
        self.process_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.process_table.setSortingEnabled(True)
        self.process_table.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.process_table.customContextMenuRequested.connect(self.process_table_menu)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.process_table)
        main_layout.addWidget(scroll_area)

        self.setLayout(main_layout)

        # Timer for updates (every second)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_metrics)
        self.timer.start(1000)

        self.all_processes = []  # for filtering

    def get_stylesheet(self):
        # Complete stylesheet with modern dark mode design
        return """
        QWidget {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #1b2631, stop:1 #0f1626);
            color: #ecf0f1;
            font-family: Arial;
        }
        QFrame.metricCard {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #2c3e50, stop:1 #1c2833);
            border: 1px solid #566573;
            border-radius: 12px;
            padding: 10px;
        }
        QFrame.metricCard:hover {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #34495e, stop:1 #1c2833);
            border: 1px solid #778899;
        }
        QLabel.title {
            font-size: 16px;
            font-weight: bold;
            background: none;
        }
        QProgressBar {
            background-color: #222;
            border: none;
            height: 20px;
            border-radius: 10px;
        }
        QProgressBar::chunk {
            border-radius: 10px;
        }
        QLineEdit {
            background-color: #222;
            border: 1px solid #566573;
            border-radius: 5px;
            padding: 5px;
            color: #ecf0f1;
        }
        QPushButton {
            background-color: #34495e;
            border: 1px solid #566573;
            border-radius: 5px;
            padding: 5px 10px;
            color: #ecf0f1;
        }
        QPushButton:hover {
            background-color: #3c5977;
        }
        QTableWidget {
            background-color: #222;
            gridline-color: #566573;
        }
        QHeaderView::section {
            background-color: #2c3e50;
            padding: 4px;
            border: 1px solid #566573;
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
        """

    def create_metric_card(self, title, color):
        # Creates a QFrame containing a metric (label + progress bar)
        card = QFrame()
        card.setObjectName("metricCard")
        card.setProperty("class", "metricCard")
        layout = QVBoxLayout()
        layout.setSpacing(5)

        label = QLabel(title + ":")
        label.setObjectName("title")
        label.setProperty("class", "title")
        layout.addWidget(label)

        progress = QProgressBar()
        progress.setStyleSheet(f"QProgressBar::chunk {{ background-color: {color}; }}")
        layout.addWidget(progress)

        # Additional detail label for numeric values
        detail = QLabel("0")
        layout.addWidget(detail)

        card.setLayout(layout)
        # Save references based on the title
        if title.startswith("CPU"):
            self.cpu_progress = progress
            self.cpu_detail = detail
        elif title.startswith("Memory"):
            self.mem_progress = progress
            self.mem_detail = detail
        elif title.startswith("Disk"):
            self.disk_progress = progress
            self.disk_detail = detail
        elif title.startswith("Network"):
            self.net_detail = detail

        return card

    def update_metrics(self):
        # CPU
        cpu_usage = psutil.cpu_percent()
        self.cpu_progress.setValue(int(cpu_usage))
        self.cpu_detail.setText(f"{cpu_usage:.1f}%")

        # Memory
        mem = psutil.virtual_memory()
        mem_percent = mem.percent
        used_mem = mem.used / 1024**3
        total_mem = mem.total / 1024**3
        self.mem_progress.setValue(int(mem_percent))
        self.mem_detail.setText(f"{used_mem:.2f}GB / {total_mem:.2f}GB ({mem_percent}%)")

        # Disk
        disk = psutil.disk_usage('/')
        disk_percent = disk.percent
        used_disk = disk.used / 1024**3
        total_disk = disk.total / 1024**3
        self.disk_progress.setValue(int(disk_percent))
        self.disk_detail.setText(f"{used_disk:.2f}GB / {total_disk:.2f}GB ({disk_percent}%)")

        # Network
        net = psutil.net_io_counters()
        self.net_detail.setText(f"Sent {net.bytes_sent/1024**2:.2f}MB / Recv {net.bytes_recv/1024**2:.2f}MB")

        # Update processes
        self.all_processes = list(psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']))
        self.populate_process_table(self.all_processes)

    def populate_process_table(self, process_list):
        # Display the top 20 processes (by CPU usage) in the table
        process_list = sorted(process_list, key=lambda p: p.info.get('cpu_percent', 0), reverse=True)[:20]
        self.process_table.setRowCount(len(process_list))
        for row, proc in enumerate(process_list):
            pid_item = QTableWidgetItem(str(proc.info.get('pid')))
            name_item = QTableWidgetItem(proc.info.get('name') or "N/A")
            cpu_item = QTableWidgetItem(f"{proc.info.get('cpu_percent', 0)}%")
            mem_item = QTableWidgetItem(f"{proc.info.get('memory_percent', 0):.2f}%")

            # Center numeric values
            for item in (pid_item, cpu_item, mem_item):
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            self.process_table.setItem(row, 0, pid_item)
            self.process_table.setItem(row, 1, name_item)
            self.process_table.setItem(row, 2, cpu_item)
            self.process_table.setItem(row, 3, mem_item)

    def filter_processes(self):
        # Filters processes based on the entered text
        filter_text = self.filter_input.text().lower()
        if not filter_text:
            filtered = self.all_processes
        else:
            filtered = [p for p in self.all_processes if filter_text in (p.info.get('name') or "").lower()]
        self.populate_process_table(filtered)

    def process_table_menu(self, pos: QPoint):
        # Context menu to kill a process
        index = self.process_table.indexAt(pos)
        if not index.isValid():
            return

        menu = QMenu()
        kill_action = menu.addAction("Kill Process")
        action = menu.exec(self.process_table.viewport().mapToGlobal(pos))
        if action == kill_action:
            pid_item = self.process_table.item(index.row(), 0)
            if pid_item:
                pid = int(pid_item.text())
                self.kill_process(pid)

    def kill_process(self, pid):
        try:
            proc = psutil.Process(pid)
            proc.terminate()
            proc.wait(3)
            QMessageBox.information(self, "Success", f"Process {pid} was terminated.")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Error terminating process {pid}:\n{str(e)}")
        self.update_metrics()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AdvancedSystemMonitor()
    window.show()
    sys.exit(app.exec())
