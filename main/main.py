import os

def run_batch_file(batch_name):
    """Führt die Batch-Datei aus, indem der vollständige Dateiname zusammengebaut wird."""
    file_name = f"run-{batch_name}.bat"
    try:
        os.system(file_name)
        print(f"Die Batch-Datei '{file_name}' wurde erfolgreich ausgeführt.\n")
    except Exception as e:
        print(f"Fehler beim Ausführen der Datei '{file_name}': {e}\n")

def display_versions():
    """Zeigt alle Versionen und zugehörigen Batch-Dateien ohne 'run-' und '.bat'."""
    print("Verfügbare MAVIS-Versionen und Batch-Dateien (ohne 'run-' und '.bat'):\n")

    versions = {
        "mavis1.2-main": "MAVIS 1.2",
        "mavis1.2-code": "MAVIS 1.2",
        "mavis1.2-code-pro": "MAVIS 1.2",
        "mavis1.2-math": "MAVIS 1.2",
        "mavis1.2-math-pro": "MAVIS 1.2",
        "mavis1.2-mini": "MAVIS 1.2",
        "mavis1.2-mini-mini": "MAVIS 1.2",
        "mavis1.3-main": "MAVIS 1.3 EAP",
        "mavis1.3_code": "MAVIS 1.3 EAP",
        "mavis1.3_code-pro": "MAVIS 1.3 EAP",
        "mavis1.3-math": "MAVIS 1.3 EAP",
        "mavis1.3-math-pro": "MAVIS 1.3 EAP",
        "mavis1.4-math": "MAVIS 1.4 EAP"
    }

    # Gruppieren der Versionen für eine saubere Anzeige
    grouped_versions = {}
    for batch_name, version in versions.items():
        if version not in grouped_versions:
            grouped_versions[version] = []
        grouped_versions[version].append(batch_name)

    # Ausgabe der gruppierten Versionen
    for i, (version, batch_files) in enumerate(grouped_versions.items(), 1):
        print(f"{i}. {version}:")
        for j, batch_file in enumerate(batch_files, 1):
            print(f"   {j}. {batch_file}")
        print()

    return versions

def get_user_input(versions):
    """Fragt den Benutzer nach der gewünschten MAVIS-Batch-Datei (direkte Eingabe)."""
    user_input = input("Geben Sie eine MAVIS-Batch-Datei ein (z. B. 'mavis1.3-main'): ").strip()

    if user_input in versions:
        run_batch_file(user_input)
    else:
        print(f"Fehler: '{user_input}' ist keine gültige Option. Bitte versuchen Sie es erneut.\n")

if __name__ == "__main__":
    versions = display_versions()
    get_user_input(versions)
