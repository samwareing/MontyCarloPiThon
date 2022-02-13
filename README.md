MontyCarloPiThon
================

![example workflow](https://github.com/samwareing/MontyCarloPiThon/actions/workflows/main.yaml/badge.svg)

Monte Carlo Pi Approximation in Python. This is only intended as a demo project.

How it works
-------

Monte Carlo simulations work by shaping random number generators in a way that mimics real life. If the shaping is correct, performing many runs of a simulation will converge on the correct answer. You can also add in some statistics.

MontyCarloPiThon works by estimating the area of a circle and a square, and using some simple maths to estimate pi from the ratio of those areas. It also watches how it converges on the real value of pi and plots the error.

Features
-------
Current:
- PiCalculatorPython: slow pi calculator written in pure Python.
- Plot: plots the simulation hits, convergence of pi and error with matplotlib.

TODO:
- Plotly interactive plotting
- Output to browser
- GUI
- GUI in browser
- PiCalculator in NumPy
- PiCalculator in C/C++ and linking to it
- Running Python in the browser
- Write a website

Licence
--------

* Free software: GNU General Public License v3
* Documentation: https://montycarlopithon.readthedocs.io.