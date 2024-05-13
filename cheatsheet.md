# PHYS265 python - version 1 (may 2024)

##  Python

      if <boolean>:         for i in range(10):                     print(f"The value of n={n} and x={f:.3}")
         print('1')            print(i)                             def mysqr(x, a=1):
      elif <boolean>:       for i,c in enumerate(['a','b','c']):       return a*x*x
         print('2')            print(i,c)
      else                  while <boolean>:
         print('3')            do_something()


      a = [1, 2.0, 'c']         b = (1, 2.0, 'c')
      len(a)                    len(b)
      a[1]                      b[1]
      a.append(4j)
      a.pop()
      
##  Numpy

      import numpy as np

      a = np.zeros(10)                   A = np.zeros(4*3*2).reshape(4,3,2)    np.dot(x,y)
      b = list(range(10))                B = np.arange(4*3).reshape(4,3)       np.outer(x,y)
      c = np.linspace(0,10,101)          C = np.transpose(B)                   np.cross(x,y)
      d = np.arange(0,10,0.5)                                

      r = np.random.normal(10.0,1.0,100)       columns = np.loadtxt('mytable.txt').T
      len(r)                                   ncolumns = len(columns)
      r.mean()                                 columns[0].mean()
      r.std()
      r.sum()
      r.min()
      r.max()

## Plotting

      import matplotlib.pyplot as plt

      plt.figure(1)                               def func2(x, y, a=0):
      plt.clf(1)                                     return x**2 + y**2 + a
      plt.plot(x,y,'ko-', label="one")            xx = np.linspace(-1,1,21)
      plt.scatter(x,y)                            yy = np.linspace(-1,1,21)
      plt.hist(r, bins=20)                        xm, ym = np.meshgrid(xx,yy)
      plt.legend()                                zm = func2(xm,ym)
      plt.savefig('myplot.png')                   for j in range(21):
                                                     for i in range(21):
                                                        zm[j,i] = func2(xm[i],ym[j])
                                                  plt.contour(xm,ym,zm)

## Integrating

      from scipy.integrate import quad
      from scipy.integrate import solve_ivp

      def f1(x, m=1, b=0):           f2 = lambda x: x**2      def deriv(t, s, drag=0):
         return x*m + b                                          # s[0] = position
                                                                 # s[1] = velocity
                                                                 D = np.zeros(len(s))
                                                                 D[0] = s[1]
                                                                 D[1] = -9.8 * s[0] - drag * s[1]
                                                                 return D

      integral, err = quad(f1, 0.0, 4.0, args=(2.0, 1.0))

      sol = solve_ivp(deriv, (t0, t1), [x0, v0], args=(0.1,))
      print(sol.t, sol.y[0])

## Fitting

      from scipy.optimize import curve_fit
      from scipy.optimize import fsolve
      from scipy.optimize import brentq
      from scipy import linalg
      import scipy.stats as st

      params, covar = curve_fit(f1, xx, yy, p0)
      par1 = params[0]
      err1 = np.sqrt(covar[0][0])

      st.chi2.pdf()
      st.chi2.sf(chisq, ndof)

      linalg.inv(A)
      linalg.solve(A,b)

      root = fsolve(f1, x0, args=(2.0,1.0))
      root = brentq(f1, x0, x1, args=(2.0,1.0))


