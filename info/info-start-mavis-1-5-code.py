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

import sys
sys.stdout.reconfigure(encoding='utf-8')

print ("""
███╗   ███╗ █████╗ ███████╗██╗   ██╗██╗███████╗     ██╗   ███████╗     ██████╗ ██████╗ ██████╗ ███████╗
████╗ ████║██╔══██╗██╔════╝██║   ██║██║██╔════╝    ███║   ██╔════╝    ██╔════╝██╔═══██╗██╔══██╗██╔════╝
██╔████╔██║███████║███████╗██║   ██║██║███████╗    ╚██║   ███████╗    ██║     ██║   ██║██║  ██║█████╗  
██║╚██╔╝██║██╔══██║╚════██║╚██╗ ██╔╝██║╚════██║     ██║   ╚════██║    ██║     ██║   ██║██║  ██║██╔══╝  
██║ ╚═╝ ██║██║  ██║███████║ ╚████╔╝ ██║███████║     ██║██╗███████║    ╚██████╗╚██████╔╝██████╔╝███████╗
╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝  ╚═══╝  ╚═╝╚══════╝     ╚═╝╚═╝╚══════╝     ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝
""")

print(f"""🎉 A warm welcome from Peharge 🎉\n""")

print("Framework Information:")
print("----------------------")

# Farbcodes definieren
red = "\033[91m"
green = "\033[92m"
yellow = "\033[93m"
blue = "\033[94m"
reset = "\033[0m"

# Farbiges Drucken des Textes
print(f"{green}Don't forget to {yellow}update pip {red}with python -m pip install --upgrade pip {blue}every now and then{reset}")

# Funktion zum Ausgeben von Frameworks mit Beschreibung
def print_framework(title, description, color=blue):
    print(f"{color}{title}{reset} - {description}")

# Frameworks and their descriptions
frameworks = [
    ("Flask", "Lightweight web framework for Python."),
    ("ollama", "Tool for integration with AI APIs."),
    ("Werkzeug", "Utility library for WSGI applications and web development."),
    ("markdown", "Library for converting Markdown to HTML."),
    ("matplotlib", "Powerful tool for data visualization."),
    ("plotly", "Interactive data visualization in Python."),
    ("dash", "Framework for creating interactive web dashboards."),
    ("seaborn", "Extension of Matplotlib for statistical data visualization."),
    ("numpy", "Library for numerical computations."),
    ("sympy", "Symbolic computation in Python."),
    ("pandas", "Tool for data analysis and manipulation."),
    ("scipy", "Library for scientific computing and optimization."),
    ("tensorflow", "Framework for machine learning and deep learning."),
    ("torch", "PyTorch library for machine learning and deep learning."),
    ("scikit-learn", "Library for machine learning."),
    ("transformers", "Library for pretrained models (NLP, vision)."),
    ("geopandas", "Geospatial data processing with Pandas."),
    ("altair", "Declarative data visualization library."),
    ("vega_datasets", "Datasets for visualizations with Altair."),
    ("ipython", "Interactive Python shell."),
    ("kaleido", "Renderer for Plotly images."),
    ("py-cpuinfo", "Library for retrieving CPU information."),
    ("GPUtil", "Monitor GPU utilization."),
    ("requests", "HTTP library for Python."),
    ("astropy", "Library for analyzing astronomical data."),
    ("QuantLib", "Quantitative finance library."),
    ("openmdao", "Framework for multidisciplinary optimization."),
    ("pybullet", "Physics engine for simulations and robotics."),
    ("monai", "Framework for medical imaging with AI."),
    ("fenics", "Solution of partial differential equations."),
    ("pydy", "Dynamic simulation of mechanical systems."),
    ("pycalculix", "Finite element analysis in Python."),
    ("solidpython", "Creation of 3D models for OpenSCAD."),
    ("pyomo", "Modeling and optimization of mathematical problems."),
    ("gekko", "Optimization and control tool for dynamic systems."),
    ("casadi", "Optimization and control of dynamic systems."),
    ("control", "Tool for control system design and analysis."),
    ("rospy", "ROS client library for Python."),
    ("h2o", "Platform for machine learning and AI."),
    ("pint", "Unit system for physical calculations."),
    ("coolprop", "Thermophysical properties of fluids and gases."),
    ("pythermo", "Thermodynamic calculations."),
    ("biopython", "Library for bioinformatics."),
    ("opencv-python", "Computer vision library."),
    ("SimpleITK", "Image processing for medical applications."),
    ("nilearn", "Analysis and visualization of neuroimaging data."),
    ("deepchem", "Machine learning for chemistry and biology."),
    ("pymedtermino", "Processing medical terminology."),
    ("lifelines", "Survival data analysis."),
    ("rdkit", "Tools for cheminformatics."),
    ("ase", "Simulation of atomic systems."),
    ("chempy", "Chemical computations."),
    ("shapely", "Manipulation of geometric objects."),
    ("fiona", "Geospatial data access and file formats."),
    ("cartopy", "Map projection and geospatial visualization."),
    ("statsmodels", "Statistical modeling and data analysis."),
    ("yfinance", "Fetching financial market data."),
    ("QuantLib", "Quantitative finance library.")
]

# Frameworks ausgeben
for title, description in frameworks:
    print_framework(title, description)
