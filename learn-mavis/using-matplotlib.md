### Matplotlib tutorial

#### Nicolas P. Rougier

[![DOI](https://zenodo.org/badge/doi/10.5281/zenodo.28747.svg)](http://dx.doi.org/10.5281/zenodo.28747)

#### Table of Contents

- [Introduction](#introduction)
- [IPython](#ipython)
- [pyplot](#pyplot)
- [Simple plot](#simple-plot)
- [Using defaults](#using-defaults)
- [Instantiating defaults](#instantiating-defaults)
- [Changing colors and line widths](#changing-colors-and-line-widths)

Sources are available from [GitHub](https://github.com/rougier/matplotlib-tutorial)

All code and material is licensed under a [Creative Commons Attribution-ShareAlike 4.0](http://creativecommons.org/licenses/by-sa/4.0/).

You can test your installation before the tutorial using the [`check-installation.py`](scripts/check-installation.py) script.

See also:

- [From Python to Numpy](http://www.labri.fr/perso/nrougier/from-python-to-numpy/)
- [100 Numpy exercises](https://github.com/rougier/numpy-100)
- [Ten simple rules for better figures](http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003833)

### Introduction

Matplotlib is probably the single most used Python package for 2D-graphics. It provides both a very quick way to visualize data from Python and publication-quality figures in many formats. We are going to explore Matplotlib in interactive mode covering most common cases.

### IPython

[IPython](http://ipython.org/) is an enhanced interactive Python shell that has lots of interesting features including named inputs and outputs, access to shell commands, improved debugging, and much more. It allows interactive Matplotlib sessions that have Matlab/Mathematica-like functionality.

### pyplot

Pyplot provides a convenient interface to the Matplotlib object-oriented plotting library. It is modeled closely after Matlab(TM). Therefore, the majority of plotting commands in Pyplot have Matlab(TM) analogs with similar arguments. Important commands are explained with interactive examples.

### Simple plot

In this section, we want to draw the cosine and sine functions on the same plot. Starting from the default settings, we'll enrich the figure step by step to make it nicer.

The first step is to get the data for the sine and cosine functions:

```python
import numpy as np

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)
```

X is now a NumPy array with 256 values ranging from -π to +π (included). C is the cosine (256 values) and S is the sine (256 values).

To run the example, you can download each of the examples and run it using:

```sh
$ python exercice_1.py
```

You can get the source for each step by clicking on the corresponding figure.

### Using defaults

#### Documentation

- [Plot tutorial](http://matplotlib.sourceforge.net/users/pyplot_tutorial.html)
- [plot() command](http://matplotlib.sourceforge.net/api/pyplot_api.html#matplotlib.pyplot.plot)

![Example 1](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/exercice_1.png)

Matplotlib comes with a set of default settings that allow customizing all kinds of properties. You can control the defaults of almost every property in Matplotlib: figure size and DPI, line width, color and style, axes, axis and grid properties, text and font properties, and so on. While Matplotlib defaults are rather good in most cases, you may want to modify some properties for specific cases.

```python
# Content from scripts/exercice_1.py
```

### Instantiating defaults

#### Documentation

- [Customizing Matplotlib](http://matplotlib.sourceforge.net/users/customizing.html)

![Example 2](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/exercice_2.png)

In the script below, we've instantiated (and commented) all the figure settings that influence the appearance of the plot. The settings have been explicitly set to their default values, but now you can interactively play with the values to explore their effect.

```python
# Content from scripts/exercice_2.py
```

### Changing colors and line widths

#### Documentation

- [Controlling line properties](http://matplotlib.sourceforge.net/users/pyplot_tutorial.html#controlling-line-properties)
- [Line API](http://matplotlib.sourceforge.net/api/artist_api.html#matplotlib.lines.Line2D)

![Example 3](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/exercice_3.png)

As a first step, we want to have the cosine in blue and the sine in red and a slightly thicker line for both of them. We'll also slightly alter the figure size to make it more horizontal.

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6), dpi=80)
plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-")
plt.plot(X, S, color="red", linewidth=2.5, linestyle="-")
plt.show()
```

### Matplotlib tutorial

#### Nicolas P. Rougier

[![DOI](https://zenodo.org/badge/doi/10.5281/zenodo.28747.svg)](http://dx.doi.org/10.5281/zenodo.28747)

#### Table of Contents

- [Introduction](#introduction)
- [IPython](#ipython)
- [pyplot](#pyplot)
- [Simple plot](#simple-plot)
- [Using defaults](#using-defaults)
- [Instantiating defaults](#instantiating-defaults)
- [Changing colors and line widths](#changing-colors-and-line-widths)
- [Setting limits](#setting-limits)
- [Setting ticks](#setting-ticks)
- [Setting tick labels](#setting-tick-labels)
- [Moving spines](#moving-spines)

Sources are available from [GitHub](https://github.com/rougier/matplotlib-tutorial)

All code and material is licensed under a [Creative Commons Attribution-ShareAlike 4.0](http://creativecommons.org/licenses/by-sa/4.0/).

You can test your installation before the tutorial using the [`check-installation.py`](scripts/check-installation.py) script.

See also:

- [From Python to Numpy](http://www.labri.fr/perso/nrougier/from-python-to-numpy/)
- [100 Numpy exercises](https://github.com/rougier/numpy-100)
- [Ten simple rules for better figures](http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003833)

### Setting limits

#### Documentation

- [xlim() command](http://matplotlib.sourceforge.net/api/pyplot_api.html#matplotlib.pyplot.xlim)
- [ylim() command](http://matplotlib.sourceforge.net/api/pyplot_api.html#matplotlib.pyplot.ylim)

![Example 4](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/exercice_4.png)

Current limits of the figure are a bit too tight and we want to make some space in order to clearly see all data points.

```python
plt.xlim(X.min()*1.1, X.max()*1.1)
plt.ylim(C.min()*1.1, C.max()*1.1)
```

### Setting ticks

#### Documentation

- [xticks() command](http://matplotlib.sourceforge.net/api/pyplot_api.html#matplotlib.pyplot.xticks)
- [yticks() command](http://matplotlib.sourceforge.net/api/pyplot_api.html#matplotlib.pyplot.yticks)
- [Tick container](http://matplotlib.sourceforge.net/users/artists.html#axis-container)
- [Tick locating and formatting](http://matplotlib.sourceforge.net/api/ticker_api.html)

![Example 5](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/exercice_5.png)

Current ticks are not ideal because they do not show the interesting values (+/-π, +/-π/2) for sine and cosine. We'll change them such that they show only these values.

```python
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
plt.yticks([-1, 0, +1])
```

### Setting tick labels

#### Documentation

- [Working with text](http://matplotlib.sourceforge.net/users/index_text.html)
- [xticks() command](http://matplotlib.sourceforge.net/api/pyplot_api.html#matplotlib.pyplot.xticks)
- [yticks() command](http://matplotlib.sourceforge.net/api/pyplot_api.html#matplotlib.pyplot.yticks)
- [set_xticklabels()](http://matplotlib.sourceforge.net/api/axes_api.html?#matplotlib.axes.Axes.set_xticklabels)
- [set_yticklabels()](http://matplotlib.sourceforge.net/api/axes_api.html?#matplotlib.axes.Axes.set_yticklabels)

![Example 6](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/exercice_6.png)

Ticks are now properly placed but their label is not very explicit. We could guess that 3.142 is π but it would be better to make it explicit. When we set tick values, we can also provide a corresponding label in the second argument list. Note that we'll use LaTeX to allow for nice rendering of the label.

```python
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
           [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

plt.yticks([-1, 0, +1],
           [r'$-1$', r'$0$', r'$+1$'])
```

### Moving spines

#### Documentation

- [Spines](http://matplotlib.sourceforge.net/api/spines_api.html#matplotlib.spines)
- [Axis container](http://matplotlib.sourceforge.net/users/artists.html#axis-container)
- [Transformations tutorial](http://matplotlib.sourceforge.net/users/transforms_tutorial.html)

![Example 7](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/exercice_7.png)

Spines are the lines connecting the axis tick marks and noting the boundaries of the data area. They can be placed at arbitrary positions and until now, they were on the border of the axis. We'll change that since we want to have them in the middle. Since there are four of them (top/bottom/left/right), we'll discard the top and right by setting their color to none and we'll move the bottom and left ones to coordinate 0 in data space coordinates.

```python
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))
```

Adding a legend
---------------

Matplotlib bietet eine Legende, die in der oberen linken Ecke platziert werden kann. Dafür müssen wir das Schlüsselwort `label` in den `plot`-Befehlen verwenden und anschließend `plt.legend()` aufrufen.

```python
plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-", label="cosine")
plt.plot(X, S, color="red", linewidth=2.5, linestyle="-", label="sine")

plt.legend(loc='upper left', frameon=False)
```

Annotate some points
--------------------

Wir können interessante Punkte mit der `annotate`-Funktion markieren. Im folgenden Beispiel annotieren wir den Wert 2π/3 sowohl für Sinus als auch für Kosinus.

```python
t = 2*np.pi/3
plt.plot([t,t],[0,np.cos(t)], color ='blue', linewidth=1.5, linestyle="--")
plt.scatter([t,],[np.cos(t),], 50, color ='blue')

plt.annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
             xy=(t, np.sin(t)), xycoords='data',
             xytext=(+10, +30), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

plt.plot([t,t],[0,np.sin(t)], color ='red', linewidth=1.5, linestyle="--")
plt.scatter([t,],[np.sin(t),], 50, color ='red')

plt.annotate(r'$\cos(\frac{2\pi}{3})=-\frac{1}{2}$',
             xy=(t, np.cos(t)), xycoords='data',
             xytext=(-90, -50), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
```

Devil is in the details
------------------------

Um die Lesbarkeit der Achsenbeschriftungen zu verbessern, können wir ihre Größe anpassen und ihnen eine halbtransparente Hintergrundfarbe geben.

```python
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(16)
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.65 ))
```

Figures, Subplots, Axes und Ticks
=================================

Bisher haben wir implizite Figuren und Achsen verwendet. Matplotlib erlaubt jedoch auch explizite Steuerung über `figure`, `subplot` und `axes`. Eine `figure` repräsentiert das gesamte Fenster, während `subplot` die Plots in einem regulären Raster anordnet. `axes` ermöglicht eine freie Platzierung.

Figures
-------

Ein `figure`-Objekt ist das Fenster in der GUI mit "Figure #" als Titel. Figuren sind nummeriert ab 1, ähnlich wie in MATLAB. Es gibt mehrere Parameter, die das Erscheinungsbild beeinflussen:

| Argument   | Standardwert           | Beschreibung                           |
|------------|------------------------|----------------------------------------|
| num        | 1                      | Nummer der Figur                      |
| figsize    | figure.figsize         | Größe der Figur (Breite, Höhe in Zoll) |
| dpi        | figure.dpi             | Auflösung in dpi                      |
| facecolor  | figure.facecolor       | Hintergrundfarbe                       |
| edgecolor  | figure.edgecolor       | Rahmenfarbe                            |
| frameon    | True                   | Rahmen zeichnen oder nicht            |

Standardwerte können in der Konfigurationsdatei gesetzt werden. Man kann eine Figur schließen, indem man auf das "X" im GUI klickt oder programmatisch über `close()`.

```python
plt.close()       # Schließt die aktuelle Figur
plt.close(1)      # Schließt eine spezifische Figur
plt.close('all')  # Schließt alle Figuren
```

Wie andere Objekte können `figure`-Eigenschaften mit den `set_something`-Methoden angepasst werden.

Adding a legend
---------------

Matplotlib bietet eine Legende, die in der oberen linken Ecke platziert werden kann. Dafür müssen wir das Schlüsselwort `label` in den `plot`-Befehlen verwenden und anschließend `plt.legend()` aufrufen.

```python
plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-", label="cosine")
plt.plot(X, S, color="red", linewidth=2.5, linestyle="-", label="sine")

plt.legend(loc='upper left', frameon=False)
```

Annotate some points
--------------------

Wir können interessante Punkte mit der `annotate`-Funktion markieren. Im folgenden Beispiel annotieren wir den Wert 2π/3 sowohl für Sinus als auch für Kosinus.

```python
t = 2*np.pi/3
plt.plot([t,t],[0,np.cos(t)], color ='blue', linewidth=1.5, linestyle="--")
plt.scatter([t,],[np.cos(t),], 50, color ='blue')

plt.annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
             xy=(t, np.sin(t)), xycoords='data',
             xytext=(+10, +30), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

plt.plot([t,t],[0,np.sin(t)], color ='red', linewidth=1.5, linestyle="--")
plt.scatter([t,],[np.sin(t),], 50, color ='red')

plt.annotate(r'$\cos(\frac{2\pi}{3})=-\frac{1}{2}$',
             xy=(t, np.cos(t)), xycoords='data',
             xytext=(-90, -50), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
```

Devil is in the details
------------------------

Um die Lesbarkeit der Achsenbeschriftungen zu verbessern, können wir ihre Größe anpassen und ihnen eine halbtransparente Hintergrundfarbe geben.

```python
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(16)
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.65 ))
```

Figures, Subplots, Axes und Ticks
=================================

Bisher haben wir implizite Figuren und Achsen verwendet. Matplotlib erlaubt jedoch auch explizite Steuerung über `figure`, `subplot` und `axes`. Eine `figure` repräsentiert das gesamte Fenster, während `subplot` die Plots in einem regulären Raster anordnet. `axes` ermöglicht eine freie Platzierung.

Figures
-------

Ein `figure`-Objekt ist das Fenster in der GUI mit "Figure #" als Titel. Figuren sind nummeriert ab 1, ähnlich wie in MATLAB. Es gibt mehrere Parameter, die das Erscheinungsbild beeinflussen:

| Argument   | Standardwert           | Beschreibung                           |
|------------|------------------------|----------------------------------------|
| num        | 1                      | Nummer der Figur                      |
| figsize    | figure.figsize         | Größe der Figur (Breite, Höhe in Zoll) |
| dpi        | figure.dpi             | Auflösung in dpi                      |
| facecolor  | figure.facecolor       | Hintergrundfarbe                       |
| edgecolor  | figure.edgecolor       | Rahmenfarbe                            |
| frameon    | True                   | Rahmen zeichnen oder nicht            |

Standardwerte können in der Konfigurationsdatei gesetzt werden. Man kann eine Figur schließen, indem man auf das "X" im GUI klickt oder programmatisch über `close()`.

```python
plt.close()       # Schließt die aktuelle Figur
plt.close(1)      # Schließt eine spezifische Figur
plt.close('all')  # Schließt alle Figuren
```

Wie andere Objekte können `figure`-Eigenschaften mit den `set_something`-Methoden angepasst werden.

Subplots
--------

Mit `subplot` können Plots in einem regulären Raster angeordnet werden. Man gibt die Anzahl der Zeilen und Spalten sowie die Nummer des Plots an.

```python
plt.subplot(2, 1, 1)  # Erstes Subplot (2 Zeilen, 1 Spalte, erstes Plot)
plt.plot(X, C)

plt.subplot(2, 1, 2)  # Zweites Subplot (2 Zeilen, 1 Spalte, zweites Plot)
plt.plot(X, S)
```

Axes
----

`Axes` ermöglichen eine freie Platzierung von Plots innerhalb einer Figur.

```python
fig = plt.figure()
ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])  # Große Achse
ax2 = fig.add_axes([0.5, 0.5, 0.3, 0.3])  # Kleine Achse innerhalb der großen

ax1.plot(X, C)
ax2.plot(X, S)
```

Ticks
-----

Ticks können mit verschiedenen `Locator`-Methoden formatiert werden.

```python
import matplotlib.ticker as ticker
ax.xaxis.set_major_locator(ticker.MultipleLocator(np.pi/2))
ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda val, pos: f'{val/np.pi:.1f}π'))
```
Adding a legend
---------------

Matplotlib bietet eine Legende, die in der oberen linken Ecke platziert werden kann. Dafür müssen wir das Schlüsselwort `label` in den `plot`-Befehlen verwenden und anschließend `plt.legend()` aufrufen.

```python
plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-", label="cosine")
plt.plot(X, S, color="red", linewidth=2.5, linestyle="-", label="sine")

plt.legend(loc='upper left', frameon=False)
```

Annotate some points
--------------------

Wir können interessante Punkte mit der `annotate`-Funktion markieren. Im folgenden Beispiel annotieren wir den Wert 2π/3 sowohl für Sinus als auch für Kosinus.

```python
t = 2*np.pi/3
plt.plot([t,t],[0,np.cos(t)], color ='blue', linewidth=1.5, linestyle="--")
plt.scatter([t,],[np.cos(t),], 50, color ='blue')

plt.annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
             xy=(t, np.sin(t)), xycoords='data',
             xytext=(+10, +30), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

plt.plot([t,t],[0,np.sin(t)], color ='red', linewidth=1.5, linestyle="--")
plt.scatter([t,],[np.sin(t),], 50, color ='red')

plt.annotate(r'$\cos(\frac{2\pi}{3})=-\frac{1}{2}$',
             xy=(t, np.cos(t)), xycoords='data',
             xytext=(-90, -50), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
```

Devil is in the details
------------------------

Um die Lesbarkeit der Achsenbeschriftungen zu verbessern, können wir ihre Größe anpassen und ihnen eine halbtransparente Hintergrundfarbe geben.

```python
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(16)
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.65 ))
```

Figures, Subplots, Axes und Ticks
=================================

Bisher haben wir implizite Figuren und Achsen verwendet. Matplotlib erlaubt jedoch auch explizite Steuerung über `figure`, `subplot` und `axes`. Eine `figure` repräsentiert das gesamte Fenster, während `subplot` die Plots in einem regulären Raster anordnet. `axes` ermöglicht eine freie Platzierung.

Figures
-------

Ein `figure`-Objekt ist das Fenster in der GUI mit "Figure #" als Titel. Figuren sind nummeriert ab 1, ähnlich wie in MATLAB. Es gibt mehrere Parameter, die das Erscheinungsbild beeinflussen:

| Argument   | Standardwert           | Beschreibung                           |
|------------|------------------------|----------------------------------------|
| num        | 1                      | Nummer der Figur                      |
| figsize    | figure.figsize         | Größe der Figur (Breite, Höhe in Zoll) |
| dpi        | figure.dpi             | Auflösung in dpi                      |
| facecolor  | figure.facecolor       | Hintergrundfarbe                       |
| edgecolor  | figure.edgecolor       | Rahmenfarbe                            |
| frameon    | True                   | Rahmen zeichnen oder nicht            |

Standardwerte können in der Konfigurationsdatei gesetzt werden. Man kann eine Figur schließen, indem man auf das "X" im GUI klickt oder programmatisch über `close()`.

```python
plt.close()       # Schließt die aktuelle Figur
plt.close(1)      # Schließt eine spezifische Figur
plt.close('all')  # Schließt alle Figuren
```

Wie andere Objekte können `figure`-Eigenschaften mit den `set_something`-Methoden angepasst werden.

Subplots
--------

Mit `subplot` können Plots in einem regulären Raster angeordnet werden. Man gibt die Anzahl der Zeilen und Spalten sowie die Nummer des Plots an.

```python
plt.subplot(2, 1, 1)  # Erstes Subplot (2 Zeilen, 1 Spalte, erstes Plot)
plt.plot(X, C)

plt.subplot(2, 1, 2)  # Zweites Subplot (2 Zeilen, 1 Spalte, zweites Plot)
plt.plot(X, S)
```

Axes
----

`Axes` ermöglichen eine freie Platzierung von Plots innerhalb einer Figur.

```python
fig = plt.figure()
ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])  # Große Achse
ax2 = fig.add_axes([0.5, 0.5, 0.3, 0.3])  # Kleine Achse innerhalb der großen

ax1.plot(X, C)
ax2.plot(X, S)
```

Ticks
-----

Ticks können mit verschiedenen `Locator`-Methoden formatiert werden.

```python
import matplotlib.ticker as ticker
ax.xaxis.set_major_locator(ticker.MultipleLocator(np.pi/2))
ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda val, pos: f'{val/np.pi:.1f}π'))
```

Drip drop
---------

Ein einfacher Regentropfen-Effekt kann mit wachsenden Ringen simuliert werden, die zufällig positioniert werden. Diese Ringe wachsen und verblassen, bis sie verschwinden und durch neue ersetzt werden.

```python
fig = plt.figure(figsize=(6,6), facecolor='white')
ax = fig.add_axes([0,0,1,1], frameon=False, aspect=1)
```

Ringe werden mit einem Scatter-Plot gezeichnet, indem nur die Kantenfarben gesetzt werden.

```python
n = 50
size_min = 50
size_max = 50*50
P = np.random.uniform(0,1,(n,2))
C = np.ones((n,4)) * (0,0,0,1)
C[:,3] = np.linspace(0,1,n)
S = np.linspace(size_min, size_max, n)
scat = ax.scatter(P[:,0], P[:,1], s=S, lw=0.5, edgecolors=C, facecolors='None')
ax.set_xlim(0,1), ax.set_xticks([])
ax.set_ylim(0,1), ax.set_yticks([])
```

Adding a legend
---------------

Matplotlib bietet eine Legende, die in der oberen linken Ecke platziert werden kann. Dafür müssen wir das Schlüsselwort `label` in den `plot`-Befehlen verwenden und anschließend `plt.legend()` aufrufen.

```python
plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-", label="cosine")
plt.plot(X, S, color="red", linewidth=2.5, linestyle="-", label="sine")

plt.legend(loc='upper left', frameon=False)
```

Annotate some points
--------------------

Wir können interessante Punkte mit der `annotate`-Funktion markieren. Im folgenden Beispiel annotieren wir den Wert 2π/3 sowohl für Sinus als auch für Kosinus.

```python
t = 2*np.pi/3
plt.plot([t,t],[0,np.cos(t)], color ='blue', linewidth=1.5, linestyle="--")
plt.scatter([t,],[np.cos(t),], 50, color ='blue')

plt.annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
             xy=(t, np.sin(t)), xycoords='data',
             xytext=(+10, +30), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

plt.plot([t,t],[0,np.sin(t)], color ='red', linewidth=1.5, linestyle="--")
plt.scatter([t,],[np.sin(t),], 50, color ='red')

plt.annotate(r'$\cos(\frac{2\pi}{3})=-\frac{1}{2}$',
             xy=(t, np.cos(t)), xycoords='data',
             xytext=(-90, -50), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
```

Other Types of Plots
====================

Regular Plots
-------------

```python
import numpy as np
import matplotlib.pyplot as plt

n = 256
X = np.linspace(-np.pi,np.pi,n,endpoint=True)
Y = np.sin(2*X)

plt.plot(X, Y+1, color='blue', alpha=1.00)
plt.plot(X, Y-1, color='blue', alpha=1.00)
plt.show()
```

Scatter Plots
-------------

```python
import numpy as np
import matplotlib.pyplot as plt

n = 1024
X = np.random.normal(0,1,n)
Y = np.random.normal(0,1,n)

plt.scatter(X, Y)
plt.show()
```

Bar Plots
---------

```python
import numpy as np
import matplotlib.pyplot as plt

n = 12
X = np.arange(n)
Y1 = (1-X/float(n)) * np.random.uniform(0.5,1.0,n)
Y2 = (1-X/float(n)) * np.random.uniform(0.5,1.0,n)

plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')

for x,y in zip(X,Y1):
    plt.text(x+0.4, y+0.05, '%.2f' % y, ha='center', va='bottom')

plt.ylim(-1.25,+1.25)
plt.show()
```

Figures, Subplots, Axes und Ticks
=================================

Bisher haben wir implizite Figuren und Achsen verwendet. Matplotlib erlaubt jedoch auch explizite Steuerung über `figure`, `subplot` und `axes`. Eine `figure` repräsentiert das gesamte Fenster, während `subplot` die Plots in einem regulären Raster anordnet. `axes` ermöglicht eine freie Platzierung.

Figures
-------

Ein `figure`-Objekt ist das Fenster in der GUI mit "Figure #" als Titel. Figuren sind nummeriert ab 1, ähnlich wie in MATLAB. Es gibt mehrere Parameter, die das Erscheinungsbild beeinflussen:

| Argument   | Standardwert           | Beschreibung                           |
|------------|------------------------|----------------------------------------|
| num        | 1                      | Nummer der Figur                      |
| figsize    | figure.figsize         | Größe der Figur (Breite, Höhe in Zoll) |
| dpi        | figure.dpi             | Auflösung in dpi                      |
| facecolor  | figure.facecolor       | Hintergrundfarbe                       |
| edgecolor  | figure.edgecolor       | Rahmenfarbe                            |
| frameon    | True                   | Rahmen zeichnen oder nicht            |

Standardwerte können in der Konfigurationsdatei gesetzt werden. Man kann eine Figur schließen, indem man auf das "X" im GUI klickt oder programmatisch über `close()`.

```python
plt.close()       # Schließt die aktuelle Figur
plt.close(1)      # Schließt eine spezifische Figur
plt.close('all')  # Schließt alle Figuren
```

Wie andere Objekte können `figure`-Eigenschaften mit den `set_something`-Methoden angepasst werden.

Subplots
--------

Mit `subplot` können Plots in einem regulären Raster angeordnet werden. Man gibt die Anzahl der Zeilen und Spalten sowie die Nummer des Plots an.

```python
plt.subplot(2, 1, 1)  # Erstes Subplot (2 Zeilen, 1 Spalte, erstes Plot)
plt.plot(X, C)

plt.subplot(2, 1, 2)  # Zweites Subplot (2 Zeilen, 1 Spalte, zweites Plot)
plt.plot(X, S)
```

Axes
----

`Axes` ermöglichen eine freie Platzierung von Plots innerhalb einer Figur.

```python
fig = plt.figure()
ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])  # Große Achse
ax2 = fig.add_axes([0.5, 0.5, 0.3, 0.3])  # Kleine Achse innerhalb der großen

ax1.plot(X, C)
ax2.plot(X, S)
```

Ticks
-----

Ticks können mit verschiedenen `Locator`-Methoden formatiert werden.

```python
import matplotlib.ticker as ticker
ax.xaxis.set_major_locator(ticker.MultipleLocator(np.pi/2))
ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda val, pos: f'{val/np.pi:.1f}π'))
```
Adding a legend
---------------

Matplotlib bietet eine Legende, die in der oberen linken Ecke platziert werden kann. Dafür müssen wir das Schlüsselwort `label` in den `plot`-Befehlen verwenden und anschließend `plt.legend()` aufrufen.

```python
plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-", label="cosine")
plt.plot(X, S, color="red", linewidth=2.5, linestyle="-", label="sine")

plt.legend(loc='upper left', frameon=False)
```

Annotate some points
--------------------

Wir können interessante Punkte mit der `annotate`-Funktion markieren. Im folgenden Beispiel annotieren wir den Wert 2π/3 sowohl für Sinus als auch für Kosinus.

```python
t = 2*np.pi/3
plt.plot([t,t],[0,np.cos(t)], color ='blue', linewidth=1.5, linestyle="--")
plt.scatter([t,],[np.cos(t),], 50, color ='blue')

plt.annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
             xy=(t, np.sin(t)), xycoords='data',
             xytext=(+10, +30), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

plt.plot([t,t],[0,np.sin(t)], color ='red', linewidth=1.5, linestyle="--")
plt.scatter([t,],[np.sin(t),], 50, color ='red')

plt.annotate(r'$\cos(\frac{2\pi}{3})=-\frac{1}{2}$',
             xy=(t, np.cos(t)), xycoords='data',
             xytext=(-90, -50), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
```

Other Types of Plots
====================

Regular Plots
-------------

```python
import numpy as np
import matplotlib.pyplot as plt

n = 256
X = np.linspace(-np.pi,np.pi,n,endpoint=True)
Y = np.sin(2*X)

plt.plot(X, Y+1, color='blue', alpha=1.00)
plt.plot(X, Y-1, color='blue', alpha=1.00)
plt.show()
```

Scatter Plots
-------------

```python
import numpy as np
import matplotlib.pyplot as plt

n = 1024
X = np.random.normal(0,1,n)
Y = np.random.normal(0,1,n)

plt.scatter(X, Y)
plt.show()
```

Bar Plots
---------

```python
import numpy as np
import matplotlib.pyplot as plt

n = 12
X = np.arange(n)
Y1 = (1-X/float(n)) * np.random.uniform(0.5,1.0,n)
Y2 = (1-X/float(n)) * np.random.uniform(0.5,1.0,n)

plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')

for x,y in zip(X,Y1):
    plt.text(x+0.4, y+0.05, '%.2f' % y, ha='center', va='bottom')

plt.ylim(-1.25,+1.25)
plt.show()
```

Contour Plots
-------------

```python
import numpy as np
import matplotlib.pyplot as plt

def f(x,y): return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)

n = 256
x = np.linspace(-3,3,n)
y = np.linspace(-3,3,n)
X,Y = np.meshgrid(x,y)

plt.contourf(X, Y, f(X,Y), 8, alpha=.75, cmap='jet')
C = plt.contour(X, Y, f(X,Y), 8, colors='black', linewidths=0.5)
plt.show()
```

Imshow
------

```python
import numpy as np
import matplotlib.pyplot as plt

def f(x,y): return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)

n = 10
x = np.linspace(-3,3,4*n)
y = np.linspace(-3,3,3*n)
X,Y = np.meshgrid(x,y)
plt.imshow(f(X,Y), origin='lower', cmap='hot', interpolation='bilinear')
plt.colorbar()
plt.show()
```

Pie Charts
----------

```python
import numpy as np
import matplotlib.pyplot as plt

n = 20
Z = np.random.uniform(0,1,n)
plt.pie(Z)
plt.show()
```

Quiver Plots
------------

```python
import numpy as np
import matplotlib.pyplot as plt

n = 8
X,Y = np.mgrid[0:n,0:n]
plt.quiver(X,Y)
plt.show()
```

Grids
-----

```python
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.set_xlim(0,4)
ax.set_ylim(0,3)
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.grid(True)
plt.show()
```

Multi Plots
-----------

```python
import numpy as np
import matplotlib.pyplot as plt

plt.subplot(2,2,1)
plt.subplot(2,2,3)
plt.subplot(2,2,4)

plt.show()
```

Polar Axis
----------

```python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

plt.subplot(111, polar=True)

N = 20
theta = np.linspace(0.0, 2*np.pi, N, endpoint=False)
radii = 10*np.random.rand(N)
width = np.pi/4*np.random.rand(N)
bars = plt.bar(theta, radii, width=width, bottom=0.0)

for r,bar in zip(radii, bars):
    bar.set_facecolor(cm.jet(r/10.))
    bar.set_alpha(0.5)

plt.show()
```

3D Plots
--------

```python
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='hot')
plt.show()
```

# Text

![Text Example](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/text_ex.png)

> **Hints**  
> Have a look at the [matplotlib logo](http://matplotlib.sourceforge.net/examples/api/logo2.html).
>
> Try to do the same from scratch!
>
> Click on the figure for the solution.

## Beyond this tutorial

Matplotlib benefits from extensive documentation as well as a large community of users and developers. Here are some links of interest:

### Tutorials

- [Pyplot tutorial](http://matplotlib.sourceforge.net/users/pyplot_tutorial.html)
  - Introduction
  - Controlling line properties
  - Working with multiple figures and axes
  - Working with text

- [Image tutorial](http://matplotlib.sourceforge.net/users/image_tutorial.html)
  - Startup commands
  - Importing image data into Numpy arrays
  - Plotting numpy arrays as images

- [Text tutorial](http://matplotlib.sourceforge.net/users/index_text.html)
  - Text introduction
  - Basic text commands
  - Text properties and layout
  - Writing mathematical expressions
  - Text rendering with LaTeX
  - Annotating text

- [Artist tutorial](http://matplotlib.sourceforge.net/users/artists.html)
  - Introduction
  - Customizing your objects
  - Object containers
  - Figure container
  - Axes container
  - Axis containers
  - Tick containers

- [Path tutorial](http://matplotlib.sourceforge.net/users/path_tutorial.html)
  - Introduction
  - Bézier example
  - Compound paths

- [Transforms tutorial](http://matplotlib.sourceforge.net/users/transforms_tutorial.html)
  - Introduction
  - Data coordinates
  - Axes coordinates
  - Blended transformations
  - Using offset transforms to create a shadow effect
  - The transformation pipeline

## Matplotlib documentation

- [User guide](http://matplotlib.sourceforge.net/users/index.html)
- [FAQ](http://matplotlib.sourceforge.net/faq/index.html)
  - Installation
  - Usage
  - How-To
  - Troubleshooting
  - Environment Variables
- [Screenshots](http://matplotlib.sourceforge.net/users/screenshots.html)

## Code documentation

The code is fairly well documented and you can quickly access a specific command from within a Python session:

```python
>>> import matplotlib.pyplot as plt
>>> help(plt)
Help on function plot in module matplotlib.pyplot:

