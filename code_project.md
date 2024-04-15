# PHYS265 Code Project (draft)


This *Code Project* is an alternative to taking the 3rd midterm exam
on May 1st.
In this project you will select a (python based) open source project.
It is your task to evaluate this software package by using it.
**Due date will also be May 1st.**

You will need to learn how to install and use it, show some results
and some figures to illustrate your findings. All of this will be
summarized in a PDF based report. You also need to keep your code
examples, and a README to make your findings reproducable. We will use
your existing github repository that you used for lab1.

You are welcome to suggest your own project, but you will need to
run this by your instructors first. We also have our own list,
some of them are listed below.

## Writeup


Some packages may not work well on windows, and only on mac or linux. Some
requires a lot of extra software, which make it too complex to install,
or require a supercomputer.  Select something simple, and always run it
by your instructors for approval.

Some questions to answer:

- what does the package do?
- how old is the package?
- what about its geneology?
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
of robust code developed in other languages (mostly Fortran, IDL and C/C++).

- geneology: LMFIT (original MINPACK-1), MPFIT (IDL), cmpfit (), pycmpfit (python)

Your task is to find the python equivalent of MPFIT or LMFIT, and compare this
to curve_fit().

Your instructors may give you a dataset to fit and compare results.

### 2. Browsing "python" on ascl.net


This list is derived from https://ascl.net/code/search/python
What you see below is a first cut, and as you might read this draft,
may well disappear in the final version.

- PDRT: Photo Dissociation Region Toolbox - https://ascl.net/1102.022

- PySpecKit: Python Spectroscopic Toolkit - https://ascl.net/1109.001	

- PyModelFit: Model-fitting Framework and GUI Tool - https://ascl.net/1109.010

- PyEphem: Astronomical Ephemeris for Python	

- Astropysics: Astrophysics utilities for python	

- EzGal: A Flexible Interface for Stellar Population Synthesis Models	

- pNbody: A python parallelized N-body reduction toolbox	

- corner.py: Corner plots

- emcee: The MCMC Hammer (possibly most used code)	

- Aegean: Compact source finding in radio images	

- Galactus: Modeling and fitting of galaxies from neutral hydrogen (HI) cubes	

- Astropy: Community Python library for astronomy	

- AstroAsciiData: ASCII table Python module	

- SunPy: Python for Solar Physicists		

- pyExtinction: Atmospheric extinction

- Gammapy: Python toolbox for gamma-ray astronomy	

- galpy: Galactic dynamics package	

- PyBDSF: Python Blob Detection and Source Finder	

- pYSOVAR: Lightcurves analysis	

- PyTransit: Transit light curve modeling	

- pyro: Python-based tutorial for computational methods for hydrodynamics	

- SavGolFilterCov: Savitzky Golay filter for data with error covariance	

- POPPY: Physical Optics Propagation in PYthon	

- Lmfit: Non-Linear Least-Square Minimization and Curve-Fitting for Python	

- PRECESSION: Python toolbox for dynamics of spinning black-hole binaries	

- Gala: Galactic astronomy and gravitational dynamics	

- PROFILER: 1D galaxy light profile decomposition	

- SETI-EC: SETI Encryption Code	

- pydftools: Distribution function fitting in Python	

- Photon: Python tool for data plotting	

- oscode: Oscillatory ordinary differential equation solver	

- GWpy: Python package for studying data from gravitational-wave detectors	

- seaborn: Statistical data visualization	

- pyFFTW: Python wrapper around FFTW	

- Citlalicue: Create and manipulate stellar light curves	

- CosmosCanvas: Useful color maps for different astrophysical properties	

- CONCEPT: COsmological N-body CodE in PyThon	

- A pseudo GUI with pyplot - might be a nice idea, but only in chinese 

