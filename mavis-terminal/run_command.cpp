#include <windows.h>
#include <iostream>
#include <string>

int main(int argc, char* argv[]) {
    if (argc < 2) {
        std::cerr << "[ERROR] No Linux command passed." << std::endl;
        return 1;
    }

    // Befehl zusammensetzen: "wsl.exe -a <argumente>"
    std::string command = "wsl.exe -a";
    for (int i = 1; i < argc; ++i) {
        command += " " + std::string(argv[i]);
    }

    // Die Standardhandles des aktuellen Terminals werden vererbt,
    // sodass interaktive Programme wie nano oder neofetch korrekt ausgeführt werden.
    STARTUPINFOA si;
    PROCESS_INFORMATION pi;
    ZeroMemory(&si, sizeof(si));
    si.cb = sizeof(si);
    si.dwFlags = STARTF_USESTDHANDLES;
    si.hStdInput  = GetStdHandle(STD_INPUT_HANDLE);
    si.hStdOutput = GetStdHandle(STD_OUTPUT_HANDLE);
    si.hStdError  = GetStdHandle(STD_ERROR_HANDLE);
    ZeroMemory(&pi, sizeof(pi));

    BOOL success = CreateProcessA(
        NULL,
        &command[0],  // CreateProcessA benötigt einen veränderbaren String
        NULL,
        NULL,
        TRUE,         // Vererbt die Standardhandles
        0,            // Keine speziellen Flags – im aktuellen Fenster ausführen
        NULL,
        NULL,
        &si,
        &pi
    );

    if (!success) {
        std::cerr << "[ERROR] Process start failed. Error code: " << GetLastError() << std::endl;
        return 1;
    }

    // Warten, bis der gestartete Prozess endet.
    WaitForSingleObject(pi.hProcess, INFINITE);
    DWORD exitCode = 0;
    GetExitCodeProcess(pi.hProcess, &exitCode);
    CloseHandle(pi.hProcess);
    CloseHandle(pi.hThread);
    return static_cast<int>(exitCode);
}
