#include <iostream>
#include <cstdlib>
#include <filesystem>
#include <string>
#include <fstream>
#include <thread>
#include <chrono>

#ifdef _WIN32
#include <windows.h>
#define CLEAR_SCREEN "cls"
#else
#include <unistd.h>
#define CLEAR_SCREEN "clear"
#endif

namespace fs = std::filesystem;

// Hilfsfunktionen
void clearScreen() {
    std::system(CLEAR_SCREEN);
}

bool isCommandAvailable(const std::string& command) {
#ifdef _WIN32
    std::string checkCmd = "where " + command + " >nul 2>nul";
#else
    std::string checkCmd = "command -v " + command + " >/dev/null 2>&1";
#endif
    return std::system(checkCmd.c_str()) == 0;
}

bool isDirectoryWritable(const std::string& path) {
    std::string testFile = path + "/.test_write";
    std::ofstream ofs(testFile);
    bool writable = ofs.is_open();
    if (writable) {
        ofs.close();
        fs::remove(testFile);
    }
    return writable;
}

void runCommand(const std::string& command, const std::string& errorMessage = "", int retries = 3, int delay = 5) {
    int attempt = 0;
    int result = -1;
    while (attempt < retries) {
        result = std::system(command.c_str());
        if (result == 0) {
            break;
        }
        std::cerr << "Attempt " << (attempt + 1) << " failed: " << errorMessage << std::endl;
        std::this_thread::sleep_for(std::chrono::seconds(delay)); // Verzögerung zwischen den Versuchen
        attempt++;
    }
    if (result != 0) {
        std::cerr << "❌ Critical error: " << errorMessage << std::endl;
        std::cerr << "Command: " << command << std::endl;
        exit(EXIT_FAILURE);
    }
}

bool checkInternetConnectivity() {
#ifdef _WIN32
    return std::system("ping -n 1 google.com >nul 2>nul") == 0;
#else
    return std::system("ping -c 1 google.com >/dev/null 2>&1") == 0;
#endif
}

// Installationsfunktionen
void installGit() {
    if (isCommandAvailable("git")) {
        std::cout << "✅ Git is already installed." << std::endl;
        return;
    }
    std::cout << "🔄 Installing Git..." << std::endl;
#ifdef _WIN32
    runCommand("winget install --id Git.Git -e --source winget", "Git installation failed. Visit https://git-scm.com.");
#elif __APPLE__
    runCommand("brew install git", "Git installation failed. Visit https://git-scm.com.");
#else
    runCommand("sudo apt update && sudo apt install -y git", "Git installation failed. Visit https://git-scm.com.");
#endif
    std::cout << "✅ Git installed successfully." << std::endl;
}

void installPython() {
    if (isCommandAvailable("python3")) {
        std::cout << "✅ Python is already installed." << std::endl;
        return;
    }
    std::cout << "🔄 Installing Python..." << std::endl;
#ifdef _WIN32
    runCommand("winget install --id Python.Python.3 -e --source winget", "Python installation failed. Visit https://www.python.org.");
#elif __APPLE__
    runCommand("brew install python", "Python installation failed. Visit https://www.python.org.");
#else
    runCommand("sudo apt update && sudo apt install -y python3 python3-venv", "Python installation failed. Visit https://www.python.org.");
#endif
    std::cout << "✅ Python installed successfully." << std::endl;
}

void installOllama() {
    if (isCommandAvailable("ollama")) {
        std::cout << "✅ Ollama is already installed." << std::endl;
        return;
    }
    std::cout << "🔄 Installing Ollama..." << std::endl;
#ifdef _WIN32
    runCommand("start https://ollama.com/download", "Ollama installation failed. Visit https://ollama.com/download.");
#elif __APPLE__
    runCommand("brew install --cask ollama", "Ollama installation failed. Visit https://ollama.com/download.");
#else
    runCommand("curl -fsSL https://ollama.com/download | sh", "Ollama installation failed. Visit https://ollama.com/download.");
#endif
    std::cout << "✅ Ollama installed successfully." << std::endl;
}

