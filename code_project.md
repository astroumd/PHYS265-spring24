# PHYS265 Code Project (draft-5)
 
This *Code Project* is an alternative to taking the 3rd midterm exam
on May 1st.  In this project you will select a (python based) open
source project.  It is your task to evaluate this software package by
using it (not reproducing it) and writing a report.
**Due date will be Thursday, May 2nd, at the usual 11.59pm time**

You will need to learn how to install and use it, show some results
and one or more figures to illustrate your findings. All of this will
be summarized in a report presented in PDF. You also need to show your
code example(s) how you exercised the code, and a README file to make
your findings reproducable.

NOTE: We will use a new folder **code3** inside your existing github
repository that you used for **lab1** and **lab2**.

You are welcome to suggest your own project too, either way, discuss
with your instructor which package you choose and you may get
additional guidelines. You can find some suggestions in our list
below extracted from ASCL and JOSS.

## Writeup

Some packages may not work well on your particular computer. Some
requires a lot of extra software, which make it too complex to install,
or require a supercomputer.  Select something simple, and always run it
by your instructors for approval. We do not want you to waste time getting
the package to run.

Some questions to answer:

- name of the package, and what does the package do?
- how old is the package? what about its geneology?
- is it still maintained, and by the original authors?
- evaluate how easy it was to install and use
- is the source code available?
- in your example, do you use the code, or do they use an interface (e.g. web, command line tool)
- is it pure python? or does it need accompanying C/C++/Fortran code?
- does it install via the "standard" pip/conda, or is it more complex?
- what is the input to the package? Just parameters, or dataset(s)?
- what is the output of the package? Just parameters, or dataset(s)?
- what (main) package does it use (e.g. numpy, curve_fit, solve_ivp)
- does the package produce figures, or are you on your own? Is matplotlib used?
- if you prefer to use a jupyter notebook instead of a python script, that's ok.



## Suggested projects


### Browsing for "python" codes on ASCL


This list below is an extraction from https://ascl.net/code/search/python
(this list returns well over 600 codes).
Another option would be to
browse JOSS ( https://joss.theoj.org/papers/search?q=python )
the Journal of Open Source Software, also a sizeable list.

Codes annotated with **[peter]** are codes that Peter uses from time to time.

- PDRT: Photo Dissociation Region Toolbox - https://ascl.net/1102.022

  OK

- PySpecKit: Python Spectroscopic Toolkit - https://ascl.net/1109.001 **[peter]**

  OK

- PyModelFit: Model-fitting Framework and GUI Tool - https://ascl.net/1109.010

  Seems only working in python2

- PyEphem: Astronomical Ephemeris for Python - https://ascl.net/1112.014

  ok. no graphics here.

- EzGal: A Flexible Interface for Stellar Population Synthesis Models - https://ascl.net/1208.021

  ok, but no example fits file?

- pNbody: A python parallelized N-body reduction toolbox - https://ascl.net/1302.004

  A general "pip install pnbody" did not work, but downloading from github and using

         pip install ./pNbody

  worked though.

- corner.py: Corner plots - https://ascl.net/1702.002

- emcee: The MCMC Hammer (possibly most used code) - https://ascl.net/1303.002	

  Markov chain Monte Carlo (MCMC) Ensemble sampler - probably one of the most downloaded codes
  used in papers. Together with the corner.py code, which plots up the covariance between
  variables.

- Aegean: Compact source finding in radio images - https://ascl.net/1212.009	

- Galactus: Modeling and fitting of galaxies from neutral hydrogen (HI) cubes - https://ascl.net/1303.018

- Astropy: Community Python library for astronomy - https://ascl.net/1304.002

  ok.

- AstroAsciiData: ASCII table Python module - https://ascl.net/1311.003

  Only works with python2

- SunPy: Python for Solar Physicists - https://ascl.net/1401.010		

- pyExtinction: Atmospheric extinction - https://ascl.net/1403.002

  It's still python2, why oh why

- Gammapy: Python toolbox for gamma-ray astronomy - https://ascl.net/1711.014

  Needs data.

- galpy: Galactic dynamics package - https://ascl.net/1411.008 **[peter]**

  ok

- PyBDSF: Python Blob Detection and Source Finder - https://ascl.net/1502.007

  Needs fortran and boost, and some python packages. Source code has test image.
  Invented their own "ipython" shell

- pYSOVAR: Lightcurves analysis	- https://ascl.net/1503.008

- PyTransit: Transit light curve modeling - https://ascl.net/1505.024	

- pyro: Python-based tutorial for computational methods for hydrodynamics - https://ascl.net/1507.018

- SavGolFilterCov: Savitzky Golay filter for data with error covariance	- https://ascl.net/1601.012

- POPPY: Physical Optics Propagation in PYthon - https://ascl.net/1602.018

- Lmfit: Non-Linear Least-Square Minimization and Curve-Fitting for Python - https://ascl.net/1606.014 **[peter]**

  ok, good alternative to curve_fit().  Here it would be interesting to show how you can fit something
  with curve_fit() and lmfit.   Your instructors may give you a dataset to fit and compare results.

- PRECESSION: Python toolbox for dynamics of spinning black-hole binaries - https://ascl.net/1611.004	

- Gala: Galactic astronomy and gravitational dynamics -	https://ascl.net/1707.006   **[peter]**

- PROFILER: 1D galaxy light profile decomposition - https://ascl.net/1705.010	

- SETI-EC: SETI Encryption Code	- https://ascl.net/1803.009

- pydftools: Distribution function fitting in Python - https://ascl.net/code/v/1940

- Photon: Python tool for data plotting	- https://ascl.net/1901.007

  A regular "pip install" claimed versions were not matching, but a manual
  "pip install -e ." in the source code worked, but then complains that
  my matplotlib has no mplDeprecation attribute.

- oscode: Oscillatory ordinary differential equation solver - https://ascl.net/1908.012

  builds a wheel;   mimics solve_ivp()

- GWpy: Python package for studying data from gravitational-wave detectors - https://ascl.net/1912.016

  ok

- seaborn: Statistical data visualization - https://ascl.net/2012.015	**[peter]**

- Citlalicue: Create and manipulate stellar light curves - https://ascl.net/2202.014

  Lot of dependancies that were not listed (arviz, celerite, corner,. ...)

- CosmosCanvas: Useful color maps for different astrophysical properties - https://ascl.net/2401.005	

- CONCEPT: COsmological N-body CodE in PyThon - https://ascl.net/2306.035

  Too compute intensive!!!

- AMUSE: Astrophysical Multipurpose Software Environment - https://ascl.net/1107.007 **[peter]**

  Most likely too large and complex, it's a python package talking to legacy codes to run a set
  of simulations of different nature (n-body, stellar evolution, hydro dynamics etc.)   Has a sister
  code called OMUSE.
  
## Installation Guidelines

Most python packages can be installed with pip.   Within spyder this would be the following
command (but check the README file in the package for guidelines, sometimes a conda
solution is given as well), e.g.

      !pip install galpy

Some packages will rely on you having a C compiler, and if that fails, it's better to find
another package before spending too much time solving compiler and linker problems.
There is also the danger that mixing **conda** and **pip** may mess up your python
environment.

If have downloaded the source code via git, you can also install it as developer, i.e. while you
would be editing their files, your modified code would be used!

      git clone https://github.com/jobovy/galpy
      pip install -e galpy
