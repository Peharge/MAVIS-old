import bcrypt

# Passwort vom Benutzer abfragen
password = input("Gib dein Passwort ein:")

# Sicherstellen, dass das Passwort korrekt kodiert ist
password_bytes = password.encode('utf-8')

# Salz erzeugen
salt = bcrypt.gensalt()

# Passwort mit Salz verschlüsseln
hashed_pw = bcrypt.hashpw(password_bytes, salt)

# Verschlüsselten Token ausgeben
print("Verschlüsselter Token:", hashed_pw.decode('utf-8'))
