#!/bin/bash

# Funktionen für die Installation
install_git() {
    if command -v git >/dev/null 2>&1; then
        echo "✅ Git is already installed."
    else
        echo "🔄 Installing Git..."
        if [[ "$OSTYPE" == "darwin"* ]]; then
            brew install git || { echo "❌ Git installation failed. Visit https://git-scm.com."; exit 1; }
        else
            sudo apt update && sudo apt install -y git || { echo "❌ Git installation failed. Visit https://git-scm.com."; exit 1; }
        fi
    fi
}

install_python() {
    if command -v python3 >/dev/null 2>&1; then
        echo "✅ Python is already installed."
    else
        echo "🔄 Installing Python..."
        if [[ "$OSTYPE" == "darwin"* ]]; then
            brew install python || { echo "❌ Python installation failed. Visit https://www.python.org."; exit 1; }
        else
            sudo apt update && sudo apt install -y python3 python3-venv || { echo "❌ Python installation failed. Visit https://www.python.org."; exit 1; }
        fi
    fi
}

install_ollama() {
    if command -v ollama >/dev/null 2>&1; then
        echo "✅ Ollama is already installed."
    else
        echo "🔄 Installing Ollama..."
        if [[ "$OSTYPE" == "darwin"* ]]; then
            brew install --cask ollama || { echo "❌ Ollama installation failed. Visit https://ollama.com/download."; exit 1; }
        else
            curl -fsSL https://ollama.com/download | sh || { echo "❌ Ollama installation failed. Visit https://ollama.com/download."; exit 1; }
        fi
    fi
}

create_folder() {
    folder="$HOME/PycharmProjects"
    if [ ! -d "$folder" ]; then
        mkdir -p "$folder"
        echo "✅ Folder created: $folder"
    else
        echo "ℹ️ Folder already exists: $folder"
    fi
}

clone_repository() {
    repo_url="https://github.com/Peharge/MAVIS"
    target_path="$HOME/PycharmProjects/MAVIS"
    if [ -d "$target_path" ]; then
        echo "ℹ️ Repository has already been cloned."
    else
        echo "🔄 Cloning repository..."
        git clone "$repo_url" "$target_path" || { echo "❌ Repository could not be cloned."; exit 1; }
    fi
}

create_virtual_environment() {
    env_path="$HOME/PycharmProjects/MAVIS/env"
    if [ -d "$env_path" ]; then
        echo "ℹ️ Virtual environment already exists."
    else
        echo "🔄 Creating virtual environment..."
        python3 -m venv "$env_path" || { echo "❌ Virtual environment could not be created."; exit 1; }
    fi
}

start_ui() {
    script_path="$HOME/PycharmProjects/MAVIS/run-mavis-all.sh"
    if [ -f "$script_path" ]; then
        echo "🚀 Starting User Interface..."
        bash "$script_path"
    else
        echo "❌ User interface script not found."
        exit 1
    fi
}

menu() {
    clear
    echo "MAVIS Installer"
    echo "================="
    echo "1. Install prerequisites (Git, Python, Ollama)"
    echo "2. Create folder"
    echo "3. Clone repository"
    echo "4. Create virtual environment"
    echo "5. Start user interface"
    echo "6. Finish"
    echo "================="
    read -rp "Select an option: " choice
    case $choice in
        1) install_git; install_python; install_ollama ;;
        2) create_folder ;;
        3) clone_repository ;;
        4) create_virtual_environment ;;
        5) start_ui ;;
        6) exit 0 ;;
        *) echo "❌ Invalid input. Please try again." ;;
    esac
    sleep 2
    menu
}

menu
