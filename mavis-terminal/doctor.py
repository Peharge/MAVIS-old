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

"""
Doctor script for MAVIS project.
Checks the integrity of the .env file, verifies essential tool installations,
recursively scans the project directory, and führt erweiterte Checks durch:
- Pfad-Literal-Korrektur (sanitize_path)
- Syntax-Checks per ast.parse und compileall
- Bytecode-Kompilierungstest via py_compile.compile
- Datei-Encoding-Prüfung
- Erweiterte Berechtigungsprüfungen (Lesen/Schreiben/Executable)
- Environment-Variablen-Validierung
- Dependency-Lock-Check für Python (pip check) und Node (npm ci --dry-run)
- Plattform-Konsistenz-Checks
"""

import os
import sys
import subprocess
import getpass
import argparse
import logging
import ast
import compileall
import py_compile
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed


DEFAULT_THREADS = 4
LOG_FORMAT = "%(asctime)s %(levelname)s: %(message)s"


# ANSI color codes
class C:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    RESET = "\033[0m"
    BOLD = "\033[1m"


def run_cmd(cmd, cwd=None, timeout=60):
    """
    Run a command; return (returncode, stdout, stderr)
    """
    try:
        result = subprocess.run(
            cmd,
            cwd=cwd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=timeout
        )
        return result.returncode, result.stdout.strip(), result.stderr.strip()
    except Exception as e:
        return -1, "", str(e)


def detect_project_path(custom: Path = None) -> Path:
    if custom:
        return custom
    user = getpass.getuser()
    default = Path("C:/Users") / user / "PycharmProjects" / "MAVIS"
    return default if default.exists() else Path.cwd()


def sanitize_path(p: str) -> str:
    """
    Wandelt einen Windows-Pfad um in einen sicheren Raw-String bzw. ersetzt Backslashes durch Slashes.
    """
    # Prüfen auf typische Windows-Laufwerke
    if p.startswith(("C:\\", "D:\\", "E:\\")):
        return p.replace("\\\\", "/").replace("\\", "/")
    return p


def check_python_syntax(root: Path, report):
    """
    Parse alle .py-Dateien und kompiliere sie via compileall.
    """
    for py_file in root.rglob("*.py"):
        try:
            source = py_file.read_text(encoding="utf-8")
            ast.parse(source)  # SyntaxCheck per ast
            report.add_pass(f"Syntax OK: {py_file}")
        except SyntaxError as e:
            report.add_issue(f"SyntaxError in {py_file}: {e}")
    # Bytecode-Komplikationstest über alle Module
    compileall.compile_dir(str(root), force=True, quiet=1)


def check_pycompile(root: Path, report):
    """
    Testet die Bytecode-Kompilierung jeder .py-Datei mittels py_compile.
    """
    for py_file in root.rglob("*.py"):
        try:
            py_compile.compile(str(py_file), doraise=True)
            report.add_pass(f"Bytecode OK: {py_file}")
        except py_compile.PyCompileError as e:
            report.add_issue(f"PyCompileError in {py_file}: {e.msg}")


def check_encoding(file: Path, report):
    """
    Prüft, ob die Datei im UTF-8-Format kodiert ist.
    """
    try:
        file.open(encoding="utf-8").read()
        report.add_pass(f"UTF-8 OK: {file}")
    except UnicodeDecodeError as e:
        report.add_issue(f"Encoding issue in {file}: {e}")


def check_permissions(file: Path, report):
    """
    Überprüft, ob die Datei Lese-, Schreib- und Ausführrechte besitzt.
    """
    modes = []
    if os.access(file, os.R_OK):
        modes.append("read")
    if os.access(file, os.W_OK):
        modes.append("write")
    if os.access(file, os.X_OK):
        modes.append("exec")
    if not modes:
        report.add_issue(f"No permissions: {file}")
    else:
        report.add_pass(f"Permissions {modes} OK: {file}")


def check_env_vars(required: list[str], report, env_path: Path):
    """
    Validiert die in der .env-Datei definierten Umgebungsvariablen gegen ein Schema.
    """
    try:
        from dotenv import dotenv_values
    except ImportError:
        report.add_issue("python-dotenv fehlt, um .env-Variablen zu validieren")
        return

    if not env_path.exists():
        report.add_issue(f".env file not found: {env_path}")
        return

    env = dotenv_values(env_path)
    for key in required:
        if key not in env:
            report.add_issue(f"Missing env var: {key}")
        else:
            report.add_pass(f"Env var {key} present")


