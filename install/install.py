import subprocess
import sys
import platform
from typing import List

def confirm_action(message: str) -> bool:
    """Prompts the user for confirmation."""
    while True:
        response = input(f"{message} [y/n]: ").strip().lower()
        if response in ["y", "yes"]:
            return True
        elif response in ["n", "no"]:
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

def check_and_install(package: str, upgrade: bool = False):
    """Checks if a package is installed and installs/updates it if necessary, with user confirmation."""
    try:
        import pkg_resources
        pkg_resources.require(package)
        if upgrade:
            print(f"{package} is installed, but an upgrade is available.")
            if confirm_action(f"Do you want to upgrade {package}?"):
                subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", package])
                print(f"{package} has been upgraded.")
            else:
                print(f"Skipping upgrade for {package}.")
        else:
            print(f"{package} is already installed and up-to-date.")
    except pkg_resources.DistributionNotFound:
        print(f"{package} is not installed.")
        if confirm_action(f"Do you want to install {package}?"):
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"{package} has been installed.")
        else:
            print(f"Skipping installation for {package}.")
    except pkg_resources.VersionConflict as e:
        print(f"Version conflict for {package}: {e}.")
        if confirm_action(f"Do you want to resolve the conflict by upgrading {package}?"):
            subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", package])
            print(f"{package} has been upgraded.")
        else:
            print(f"Skipping upgrade for {package}.")

def process_packages(packages: List[str], upgrade: bool = False):
    """Processes a list of packages to check, install, or upgrade them."""
    for package in packages:
        print(f"\nChecking package: {package}")
        check_and_install(package, upgrade=upgrade)

# --- 1.1: Define packages and install them ---
packages = [
    "Flask",
    "ollama",
    "Werkzeug",
    "markdown",
    "matplotlib",
    "plotly",
    "dash",
    "seaborn",
    "numpy",
    "sympy",
    "pandas",
    "scipy",
    "tensorflow",
    "torch",
    "scikit-learn",
    "transformers",
    "geopandas",
    "altair",
    "vega_datasets",
    "altair_viewer",
    "ipython",
    "altair-saver",
    "kaleido",
    "vl-convert-python"
]

process_packages(packages, upgrade=False)

# --- 1.2: Additional specific installs ---
specific_packages = [
    "qwen-vl-utils",
    "accelerate>=0.26.0",
    "accelerate"
]

process_packages(specific_packages, upgrade=False)

# --- 1.3: vllm and uvloop installation ---
vllm_packages = ["vllm"]
process_packages(vllm_packages, upgrade=False)

if platform.system().lower() == "windows":
    print("\nSkipping uvloop installation: uvloop is not supported on Windows.")
else:
    uvloop_packages = ["uvloop"]
    process_packages(uvloop_packages, upgrade=False)

# --- Serve commands for vllm ---
print("\nTo serve vllm, use the following commands:")
print("vllm serve 'Qwen/Qwen2-VL-7B-Instruct'")
print("or")
print("vllm serve 'Qwen/Qwen2-VL-7B-Instruct' --no-uvloop\n")
