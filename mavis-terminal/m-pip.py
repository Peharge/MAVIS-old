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
import sys
import subprocess
from PyQt6 import QtCore, QtWidgets

# Pfad zur virtuellen Umgebung
venv_path = f"C:\\Users\\{os.getlogin()}\\PycharmProjects\\MAVIS\\.env"
pip_executable = os.path.join(venv_path, "Scripts", "pip.exe")

# QSS-Stylesheet (Style-Sheet)
STYLE_SHEET = """
QWidget {
    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #1b2631, stop:1 #0f1626);
    color: #FFFFFF;
    font-family: 'Roboto', sans-serif;
    font-size: 14px;
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
"""

class PipManagerWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("PIP-Paketmanager")
        self.resize(800, 600)
        self.layout = QtWidgets.QVBoxLayout(self)

        user = os.getenv("USERNAME") or os.getenv("USER")
        icon_path = f"C:/Users/{user}/PycharmProjects/MAVIS/icons/mavis-logo.ico"
        self.setWindowIcon(QIcon(icon_path))

        # Überschrift
        header = QtWidgets.QLabel("Installierte Pakete")
        header.setObjectName("title")
        header.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(header)

        # Table zur Anzeige der Pakete
        self.table = QtWidgets.QTableWidget(0, 3)
        self.table.setHorizontalHeaderLabels(["Paket", "Version", "Aktionen"])
        self.layout.addWidget(self.table)

        # Refresh Button
        refresh_button = QtWidgets.QPushButton("Liste aktualisieren")
        refresh_button.clicked.connect(self.load_packages)
        self.layout.addWidget(refresh_button)

        # Initiale Ladung der Pakete
        self.load_packages()

    def load_packages(self):
        """Lade die installierten Pakete mit pip freeze und befülle die Tabelle."""
        self.table.setRowCount(0)  # Tabelle leeren

        try:
            result = subprocess.run([pip_executable, "freeze"], capture_output=True, text=True, check=True)
            packages = result.stdout.strip().splitlines()
        except subprocess.CalledProcessError as e:
            QtWidgets.QMessageBox.critical(self, "Fehler", f"Fehler beim Laden der Pakete:\n{e}")
            return

        # Pakete in der Tabelle anzeigen
        for package in packages:
            # Erwartetes Format: paket==version
            if "==" in package:
                name, version = package.split("==")
            else:
                name, version = package, "Unbekannt"

            row_position = self.table.rowCount()
            self.table.insertRow(row_position)

            # Paketname
            name_item = QtWidgets.QTableWidgetItem(name)
            self.table.setItem(row_position, 0, name_item)
            # Version
            version_item = QtWidgets.QTableWidgetItem(version)
            self.table.setItem(row_position, 1, version_item)
            # Update Button
            update_btn = QtWidgets.QPushButton("Update")
            update_btn.clicked.connect(lambda _, pkg=name, row=row_position: self.update_package(pkg, row))
            self.table.setCellWidget(row_position, 2, update_btn)

        # Spalten anpassen
        self.table.resizeColumnsToContents()

    def update_package(self, package, row):
        """Führe ein pip update für das angegebene Paket aus."""
        confirm = QtWidgets.QMessageBox.question(self, "Update bestätigen",
                                                 f"Möchtest du das Paket '{package}' aktualisieren?")
        if confirm != QtWidgets.QMessageBox.StandardButton.Yes:
            return

        # Starte den Update-Prozess und zeige einen Fortschrittsdialog
        progress_dialog = QtWidgets.QProgressDialog(f"Updating {package}...", "Abbrechen", 0, 0, self)
        progress_dialog.setWindowModality(QtCore.Qt.WindowModality.WindowModal)
        progress_dialog.setMinimumDuration(0)
        progress_dialog.show()

        def run_update():
            try:
                result = subprocess.run([pip_executable, "install", "--upgrade", package],
                                        capture_output=True, text=True, check=True)
                output = result.stdout
            except subprocess.CalledProcessError as e:
                output = e.stderr or str(e)
            QtCore.QMetaObject.invokeMethod(self, "update_finished", QtCore.Qt.ConnectionType.QueuedConnection,
                                            QtCore.Q_ARG(str, package), QtCore.Q_ARG(str, output), QtCore.Q_ARG(int, row))

        # Start in einem separaten Thread
        updater_thread = QtCore.QThread()
        worker = Worker(run_update)
        worker.moveToThread(updater_thread)
        updater_thread.started.connect(worker.run)
        # Aufräumen nach Abschluss
        worker.finished.connect(updater_thread.quit)
        worker.finished.connect(worker.deleteLater)
        updater_thread.finished.connect(updater_thread.deleteLater)
        updater_thread.start()

    @QtCore.pyqtSlot(str, str, int)
    def update_finished(self, package, output, row):
        QtWidgets.QMessageBox.information(self, "Update beendet", f"Update von '{package}' abgeschlossen:\n{output}")
        # Nach Update die Version in der Tabelle neu laden
        self.load_packages()


class Worker(QtCore.QObject):
    finished = QtCore.pyqtSignal()

    def __init__(self, fn):
        super().__init__()
        self.fn = fn

    def run(self):
        self.fn()
        self.finished.emit()


def main():
    app = QtWidgets.QApplication(sys.argv)
    # Style setzen
    app.setStyleSheet(STYLE_SHEET)
    widget = PipManagerWidget()
    widget.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
