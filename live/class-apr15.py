#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Author:   Peter Teuben
Created:  Mon Apr 15 11:57:40 2024
Modified: Mon Apr 15 11:57:40 2024

Description:
------------
"""
import numpy as np
import matplotlib.pyplot as plt


# class-apr15.

import scipy.stats as st

def f(x, m, b):
    # linear function, slope m, offset b
    return m*x + b

m = 2
b = -1 
dy = 0.2

npt = 11
xx = np.linspace(0, 2, npt)
ym = f(xx, m, b)
#np.random.seed(123)
yd = ym + np.random.normal(0,dy, npt)

plt.figure(1)
plt.clf()
plt.plot(xx, ym, '--')
plt.plot(xx, yd, 'ok')
plt.errorbar(xx, yd, dy, fmt='ok')

chisq =  ((yd-ym)**2).sum()/dy**2
pvalue = st.chi2.sf(chisq, npt)
print(f"chisq={chisq:.2f} pvalue={pvalue:.4})")

#%%

from scipy.optimize import curve_fit

def f1( x, m):
    #  danger danger, using global variable b
    return m*x + b
# b = 0
p0 = (2.5,)
sigma = np.full(len(yd), dy)
sigma = dy * np.ones(len(yd))
params, covar = curve_fit(f1, xx, yd, p0, sigma=sigma, absolute_sigma=True)
mfit = params[0]
merr = np.sqrt(covar[0][0])
print(f"mfit = {mfit:.3f} +/- {merr:.3f} for dy={dy}")

chisq = ((yd-f1(xx,mfit))**2).sum()/dy**2
pvalue = st.chi2.sf(chisq,npt)
print(f"chisq={chisq} pvalue={pvalue}")


#%%   a proper 2D fit


p0 = (30, 10)
params, covar = curve_fit(f, xx, yd, p0, sigma=sigma, absolute_sigma=True)
mfit = params[0]
merr = np.sqrt(covar[0][0])
bfit = params[1]
berr = np.sqrt(covar[1][1])
print(f"Weighted mfit = {mfit:.3f} +/- {merr:.3f}  bfit = {bfit:.3f} +/- {berr:.3f}  for dy={dy}")

chisq = ((yd-f(xx,mfit,bfit))**2).sum()/dy**2
pvalue = st.chi2.sf(chisq,npt)
print(f"chisq={chisq} pvalue={pvalue}")

#%%

params, covar = curve_fit(f, xx, yd, p0)

mfit = params[0]
merr = np.sqrt(covar[0][0])
bfit = params[1]
berr = np.sqrt(covar[1][1])
print(f"Unweighted mfit = {mfit:.3f} +/- {merr:.3f}  bfit = {bfit:.3f} +/- {berr:.3f}")

chisq = ((yd-f(xx,mfit,bfit))**2).sum()/dy**2
pvalue = st.chi2.sf(chisq,npt)
print(f"chisq={chisq} pvalue={pvalue}")
