# Using MAVIS 3  

## 1. Launching the MAVIS Installer  
To begin the installation process, execute the appropriate [`mavis-installer.bat`](https://github.com/Peharge/MAVIS/blob/main/mavis-installer/mavis-installer.bat) file for your desired MAVIS version. This will open a terminal window on your operating system, initiating the MAVIS Installer.
```bash
-------------------------------------------------
       Welcome to the MAVIS Installer 3
-------------------------------------------------
     Initiating high-tech installation...
          Prepare for the next level

                 MIT License
             Copyright (c) 2024
                   Peharge

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Gooo...

Python 3.12 is already installed.
Git is already installed.
Ollama is already installed.
MAVIS already exists.
.env file already exists.
Starting run-mavis-3-all.bat...

All MAVIS versions are available here:

1. MAVIS 3 EAP:
   1. mavis-3-main
   2. mavis-3-code
   3. mavis-3-code-pro (not jet)
   4. mavis-3-math
   5. mavis-3-math-pro (not jet)
   6. mavis-3-mini (not jet)
   7. mavis-3-mini-mini (not jet)

2. MAVIS Terminal 3 EAP:
   1. mavis-terminal-3

3. MAVIS 3 EAP fast start:
   1. mavis-3-main-fast
   2. mavis-3-code-fast
   3. mavis-3-code-pro-fast (not jet)
   4. mavis-3-math-fast
   5. mavis-3-math-pro-fast (not jet)
   6. mavis-3-mini-fast (not jet)
   7. mavis-3-mini-mini-fast (not jet)

Enter a MAVIS batch file (e.g. 'mavis-3-code'):
```

If you are launching MAVIS 3 for the first time, the installation process may take between **10 to 30 minutes**, depending on your internet speed. If MAVIS is already installed, the program will start in approximately **5 seconds**.  

Regardless of the installation state, the system will always perform a **completeness check** and apply updates if necessary.

If you are starting **MAVIS 3 for the first time**, please **do not select** the **"3. MAVIS 3 EAP Fast Start"** option. Instead, choose one of the following:  

- **"1. MAVIS 3 EAP"**  
- **"2. MAVIS Terminal 3 EAP"** *(Recommended for experienced users only. More information: [MAVIS Terminal Guide](https://github.com/Peharge/MAVIS/blob/main/learn-mavis/learn-mavis-terminal-3.md))*

After entering the desired MAVIS version, such as `"mavis-3-code"`, the specified program will launch automatically.  

```bash
Enter a MAVIS batch file (e.g. 'mavis-3-code'):mavis-3-code
Executing file: C:\Users\julia\PycharmProjects\MAVIS\run-mavis-3-code.bat

      ██╗     █╗
     ████╗   ███╗        ███╗   ███╗ █████╗ ██╗   ██╗██╗███████╗    ██████╗      ██████╗ ██████╗ ██████╗ ███████╗
    ██████╗  ████╗       ████╗ ████║██╔══██╗██║   ██║██║██╔════╝    ╚════██╗    ██╔════╝██╔═══██╗██╔══██╗██╔════╝
   ████████╗  ████╗      ██╔████╔██║███████║██║   ██║██║███████╗     █████╔╝    ██║     ██║   ██║██║  ██║█████╗
  ████╔█████╗  ████╗     ██║╚██╔╝██║██╔══██║╚██╗ ██╔╝██║╚════██║     ╚═══██╗    ██║     ██║   ██║██║  ██║██╔══╝
 ████╔╝ █████╗  ████╗    ██║ ╚═╝ ██║██║  ██║ ╚████╔╝ ██║███████║    ██████╔╝    ╚██████╗╚██████╔╝██████╔╝███████╗
 ╚═══╝   ███╔╝  ╚═══╝    ╚═╝     ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚═╝╚══════╝    ╚═════╝      ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝
          █╔╝
          ╚╝

A warm welcome, Mr.X, to MAVIS (MAth Visual Intelligent System) - the most powerful calculator in the world!
Developed by Peharge and JK (Peharge Projects 2025)
Thank you so much for using MAVIS. We truly appreciate your support ❤️

MAVIS Version: 3
MAVIS Installer Version: 3
MAVIS Terminal Version: 3
MAVIS License: MIT

████████
████████

Framework Information:
----------------------
Do you want to install or update the required Python frameworks for MAVIS? [y/n]:
```

## 2. Installing the required frameworks
Once the terminal is opened, a list of Python frameworks required for MAVIS will appear. These frameworks allow MAVIS to perform various tasks. You can also use them later in Jupyter Notebook, as MAVIS runs in its own Python environment.

For example, the output might look like this:

```bash
Framework Information:
----------------------
Do you want to install or update the required Python frameworks for MAVIS? [y/n]:y

Flask - Lightweight web framework for Python.
Ollama - Tool for integrating with AI APIs.
Jupyter - Open source web application for live code, equations, visualizations and text.
etc.
```

You will also see the following message reminding you that you should update PIP occasionally:

```bash
Dont forget to update PIP regularly with the command: python -m pip install --upgrade pip.
```

If not already done, the required frameworks will now be installed and updated:

```bash
All frameworks for MAVIS versions 1.2, 1.3, 1.4 and 1.5 are currently being installed and updated:
```

If you are starting MAVIS for the first time, you will need to confirm that each framework should be installed. Enter `y` or `yes` to start the installation:

```bash
Would you like to install Flask? [y/n]:
```

Please always confirm with `y` or `yes` to avoid later problems. The same applies to future automatic updates of the frameworks.

## 3. Updating MAVIS
After installing the frameworks, you will be asked if you want to update MAVIS. The latest version will be downloaded from GitHub. The automatic update is usually stable, but errors can occur. If you experience problems, use this command manually:

```bash
git pull https://github.com/Peharge/MAVIS.git
```

The update query looks like this:

```bash
MAVIS Repository Update (experimental):
--------------------------------------
This update function is not yet 100% reliable and errors may occur.
We therefore recommend using the command:
git pull https://github.com/Peharge/MAVIS.git
instead.

MAVIS - Last update: 01/30/2025
Would you like to perform an update? [y/n]:
```

## 4. Installation of additional AI models
After the update, two AI models must be installed. These must each be confirmed with `y` or `yes`.

Some system information will then appear that does not necessarily need to be understood in order to use MAVIS.

## 5. Starting Jupyter Notebook
After a short while, another terminal will open, asking you if you want to open Jupyter Notebook. Jupyter Notebook is a code editor that runs in the browser and is installed with MAVIS.

```bash
Do you want to start Jupyter Notebook? [y/n]:
```

If you enter `y` or `yes`, Jupyter Notebook will open in the browser.

Regardless of this selection, MAVIS will automatically open in a browser tab. If the browser has not started, a connection error may be displayed. This is because the MAVIS server needs a little longer to start up than the browser. In this case, wait 15-30 seconds and refresh the tab. The first start may take a little longer depending on the PC performance.

After the successful start, your browser should look like this:

![MAVIS](./readme-img/using-img-1.png)

## 6. Using MAVIS
You can now send questions to the chatbot, upload images and use the control panel.

![Using MAVIS](./readme-img/using-img-2.png)

Once you have uploaded an image, a small window will appear with the image. Simply click on the window to close it.

If you want to ask the chatbot to create a graph, tell it to use one of the following frameworks:
- Matplotlib
- Plotly
- Seaborn
- Altair

MAVIS also supports LaTeX for mathematical formulas and can perform calculations directly.

Here is an example of MAVIS in operation:

![MAVIS example](./readme-img/mavis-1-5-demo-3.png)

![MAVIS example](./readme-img/mavis-1-5-demo-4.png)

![MAVIS example](./readme-img/mavis-1-5-demo-5.png)

By default, the formula editor is open, which you can use to draw formulas. The drawn formulas are converted to LaTeX code in the input box below and displayed correctly rendered directly below. To convert the formula, simply press the black play button in the drawing box.

The input box in which the LaTeX code is written is connected to the lower input box in the taskbar and can be used as input for the AI-Chatbot.

![Formula editor use](./readme-img/mavis-1-5-use-gif-1.gif)

To close the formula editor, press the pen button in the main taskbar.

![Formula editor usage](./readme-img/mavis-1-5-use-gif-2.gif)

You can also use the graph editor to display formulas in a 2D or 3D coordinate system.

![Graph editor](./readme-img/using-img-4.png)

Enter your formula and use the "Select" function to select special characters, pre-defined formulas, operations (derivation and integration) and the display as a 2D or 3D diagram (2D by default). The formula is displayed in real time.

![Formula display](./readme-img/using-img-5.png)

You can close this window at any time by clicking on the corresponding icon in the taskbar again.

<div align="center">
<img src="./readme-img/using-img-6.png" alt="pen-button" width="600">
</div>

Have fun with MAVIS! Over time, you will get used to using the chatbot. Always give the chatbot a clear role, e.g.: "You are a professional programmer and your job is [...] - get to work!"