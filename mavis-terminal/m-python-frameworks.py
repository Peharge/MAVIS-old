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
import subprocess
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTreeWidget, QTreeWidgetItem, QLabel, QScrollArea, QTextEdit
from PyQt6.QtGui import QPalette, QColor, QIcon
from PyQt6.QtCore import Qt

def get_installed_frameworks():
    env_path = f"C:\\Users\\{os.getlogin()}\\PycharmProjects\\MAVIS\\.env"
    pip_list_cmd = f"{env_path}\\Scripts\\python.exe -m pip list"

    try:
        result = subprocess.run(pip_list_cmd, shell=True, capture_output=True, text=True, check=True)
        lines = result.stdout.split('\n')[2:]
        frameworks = {}

        for line in lines:
            parts = line.split()
            if len(parts) >= 2:
                frameworks[parts[0]] = parts[1]

        return frameworks
    except Exception as e:
        return {"Error": str(e)}

def get_framework_details(name):
    env_path = f"C:\\Users\\{os.getlogin()}\\PycharmProjects\\MAVIS\\.env"
    pip_show_cmd = f"{env_path}\\Scripts\\python.exe -m pip show {name}"

    try:
        result = subprocess.run(pip_show_cmd, shell=True, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except Exception as e:
        return f"Error retrieving details: {str(e)}"

class FrameworkViewer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python Framework Viewer")
        self.setGeometry(100, 100, 1000, 800)

        self.set_dark_mode()

        user = os.getenv("USERNAME") or os.getenv("USER")
        icon_path = f"C:/Users/{user}/PycharmProjects/MAVIS/icons/mavis-logo.ico"
        self.setWindowIcon(QIcon(icon_path))

        layout = QVBoxLayout()

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)

        # Dies wird jetzt auf die Instanz von QApplication angewendet
        app.setStyleSheet("""
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

        self.tree = QTreeWidget()
        self.tree.setHeaderLabels(["Framework", "Version"])
        self.tree.itemExpanded.connect(self.load_details_on_expand)
        layout.addWidget(self.tree)

        self.status_label = QLabel("Loading...")
        layout.addWidget(self.status_label)

        self.setLayout(layout)
        self.load_frameworks()

    def set_dark_mode(self):
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(40, 40, 40))
        palette.setColor(QPalette.ColorRole.WindowText, QColor(255, 255, 255))
        palette.setColor(QPalette.ColorRole.Base, QColor(40, 40, 40))
        palette.setColor(QPalette.ColorRole.AlternateBase, QColor(40, 40, 40))
        palette.setColor(QPalette.ColorRole.ToolTipBase, QColor(255, 255, 255))
        palette.setColor(QPalette.ColorRole.ToolTipText, QColor(0, 0, 0))
        palette.setColor(QPalette.ColorRole.Text, QColor(255, 255, 255))
        palette.setColor(QPalette.ColorRole.Button, QColor(40, 40, 40))
        palette.setColor(QPalette.ColorRole.ButtonText, QColor(255, 255, 255))
        palette.setColor(QPalette.ColorRole.Highlight, QColor(40, 40, 40))
        palette.setColor(QPalette.ColorRole.HighlightedText, QColor(255, 255, 255))
        self.setPalette(palette)

    def load_frameworks(self):
        frameworks = get_installed_frameworks()
        self.tree.clear()

        for name, version in frameworks.items():
            item = QTreeWidgetItem([name, version])
            item.setChildIndicatorPolicy(QTreeWidgetItem.ChildIndicatorPolicy.ShowIndicator)
            self.tree.addTopLevelItem(item)

        self.status_label.setText("Frameworks loaded successfully.")

    def load_details_on_expand(self, item):
        if item.childCount() == 0:  # Load details only if not already loaded
            details_text = get_framework_details(item.text(0))
            details_widget = QTextEdit()
            details_widget.setPlainText(details_text)
            details_widget.setReadOnly(True)
            details_widget.setStyleSheet("background-color: sqrt(40, 40, 40); color: white; border: none; padding: 5px;")
            details_widget.setFixedHeight(200)

            container = QTreeWidgetItem()
            item.addChild(container)
            self.tree.setItemWidget(container, 0, details_widget)
            item.setExpanded(True)

    def resizeEvent(self, event):
        super().resizeEvent(event)

        # 66% der Breite für die 'Framework' Spalte
        width = self.width()
        self.tree.setColumnWidth(0, int(width * 0.66))  # Erste Spalte (Framework) 66% der Fensterbreite
        self.tree.setColumnWidth(1, int(width * 0.30))  # Zweite Spalte (Version) 34% der Fensterbreite

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Das Stylesheet wird hier auf die 'app' Instanz angewendet
    window = FrameworkViewer()
    window.show()
    sys.exit(app.exec())
