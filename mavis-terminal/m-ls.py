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
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTreeWidget, QTreeWidgetItem, QLabel, QScrollArea
from PyQt6.QtGui import QPalette, QColor, QIcon

class FileExplorer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("File Explorer")
        self.setGeometry(100, 100, 1000, 800)

        self.set_dark_mode()

        user = os.getenv("USERNAME") or os.getenv("USER")
        icon_path = f"C:/Users/{user}/PycharmProjects/MAVIS/icons/mavis-logo.ico"
        self.setWindowIcon(QIcon(icon_path))

        layout = QVBoxLayout()

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)

        self.tree = QTreeWidget()
        self.tree.setHeaderLabels(["Name", "Type"])
        layout.addWidget(self.tree)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)

        # Dies wird jetzt auf die Instanz von QApplication angewendet
        app.setStyleSheet("""
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
        """)

        self.status_label = QLabel("Loading...")
        layout.addWidget(self.status_label)

        self.setLayout(layout)

        self.load_directory_structure()

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

    def load_directory_structure(self):
        directory_path = f"C:\\Users\\{os.getlogin()}\\PycharmProjects\\MAVIS\\"
        self.tree.clear()

        self.add_directory_to_tree(directory_path)

        self.status_label.setText("Directory structure loaded successfully.")

    def add_directory_to_tree(self, path, parent=None):
        try:
            items = os.listdir(path)
        except PermissionError:
            return

        for item in items:
            item_path = os.path.join(path, item)
            item_type = "Directory" if os.path.isdir(item_path) else "File"

            tree_item = QTreeWidgetItem([item, item_type])

            if os.path.isdir(item_path):
                self.add_directory_to_tree(item_path, tree_item)  # Recursive call for directories

            if parent:
                parent.addChild(tree_item)
            else:
                self.tree.addTopLevelItem(tree_item)

    def resizeEvent(self, event):
        super().resizeEvent(event)

        # 66% der Breite für die 'Name' Spalte
        width = self.width()
        self.tree.setColumnWidth(0, int(width * 0.66))  # Erste Spalte (Name) 66% der Fensterbreite
        self.tree.setColumnWidth(1, int(width * 0.30))  # Zweite Spalte (Type) 34% der Fensterbreite


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileExplorer()
    window.show()
    sys.exit(app.exec())
