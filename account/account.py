import json
import bcrypt
from datetime import datetime
import re
import os

DATA_FILE = os.path.join(os.path.expanduser("~"), "PycharmProjects", "MAVIS", "account", "users.json")
TOKEN_FILE = os.path.join(os.path.expanduser("~"), "PycharmProjects", "MAVIS", "account", "token.json")

# Farbcodes definieren
red = "\033[91m"
green = "\033[92m"
blue = "\033[94m"
reset = "\033[0m"


def load_users():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_users(users):
    with open(DATA_FILE, "w") as file:
        json.dump(users, file, indent=4)


def load_tokens():
    try:
        with open(TOKEN_FILE, "r") as file:
            tokens = json.load(file)
        return tokens["tokens"]
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_tokens(tokens):
    with open(TOKEN_FILE, "w") as file:
        json.dump({"tokens": tokens}, file, indent=4)


def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


def check_password(hashed, password):
    return bcrypt.checkpw(password.encode(), hashed.encode())


def hash_token(token):
    return bcrypt.hashpw(token.encode(), bcrypt.gensalt()).decode()


def check_token(hashed_token, token):
    return bcrypt.checkpw(token.encode(), hashed_token.encode())


def validate_age(birthdate):
    try:
        birth_date = datetime.strptime(birthdate, "%Y-%m-%d")
        age = (datetime.today() - birth_date).days // 365
        return 18 <= age <= 120
    except ValueError:
        return False


def validate_password(password):
    return (
            8 <= len(password) <= 20
            and re.search(r"[A-Za-z]", password)
            and re.search(r"\d", password)
            and re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)
    )


def register(user_type="Standard"):
    print("\n--- Registration ---")
    users = load_users()

    # Username Eingabe
    while True:
        username = input(f"{blue}Username{reset}:")
        if not username.strip():
            print(f"{red}ERROR{reset}: Username cannot be empty!")
            continue
        if username in users:
            print(f"{red}ERROR{reset}: This username is already taken! Please choose another one.")
            continue
        break

    # E-Mail Eingabe
    while True:
        email = input(f"{blue}E-Mail{reset}:")
        if "@" in email and "." in email:
            if any(user["email"] == email for user in users.values()):
                print(f"{red}ERROR{reset}: This email is already in use. Please choose another one.")
                continue
            break
        print(f"{red}ERROR{reset}: Invalid email address!")

    # Geburtsdatum Eingabe
    while True:
        birthdate = input(f"{blue}Date of birth (YYYY-MM-DD){reset}:")
        if validate_age(birthdate):
            break
        print(f"{red}ERROR{reset}: Invalid birthdate or age is not valid. You must be at least 18 years old.")

    # Passwort Eingabe
    while True:
        password = input(f"{blue}Password{reset}:")
        if validate_password(password):
            break
        print(
            f"{red}ERROR{reset}: Password must be between 8 and 20 characters, contain letters, numbers, and special characters.")

    # Bestätigung des Passworts
    while True:
        confirm_password = input(f"{blue}Repeat password{reset}:")
        if password == confirm_password:
            break
        print(f"{red}ERROR{reset}: Passwords do not match!")

    # Benutzer registrieren
    users[username] = {
        "email": email,
        "birthdate": birthdate,
        "password": hash_password(password),
        "user_type": user_type,
    }
    save_users(users)
    print(f"{green}Registration successful!{reset}")


def register_mavis_ultra():
    print("\n--- MAVIS Ultra Registration ---")
    tokens = load_tokens()

    if not tokens:  # Falls keine Tokens vorhanden sind
        print(f"{red}ERROR{reset}: No valid tokens available. You cannot proceed with MAVIS Ultra registration.")
        return  # Beende die Funktion, da keine Tokens vorhanden sind

    # Token Eingabe
    while True:
        token = input(f"{blue}Enter your MAVIS Ultra token{reset}:")

        # Überprüfen der Tokens
        token_valid = False
        for hashed_token in tokens:
            try:
                if check_token(hashed_token, token):
                    print(f"{green}Token verified successfully! Proceeding with registration...{reset}")
                    token_valid = True
                    break
            except ValueError as e:
                # Fehlerbehandlung, falls das Salt ungültig ist
                print(f"{red}ERROR{reset}: Invalid token format. Please check the stored tokens.")
                return  # Beende die Funktion, da ein ungültiger Token gefunden wurde

        if token_valid:
            break
        else:
            print(f"{red}ERROR{reset}: Invalid token. Please try again.")

    # Nach erfolgreicher Token-Überprüfung wird die Registrierung fortgesetzt
    register("MAVIS Ultra")

def login():
    print("\n--- Login ---")
    username_or_email = input(f"{blue}Username or Email{reset}:")
    password = input(f"{blue}Password{reset}:")
    users = load_users()

    for username, data in users.items():
        if username_or_email in [username, data["email"]] and check_password(data["password"], password):
            greeting = f"Welcome {username}!"
            if data.get("user_type") == "MAVIS Ultra":
                greeting = f"{green}Welcome MAVIS Ultra User{username}!{reset}"
            print(greeting)
            exit()

    print(f"{red}ERROR{reset}: Incorrect login details!")

def main():
    # Zuerst sicherstellen, dass einige Tokens (vielleicht für die Ultra-Registrierung) erstellt werden.
    tokens = load_tokens()
    if not tokens:  # Falls keine Tokens vorhanden sind, erstellen wir einen
        print(f"{red}ERROR{reset}: No token found. You cannot use this software.")

    while True:
        print("\nOptions:\n [1] Login\n [2] Register\n [3] Register as a MAVIS Ultra user")
        choice = input("Selection [1/2/3]:")

        if choice == "1":
            login()
        elif choice == "2":
            register("Standard")
        elif choice == "3":
            register_mavis_ultra()
        else:
            print(f"{red}ERROR{reset}: Invalid selection!")

if __name__ == "__main__":
    main()
