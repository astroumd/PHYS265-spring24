# PHYS265 Code Project (draft-3)
 
This *Code Project* is an alternative to taking the 3rd midterm exam
on May 1st.  In this project you will select a (python based) open
source project.  It is your task to evaluate this software package by
using it (not reproducing it) and writing a report.  **Due date will
also be May 1st.**

You will need to learn how to install and use it, show some results
and one or more figures to illustrate your findings. All of this will
be summarized in a report presented in PDF. You also need to show your
code examples how you exercised the code, and a README file to make
your findings reproducable. We will use a new folder **code3** inside
your existing github repository that you used for **lab1** and
**lab2**.

You are welcome to suggest your own project, either way, discuss with
your instructor which package you choose and you may get additional
guidelines. You can find some suggestions in our list below.

## Writeup

Some packages may not work well on Windows, and only on Mac or Linux. Some
requires a lot of extra software, which make it too complex to install,
or require a supercomputer.  Select something simple, and always run it
by your instructors for approval. 

Some questions to answer:

- name of the package, anad what does the package do?
- how old is the package? what about its geneology?
- is it still maintained, and by the original authors?
- is it pure python? or does it need accompanying C/C++/Fortran code?
- does it install via the "standard" pip/conda, or is it more complex?
- what is the input to the package? Just parameters, or dataset(s)?
- what is the output of the package? Just parameters, or dataset(s)?
- does the package produce figures, or are you on your own? Is matplotlib used?

## Suggested projects

### 1. Fitting

Although our recommended fitting module is curve_fit(), much like
we saw for quad() and solve_ivp() they are based on a long history
of robust codes developed in other languages (mostly Fortran, IDL and C/C++).

- geneology: LMFIT (original MINPACK-1), MPFIT (IDL), cmpfit (), pycmpfit (python)

Your task is to find the python equivalent of MPFIT or LMFIT, and compare this
code to the curve_fit() procedure we used in class.

Your instructors may give you a dataset to fit and compare results.

### 2. Browsing for "python" codes on ASCL


This list below is an extraction from https://ascl.net/code/search/python
some of these may well be too complex.

- PDRT: Photo Dissociation Region Toolbox - https://ascl.net/1102.022

- PySpecKit: Python Spectroscopic Toolkit - https://ascl.net/1109.001	

- PyModelFit: Model-fitting Framework and GUI Tool - https://ascl.net/1109.010

- PyEphem: Astronomical Ephemeris for Python - https://ascl.net/1112.014	

- EzGal: A Flexible Interface for Stellar Population Synthesis Models - https://ascl.net/1208.021	

- pNbody: A python parallelized N-body reduction toolbox - https://ascl.net/1302.004	

- corner.py: Corner plots - https://ascl.net/1702.002

- emcee: The MCMC Hammer (possibly most used code) - https://ascl.net/1303.002	

- Aegean: Compact source finding in radio images - https://ascl.net/1212.009	

- Galactus: Modeling and fitting of galaxies from neutral hydrogen (HI) cubes - https://ascl.net/1303.018

- Astropy: Community Python library for astronomy - https://ascl.net/1304.002	

- AstroAsciiData: ASCII table Python module - https://ascl.net/1311.003	

- SunPy: Python for Solar Physicists - https://ascl.net/1401.010		

- pyExtinction: Atmospheric extinction - https://ascl.net/1403.002

- Gammapy: Python toolbox for gamma-ray astronomy - https://ascl.net/1711.014	

- galpy: Galactic dynamics package - https://ascl.net/1411.008	

- PyBDSF: Python Blob Detection and Source Finder - https://ascl.net/1502.007	

- pYSOVAR: Lightcurves analysis	- https://ascl.net/1503.008

- PyTransit: Transit light curve modeling - https://ascl.net/1505.024	

- pyro: Python-based tutorial for computational methods for hydrodynamics - https://ascl.net/1507.018

- SavGolFilterCov: Savitzky Golay filter for data with error covariance	- https://ascl.net/1601.012

- POPPY: Physical Optics Propagation in PYthon - https://ascl.net/1602.018

- Lmfit: Non-Linear Least-Square Minimization and Curve-Fitting for Python - https://ascl.net/1606.014	

- PRECESSION: Python toolbox for dynamics of spinning black-hole binaries - https://ascl.net/1611.004	

- Gala: Galactic astronomy and gravitational dynamics -	https://ascl.net/1707.006

- PROFILER: 1D galaxy light profile decomposition - https://ascl.net/1705.010	

- SETI-EC: SETI Encryption Code	- https://ascl.net/1803.009

- pydftools: Distribution function fitting in Python - https://ascl.net/code/v/1940

- Photon: Python tool for data plotting	- https://ascl.net/1901.007

- oscode: Oscillatory ordinary differential equation solver - https://ascl.net/1908.012	

- GWpy: Python package for studying data from gravitational-wave detectors - https://ascl.net/1912.016	

- seaborn: Statistical data visualization - https://ascl.net/2012.015	

- Citlalicue: Create and manipulate stellar light curves - https://ascl.net/2202.014	

- CosmosCanvas: Useful color maps for different astrophysical properties - https://ascl.net/2401.005	

- CONCEPT: COsmological N-body CodE in PyThon - https://ascl.net/2306.035	

## Installation Guidelines

Most python packages can be installed with pip.   Within spyder this would be the following
command (but read their README for guidelines):

      !pip install ThePackage

Some packages will rely on you having a C compiler, and if that fails, it's better to find
another package before spending too much time solving compiler and linked problems.
There is also the danger that mixing **conda** and **pip** may mess up your python
environment.