def check_dependencies(report, project_path: Path):
    """
    Prüft die Abhängigkeiten in requirements.txt via pip check und in package.json via npm ci --dry-run.
    """
    # Python-Abhängigkeiten
    if (project_path / "requirements.txt").exists() or (project_path / "pyproject.toml").exists():
        code, out, err = run_cmd(["pip", "check"])
        if code != 0:
            report.add_issue("pip dependency check failures")
        else:
            report.add_pass("pip dependencies OK")
    # Node-Abhängigkeiten
    if (project_path / "package.json").exists():
        code, out, err = run_cmd(["npm", "ci", "--dry-run"], cwd=str(project_path))
        if code != 0:
            report.add_issue("npm dependency check failures")
        else:
            report.add_pass("npm dependencies OK")


def advanced_checks(proj: Path, report):
    """
    Führt erweiterte Checks für alle .py-Dateien sowie Environment- und Dependency-Checks aus.
    """
    # 1. Überprüfe Encoding, Permissions und sanitiziere Pfad für alle Python-Dateien
    for py_file in proj.rglob("*.py"):
        check_encoding(py_file, report)
        check_permissions(py_file, report)
        # Optional: Ausgabe des sanierten Pfads (hilfreich für Pfad-Konsistenz)
        sanitized = sanitize_path(str(py_file))
        report.add_pass(f"Sanitized path: {sanitized}")

    # 2. Syntaxvalidierung
    check_python_syntax(proj, report)
    # 3. Bytecode-Kompilierung per py_compile
    check_pycompile(proj, report)
    # 4. Überprüfe Environment-Variablen (Beispiel: Hier werden beispielhafte Variablen geprüft)
    env_path = proj / ".env"
    check_env_vars(["DB_HOST", "DB_USER", "DB_PASS"], report, env_path)
    # 5. Dependency-Lock-Check
    check_dependencies(report, proj)


class Report:
    def __init__(self, fmt="text"):
        self.issues = []
        self.passes = []
        self.fmt = fmt

    def add_issue(self, msg):
        logging.warning(msg)
        self.issues.append(msg)

    def add_pass(self, msg):
        logging.info(msg)
        self.passes.append(msg)

    def summary(self):
        if self.fmt == "json":
            import json
            print(json.dumps({"issues": self.issues, "passes": self.passes}, indent=2))
        else:
            print(f"\n{C.BOLD}Doctor Script Summary{C.RESET}")
            if self.issues:
                print(f"{C.RED}Issues Detected:{C.RESET}")
                for i, m in enumerate(self.issues, 1):
                    print(f"  {i}. {m}")
            else:
                print(f"{C.GREEN}All checks passed!{C.RESET}")


def check_file(path: Path, report: Report):
    if not path.exists():
        report.add_issue(f"Missing file: {path}")
        return False
    if not os.access(path, os.R_OK):
        report.add_issue(f"Cannot read file: {path}")
        return False
    report.add_pass(f"File OK: {path}")
    return True


def check_tool(name, cmd, parse=lambda out: out.splitlines()[0], report=None):
    logging.info(f"Checking {name}...")
    code, out, err = run_cmd(cmd)
    if code == 0 and (out or err):
        version = parse(out or err)
        report.add_pass(f"{name} found: {version}")
        return True
    report.add_issue(f"{name} missing or version failed")
    return False


# Language-specific workflows

def python_checks(proj: Path, report: Report):
    # Lint (flake8), typecheck (mypy), test (pytest)
    if (proj / "requirements.txt").exists() or (proj / "pyproject.toml").exists():
        for tool, args in [("flake8", ["flake8", str(proj)]),
                           ("mypy", ["mypy", str(proj)]),
                           ("pytest", ["pytest", str(proj)])]:
            check_tool(tool, args, report=report)
    else:
        report.add_pass("No Python config found, skipping Python checks")