// MAVIS-Installation
void createFolder(const std::string& path) {
    if (!fs::exists(path)) {
        if (!isDirectoryWritable(fs::path(path).parent_path().string())) {
            std::cerr << "❌ Error: No write permissions in the directory: " << path << std::endl;
            exit(EXIT_FAILURE);
        }
        fs::create_directories(path);
        std::cout << "✅ Folder created: " << path << std::endl;
    } else {
        std::cout << "ℹ️ Folder already exists: " << path << std::endl;
    }
}

void cloneRepository(const std::string& repoUrl, const std::string& targetPath) {
    if (fs::exists(targetPath)) {
        std::cout << "ℹ️ Repository has already been cloned." << std::endl;
        return;
    }
    std::cout << "🔄 Cloning repository..." << std::endl;
    std::string command = "git clone " + repoUrl + " " + targetPath;
    runCommand(command, "Repository could not be cloned.");
    std::cout << "✅ Repository successfully cloned." << std::endl;
}

void createVirtualEnvironment(const std::string& envPath) {
    if (fs::exists(envPath)) {
        std::cout << "ℹ️ Virtual environment already exists." << std::endl;
        return;
    }
    std::cout << "🔄 Creating virtual environment..." << std::endl;
#ifdef _WIN32
    std::string command = "python -m venv " + envPath;
#else
    std::string command = "python3 -m venv " + envPath;
#endif
    runCommand(command, "Virtual environment could not be created.");
    std::cout << "✅ Virtual environment created successfully." << std::endl;
}

void startUI(const std::string& scriptName) {
    std::cout << "🚀 Starting User Interface..." << std::endl;
#ifdef _WIN32
    std::string command = scriptName + ".bat";
#else
    std::string command = "./" + scriptName + ".sh";
#endif
    runCommand(command, "User interface could not be started.");
}

void displayMenu() {
    std::cout << "\nMAVIS Installer\n"
              << "=================\n"
              << "1. Install prerequisites (Git, Python, Ollama)\n"
              << "2. Create folder\n"
              << "3. Clone repository\n"
              << "4. Create virtual environment\n"
              << "5. Start user interface\n"
              << "6. Finish\n"
              << "=================\n";
}

int main() {
    std::string basePath;
#ifdef _WIN32
    basePath = "C:\\Users\\" + std::string(getenv("USERNAME")) + "\\PycharmProjects";
#else
    basePath = fs::path(getenv("HOME")) / "PycharmProjects";
#endif
    std::string repoUrl = "https://github.com/Peharge/MAVIS";
    std::string projectPath = basePath + "/MAVIS";
    std::string envPath = projectPath + "/env";

    if (!checkInternetConnectivity()) {
        std::cerr << "❌ Error: No internet connection. Please check your connection." << std::endl;
        return EXIT_FAILURE;
    }

    int choice;
    do {
        clearScreen();
        displayMenu();
        std::cout << "Select an option:";
        std::cin >> choice;

        switch (choice) {
            case 1:
                installGit();
                installPython();
                installOllama();
                break;
            case 2:
                createFolder(basePath);
                break;
            case 3:
                cloneRepository(repoUrl, projectPath);
                break;
            case 4:
                createVirtualEnvironment(envPath);
                break;
            case 5:
                startUI("run-mavis-all");
                break;
            case 6:
                std::cout << "Finishing..." << std::endl;
                break;
            default:
                std::cout << "❌ Invalid input. Please try again." << std::endl;
        }
#ifdef _WIN32
        Sleep(2000);  // 2 Sekunden Verzögerung für Windows
#else
        sleep(2);  // 2 Sekunden Verzögerung für macOS/Linux
#endif
    } while (choice != 6);

    return 0;
}
