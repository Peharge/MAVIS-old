import os

# Farbcodes definieren
red = "\033[91m"
green = "\033[92m"
yellow = "\033[93m"
blue = "\033[94m"
magenta = "\033[95m"
cyan = "\033[96m"
white = "\033[97m"
black = "\033[30m"
orange = "\033[38;5;214m"
reset = "\033[0m"
bold = "\033[1m"

# Funktion zur Auswahl der Ausführungsart
def start_mavis():
    print(f"Would you like to run MAVIS as:")
    print(f"[1] Edge Extension")
    print(f"[2] Browser")

    while True:
        choice = input(f"Enter your choice [1 / 2]:").strip()

        if choice == '1':
            print(f"{green}Starting MAVIS as Edge Extension...{reset}")
            try:
                os.system('python run_with_browser/run_with_browser-ext.py')  # run_with_browser-ext.py wird ausgeführt
            except Exception as e:
                print(f"{red}Error running extension.py: {e}{reset}")
            break
        elif choice == '2':
            print(f"{blue}Starting MAVIS in Browser...{reset}")
            try:
                os.system('python run_with_browser/run_with_browser.py')  # run_with_browser.py wird ausgeführt
            except Exception as e:
                print(f"{red}Error running browser.py: {e}{reset}")
            break
        else:
            print(f"{red}Invalid choice. Please enter 1 or 2.{reset}")

# Hauptprogramm starten
if __name__ == "__main__":
    start_mavis()
