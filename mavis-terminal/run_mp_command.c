/*
   Englisch | Peharge: This source code is released under the MIT License.

   Usage Rights:
   The source code may be copied, modified, and adapted to individual requirements.
   Users are permitted to use this code in their own projects, both for private and commercial purposes.
   However, it is recommended to modify the code only if you have sufficient programming knowledge,
   as changes could cause unintended errors or security risks.

   Dependencies and Additional Frameworks:
   The code relies on the use of various frameworks and executes additional files.
   Some of these files may automatically install further dependencies required for functionality.
   It is strongly recommended to perform installation and configuration in an isolated environment
   (e.g., a virtual environment) to avoid potential conflicts with existing software installations.

   Disclaimer:
   Use of the code is entirely at your own risk.
   Peharge assumes no liability for damages, data loss, system errors, or other issues
   that may arise directly or indirectly from the use, modification, or redistribution of the code.

   Please read the full terms of the MIT License to familiarize yourself with your rights and obligations.
*/

/*
   Deutsch | Peharge: Dieser Quellcode wird unter der MIT-Lizenz veröffentlicht.

   Nutzungsrechte:
   Der Quellcode darf kopiert, bearbeitet und an individuelle Anforderungen angepasst werden.
   Nutzer sind berechtigt, diesen Code in eigenen Projekten zu verwenden, sowohl für private als auch kommerzielle Zwecke.
   Es wird jedoch empfohlen, den Code nur dann anzupassen, wenn Sie über ausreichende Programmierkenntnisse verfügen,
   da Änderungen unbeabsichtigte Fehler oder Sicherheitsrisiken verursachen könnten.

   Abhängigkeiten und zusätzliche Frameworks:
   Der Code basiert auf der Nutzung verschiedener Frameworks und führt zusätzliche Dateien aus.
   Einige dieser Dateien könnten automatisch weitere Abhängigkeiten installieren, die für die Funktionalität erforderlich sind.
   Es wird dringend empfohlen, die Installation und Konfiguration in einer isolierten Umgebung (z. B. einer virtuellen Umgebung) durchzuführen,
   um mögliche Konflikte mit bestehenden Softwareinstallationen zu vermeiden.

   Haftungsausschluss:
   Die Nutzung des Codes erfolgt vollständig auf eigene Verantwortung.
   Peharge übernimmt keinerlei Haftung für Schäden, Datenverluste, Systemfehler oder andere Probleme,
   die direkt oder indirekt durch die Nutzung, Modifikation oder Weitergabe des Codes entstehen könnten.

   Bitte lesen Sie die vollständigen Lizenzbedingungen der MIT-Lizenz, um sich mit Ihren Rechten und Pflichten vertraut zu machen.
*/

/*
   Français | Peharge: Ce code source est publié sous la licence MIT.

   Droits d'utilisation:
   Le code source peut être copié, édité et adapté aux besoins individuels.
   Les utilisateurs sont autorisés à utiliser ce code dans leurs propres projets, à des fins privées et commerciales.
   Il est cependant recommandé d'adapter le code uniquement si vous avez des connaissances suffisantes en programmation,
   car les modifications pourraient provoquer des erreurs involontaires ou des risques de sécurité.

   Dépendances et frameworks supplémentaires:
   Le code est basé sur l'utilisation de différents frameworks et exécute des fichiers supplémentaires.
   Certains de ces fichiers peuvent installer automatiquement des dépendances supplémentaires requises pour la fonctionnalité.
   Il est fortement recommandé d'effectuer l'installation et la configuration dans un environnement isolé (par exemple un environnement virtuel),
   pour éviter d'éventuels conflits avec les installations de logiciels existantes.

   Clause de non-responsabilité:
   L'utilisation du code est entièrement à vos propres risques.
   Peharge n'assume aucune responsabilité pour tout dommage, perte de données, erreurs système ou autres problèmes,
   pouvant découler directement ou indirectement de l'utilisation, de la modification ou de la diffusion du code.

   Veuillez lire l'intégralité des termes et conditions de la licence MIT pour vous familiariser avec vos droits et responsabilités.
*/

#include <windows.h>
#include <shellapi.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#pragma comment(lib, "shell32.lib")

int main(int argc, char* argv[]) {
    if (argc < 2) {
        fprintf(stderr, "[ERROR] No command specified.\n");
        return 1;
    }

    // Kommandozeile für PowerShell-Befehl bauen
    size_t totalLen = 0;
    for (int i = 1; i < argc; ++i) {
        totalLen += strlen(argv[i]) + 3; // Für Anführungszeichen und Leerzeichen
    }

    char* psCommand = (char*)malloc(totalLen + 1);
    if (!psCommand) {
        fprintf(stderr, "[ERROR] Memory allocation failed.\n");
        return 1;
    }

    psCommand[0] = '\0';
    for (int i = 1; i < argc; ++i) {
        strcat(psCommand, "\"");
        strcat(psCommand, argv[i]);
        strcat(psCommand, "\" ");
    }

    // Komplette Parameterzeile vorbereiten
    const char* prefix = "-NoProfile -ExecutionPolicy Bypass -Command ";
    size_t parametersLen = strlen(prefix) + strlen(psCommand) + 1;

    char* parameters = (char*)malloc(parametersLen);
    if (!parameters) {
        fprintf(stderr, "[ERROR] Memory allocation failed.\n");
        free(psCommand);
        return 1;
    }

    strcpy(parameters, prefix);
    strcat(parameters, psCommand);
    free(psCommand);

    // SHELLEXECUTEINFOA Struktur initialisieren
    SHELLEXECUTEINFOA sei;
    ZeroMemory(&sei, sizeof(sei));
    sei.cbSize = sizeof(SHELLEXECUTEINFOA);
    sei.fMask = SEE_MASK_NOCLOSEPROCESS;
    sei.hwnd = NULL;
    sei.lpVerb = "runas";                  // Start as administrator
    sei.lpFile = "powershell.exe";
    sei.lpParameters = parameters;
    sei.nShow = SW_SHOWDEFAULT;

    if (!ShellExecuteExA(&sei)) {
        DWORD errorCode = GetLastError();
        fprintf(stderr, "[ERROR] Process start failed. Error code: %lu\n", errorCode);
        free(parameters);
        return 1;
    }

    // Auf Prozess warten
    WaitForSingleObject(sei.hProcess, INFINITE);

    DWORD exitCode = 0;
    GetExitCodeProcess(sei.hProcess, &exitCode);

    CloseHandle(sei.hProcess);
    free(parameters);

    return (int)exitCode;
}