plot(*args, **kwargs)
   Plot lines and/or markers to the
   :class:`~matplotlib.axes.Axes`.  *args* is a variable length
   argument, allowing for multiple *x*, *y* pairs with an
   optional format string.  For example, each of the following is
   legal::

       plot(x, y)         # plot x and y using default line style and color
       plot(x, y, 'bo')   # plot x and y using blue circle markers
       plot(y)            # plot y using x as index array 0..N-1
       plot(y, 'r+')      # ditto, but with red plusses

   If *x* and/or *y* is 2-dimensional, then the corresponding columns
   will be plotted.
 ```

## Galleries

The [matplotlib gallery](http://matplotlib.sourceforge.net/gallery.html) is also incredibly useful when you search for how to render a given graphic. Each example comes with its source.

## Mailing lists

Finally, there is a [user mailing list](https://mail.python.org/mailman/listinfo/matplotlib-users) where you can ask for help and a [developers mailing list](https://mail.python.org/mailman/listinfo/matplotlib-devel) that is more technical.

# Quick references

Here is a set of tables that show main properties and styles.

## Line properties

| Property                | Description                                    | Appearance                              |
|-------------------------|------------------------------------------------|-----------------------------------------|
| **alpha (or a)**         | alpha transparency on 0-1 scale                | ![alpha](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/alpha.png)             |
| **antialiased**          | True or False - use antialiased rendering      | ![aliased](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/aliased.png) ![antialiased](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/antialiased.png) |
| **color (or c)**         | matplotlib color arg                           | ![color](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/color.png)             |
| **linestyle (or ls)**    | see `Line properties`                          |                                         |
| **linewidth (or lw)**    | float, the line width in points                | ![linewidth](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/linewidth.png)     |
| **solid_capstyle**       | Cap style for solid lines                      | ![solid_capstyle](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/solid_capstyle.png) |
| **solid_joinstyle**      | Join style for solid lines                     | ![solid_joinstyle](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/solid_joinstyle.png) |
| **dash_capstyle**        | Cap style for dashes                           | ![dash_capstyle](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/dash_capstyle.png) |
| **dash_joinstyle**       | Join style for dashes                          | ![dash_joinstyle](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/dash_joinstyle.png) |
| **marker**               | see `Markers`                                  |                                         |
| **markeredgewidth (mew)**| line width around the marker symbol            | ![mew](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/mew.png)                 |
| **markeredgecolor (mec)**| edge color if a marker is used                 | ![mec](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/mec.png)                 |
| **markerfacecolor (mfc)**| face color if a marker is used                 | ![mfc](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/mfc.png)                 |
| **markersize (ms)**      | size of the marker in points                   | ![ms](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/ms.png)                   |

## Line styles

| Symbol | Description   | Appearance                              |
|--------|---------------|-----------------------------------------|
| `-`    | solid line    | ![solid line](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/linestyle--.png)  |
| `--`   | dashed line   | ![dashed line](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/linestyle---.png)|
| `-.`   | dash-dot line | ![dash-dot line](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/linestyle--dot.png)|
| `:`    | dotted line   | ![dotted line](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/linestyle-:.png) |
| `.`    | points        | ![points](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/linestyle-dot.png)    |
| `,`    | pixels        | ![pixels](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/linestyle-,.png)      |
| `o`    | circle        | ![circle](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/linestyle-o.png)      |
| `^`    | triangle up   | ![triangle up](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/linestyle-^.png) |
| `v`    | triangle down | ![triangle down](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/linestyle-v.png)|
| `<`    | triangle left | ![triangle left](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/linestyle-<.png)|
| `>`    | triangle right| ![triangle right](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/linestyle->.png)|
| `s`    | square        | ![square](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/linestyle-s.png)      |
| `+`    | plus          | ![plus](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/linestyle-+.png)        |
| `x`    | cross         | ![cross](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/linestyle-x.png)       |
| `D`    | diamond       | ![diamond](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/linestyle-dd.png)    |
| `d`    | thin diamond  | ![thin diamond]https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/linestyle-d.png)|
| `1`    | tripod down   | ![tripod down](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/linestyle-1.png) |
| `2`    | tripod up     | ![tripod up](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/linestyle-2.png)   |
| `3`    | tripod left   | ![tripod left](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/linestyle-3.png) |
| `4`    | tripod right  | ![tripod right](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/linestyle-4.png)|
| `h`    | hexagon       | ![hexagon](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/linestyle-h.png)     |
| `H`    | rotated hexagon| ![rotated hexagon](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/linestyle-hh.png)|
| `p`    | pentagon      | ![pentagon](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/linestyle-p.png)    |
| `|`    | vertical line | ![vertical line](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/linestyle-|.png)|
| `_`    | horizontal line| ![horizontal line](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/linestyle-_.png)|

## Markers

| Symbol  | Description    | Appearance                             |
|---------|----------------|----------------------------------------|
| `0`     | tick left      | ![tick left](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/marker-i0.png)    |
| `1`     | tick right     | ![tick right](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/marker-i1.png)   |
| `2`     | tick up        | ![tick up](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/marker-i2.png)      |
| `3`     | tick down      | ![tick down](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/marker-i3.png)    |
| `4`     | caret left     | ![caret left](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/marker-i4.png)   |
| `5`     | caret right    | ![caret right](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/marker-i5.png)  |
| `6`     | caret up       | ![caret up](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/marker-i6.png)     |
| `7`     | caret down     | ![caret down](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/marker-i7.png)   |
| `o`     | circle         | ![circle](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/marker-o.png)        |
| `D`     | diamond        | ![diamond](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/marker-dd.png)      |
| `h`     | hexagon 1      | ![hexagon 1](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/marker-h.png)     |
| `H`     | hexagon 2      | ![hexagon 2](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/marker-hh.png)    |
| `_`     | horizontal line| ![horizontal line](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/marker-_.png)|
| `1`     | tripod down    | ![tripod down](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/marker-1.png)   |
| `2`     | tripod up      | ![tripod up](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/marker-2.png)     |
| `3`     | tripod left    | ![tripod left](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/marker-3.png)   |
| `4`     | tripod right   | ![tripod right](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/marker-4.png)  |
| `8`     | octagon        | ![octagon](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/marker-8.png)       |
| `p`     | pentagon       | ![pentagon](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/marker-p.png)      |
| `^`     | triangle up    | ![triangle up](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/marker-^.png)   |
| `v`     | triangle down  | ![triangle down](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/marker-v.png) |
| `<`     | triangle left  | ![triangle left](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/marker-<.png) |
| `>`     | triangle right | ![triangle right](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/marker->.png) |
| `d`     | thin diamond   | ![thin diamond](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/marker-d.png)  |
| `,`     | pixel          | ![pixel](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/marker-,.png)         |
| `+`     | plus           | ![plus](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/marker-+.png)          |
| `.`     | point          | ![point](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/marker-dot.png)       |
| `s`     | square         | ![square](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/marker-s.png)        |
| `*`     | star           | ![star](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/marker-*.png)          |
| `|`     | vertical line  | ![vertical line](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/marker-|.png)  |
| `x`     | cross          | ![cross](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/marker-x.png)         |
| `r'$\sqrt{2}$'` | any latex expression | ![latex expression](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/marker-latex.png) |

# Colormaps

All colormaps can be reversed by appending `_r`. For instance, `gray_r` is the reverse of `gray`.

If you want to know more about colormaps, see [Documenting the matplotlib colormaps](https://gist.github.com/2719900).

## Base

| Name    | Appearance                     |
|---------|--------------------------------|
| autumn  | ![autumn](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/cmap-autumn.png)  |
| bone    | ![bone](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/cmap-bone.png)      |
| cool    | ![cool](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/cmap-cool.png)      |
| copper  | ![copper](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/cmap-copper.png)  |
| flag    | ![flag](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/cmap-flag.png)      |
| gray    | ![gray](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/cmap-gray.png)      |
| hot     | ![hot](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/cmap-hot.png)        |
| hsv     | ![hsv](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/cmap-hsv.png)        |
| jet     | ![jet](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/cmap-jet.png)        |
| pink    | ![pink](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/cmap-pink.png)      |
| prism   | ![prism](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/cmap-prism.png)    |
| spectral| ![spectral](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/cmap-spectral.png)|
| spring  | ![spring](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/cmap-spring.png)  |
| summer  | ![summer](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/cmap-summer.png)  |
| winter  | ![winter](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/cmap-winter.png)  |

## GIST

| Name          | Appearance                     |
|---------------|--------------------------------|
| gist_earth    | ![gist_earth](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/cmap-gist_earth.png)  |
| gist_gray     | ![gist_gray](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/cmap-gist_gray.png)    |
| gist_heat     | ![gist_heat](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/cmap-gist_heat.png)    |
| gist_ncar     | ![gist_ncar](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/cmap-gist_ncar.png)    |
| gist_rainbow  | ![gist_rainbow](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/cmap-gist_rainbow.png) |
| gist_stern    | ![gist_stern](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/cmap-gist_stern.png)  |
| gist_yarg     | ![gist_yarg](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/cmap-gist_yarg.png)    |

## Diverging

| Name    | Appearance                     |
|---------|--------------------------------|
| BrBG    | ![BrBG](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/cmap-BrBG.png)  |
| PiYG    | ![PiYG](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/cmap-PiYG.png)  |
| PRGn    | ![PRGn](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/cmap-PRGn.png)  |
| PuOr    | ![PuOr](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/cmap-PuOr.png)  |
| RdBu    | ![RdBu](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/cmap-RdBu.png)  |
| RdGy    | ![RdGy](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/cmap-RdGy.png)  |
| RdYlBu  | ![RdYlBu](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/cmap-RdYlBu.png) |
| RdYlGn  | ![RdYlGn](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/cmap-RdYlGn.png) |
| Spectral| ![Spectral](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/cmap-spectral-2.png) |

## Sequential

| Name    | Appearance                     |
|---------|--------------------------------|
| Blues   | ![Blues](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/cmap-Blues.png) |
| BuGn    | ![BuGn](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/cmap-BuGn.png)  |
| BuPu    | ![BuPu](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/cmap-BuPu.png)  |
| GnBu    | ![GnBu](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/cmap-GnBu.png)  |
| Greens  | ![Greens](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/cmap-Greens.png) |
| Greys   | ![Greys](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/cmap-Greys.png) |
| Oranges | ![Oranges](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/cmap-Oranges.png) |
| OrRd    | ![OrRd](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/cmap-OrRd.png)  |
| PuBu    | ![PuBu](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/cmap-PuBu.png)  |
| PuBuGn  | ![PuBuGn](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/cmap-PuBuGn.png) |
| PuRd    | ![PuRd](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/cmap-PuRd.png)  |
| Purples | ![Purples](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/cmap-Purples.png) |
| RdPu    | ![RdPu](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/cmap-RdPu.png)  |
| Reds    | ![Reds](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/cmap-Reds.png)  |
| YlGn    | ![YlGn](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/cmap-YlGn.png)  |
| YlGnBu  | ![YlGnBu](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/cmap-YlGnBu.png) |
| YlOrBr  | ![YlOrBr](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/cmap-YlOrBr.png) |
| YlOrRd  | ![YlOrRd](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/cmap-YlOrRd.png) |

## Qualitative

| Name    | Appearance                     |
|---------|--------------------------------|
| Accent  | ![Accent](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/cmap-Accent.png) |
| Dark2   | ![Dark2](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/cmap-Dark2.png) |
| Paired  | ![Paired](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/cmap-Paired.png) |
| Pastel1 | ![Pastel1](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/cmap-Pastel1.png) |
| Pastel2 | ![Pastel2](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/cmap-Pastel2.png) |
| Set1    | ![Set1](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/cmap-Set1.png)  |
| Set2    | ![Set2](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/cmap-Set2.png)  |
| Set3    | ![Set3](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/cmap-Set3.png)  |

## Miscellaneous

| Name    | Appearance                     |
|---------|--------------------------------|
| afmhot  | ![afmhot](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/cmap-afmhot.png) |
| binary  | ![binary](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/cmap-binary.png) |
| brg     | ![brg](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/cmap-brg.png)   |
| bwr     | ![bwr](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/cmap-bwr.png)   |
| coolwarm| ![coolwarm](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/cmap-coolwarm.png) |
| CMRmap  | ![CMRmap](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/cmap-CMRmap.png) |
| cubehelix| ![cubehelix](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/cmap-cubehelix.png) |
| gnuplot | ![gnuplot](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/cmap-gnuplot.png) |
| gnuplot2| ![gnuplot2](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/cmap-gnuplot2.png) |
| ocean   | ![ocean](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/cmap-ocean.png) |
| rainbow | ![rainbow](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/cmap-rainbow.png) |
| seismic | ![seismic](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/cmap-seismic.png) |
| terrain | ![terrain](https://raw.githubusercontent.com/rougier/matplotlib-tutorial/master/figures/cmap-terrain.png) |