def cpp_checks(proj: Path, report: Report):
    # Detect CMakeLists.txt or .vcxproj
    if (proj / "CMakeLists.txt").exists():
        build_dir = proj / "_build"
        build_dir.mkdir(exist_ok=True)
        check_tool("cmake-configure", ["cmake", str(proj)], report=report)
        check_tool("cmake-build", ["cmake", "--build", str(build_dir)], report=report)
    else:
        report.add_pass("No CMake project found, skipping C++ checks")


def java_checks(proj: Path, report: Report):
    # Maven oder Gradle
    if (proj / "pom.xml").exists():
        check_tool("mvn-compile", ["mvn", "-f", str(proj / "pom.xml"), "compile"], report=report)
    elif (proj / "build.gradle").exists():
        check_tool("gradle-build", ["gradle", "build", "-p", str(proj)], report=report)
    else:
        report.add_pass("No Java project found, skipping Java checks")


def js_checks(proj: Path, report: Report):
    if (proj / "package.json").exists():
        check_tool("npm-install", ["npm", "install", str(proj)], report=report)
        check_tool("npm-lint", ["npm", "run", "lint", "--prefix", str(proj)], report=report)
        check_tool("npm-test", ["npm", "test", "--prefix", str(proj)], report=report)
    else:
        report.add_pass("No package.json found, skipping JS/TS checks")


def dotnet_checks(proj: Path, report: Report):
    sln_files = list(proj.glob("*.sln"))
    if sln_files:
        for sln in sln_files:
            check_tool("dotnet-build", ["dotnet", "build", str(sln)], report=report)
            check_tool("dotnet-test", ["dotnet", "test", str(sln)], report=report)
    else:
        report.add_pass("No .NET solution found, skipping .NET checks")


def rust_checks(proj: Path, report: Report):
    if (proj / "Cargo.toml").exists():
        check_tool("cargo-check", ["cargo", "check", "--manifest-path", str(proj / "Cargo.toml")], report=report)
        check_tool("cargo-test", ["cargo", "test", "--manifest-path", str(proj / "Cargo.toml")], report=report)
    else:
        report.add_pass("No Cargo.toml, skipping Rust checks")


def go_checks(proj: Path, report: Report):
    if (proj / "go.mod").exists():
        check_tool("go-build", ["go", "build", "./..."], report=report)
        check_tool("go-test", ["go", "test", "./..."], report=report)
    else:
        report.add_pass("No go.mod, skipping Go checks")


def docker_checks(proj: Path, report: Report):
    if (proj / "Dockerfile").exists():
        check_tool("docker-build", ["docker", "build", "-t", "mavis_project", str(proj)], report=report)
    if (proj / "docker-compose.yml").exists():
        check_tool("docker-compose-config", ["docker-compose", "-f", str(proj / "docker-compose.yml"), "config"],
                   report=report)


def main():
    parser = argparse.ArgumentParser("Doctor Script: full-stack project checker")
    parser.add_argument("-p", "--path", type=Path, help="Project path")
    parser.add_argument("-t", "--threads", type=int, default=DEFAULT_THREADS)
    parser.add_argument("-o", "--output", choices=["text", "json"], default="text")
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args()

    # Logging setup
    level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(level=level, format=LOG_FORMAT)

    project_path = detect_project_path(args.path)
    print(f"Scanning project at: {project_path}")

    report = Report(fmt=args.output)

    # 1) Basis-Check: .env file
    check_file(project_path / ".env", report)

    # 2) System-Tools
    system_tools = [
        ("python", [sys.executable, "--version"]),
        ("git", ["git", "--version"]),
        ("wmic", ["wmic", "os", "get", "Caption"]),
        ("wsl", ["wsl", "--version"]),
        ("powershell", ["powershell", "-Command", "$PSVersionTable.PSVersion"]),
    ]
    for name, cmd in system_tools:
        check_tool(name, cmd, report=report)

    # 3) Parallele language-spezifische Checks
    tasks = [python_checks, cpp_checks, java_checks,
             js_checks, dotnet_checks, rust_checks,
             go_checks, docker_checks]
    with ThreadPoolExecutor(max_workers=args.threads) as exe:
        futures = [exe.submit(func, project_path, report) for func in tasks]
        for _ in as_completed(futures):
            pass

    # 4) Erweiterte Checks: Syntax, Bytecode, Encoding, Permissions, Environment- und Dependency-Checks
    advanced_checks(project_path, report)

    # 5) Finales Summary
    report.summary()


if __name__ == "__main__":
    main()
