# PHYS265 python - draft cheatsheet

##  Python

      if <boolean>:         for i in range(10):                     print(f"The value of n={n} and x={f:.3}")
         print('1')            print(i)                             def mysqr(x, a=1):
      elif <boolean>:       for i,c in enumerate(['a','b','c']:       return a*x*x
         print('2')            print(i,c)
      else                  while <boolean>:
         print('3')            do_something()


      a = [1, 2.0, 'c']         b = (1, 2.0, 'c')
      len(a)                    len(b)
      a[]   .pop .append
      


##  Numpy

      import numpy as np

      a = np.zeros(10)                   A = np.zeros(4*3*2).reshape(4,3,2)    np.dot(x,y)
      b = list(range(10))                B = np.arange(4*3).reshape(4,3)       np.outer(x,y)
      c = np.linspace(0,10,101)          C = np.transpose(B)                   np.cross(x,y)
      d = np.arange(0,10,0.5)                                

      r = np.random.normal(10.0,1.0,100)
      len(r)
      r.mean()
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
      plt.legend()                                xm, ym = np.meshgrid(xx,yy)
      plt.savefig('myplot.png')                   zm = func2(xm,ym)
                                                  plt.contour(xm,ym,zm)

## Integrating


      def f1(x, m=1, b=0):           f2 = lambda x: x**2      def deriv(t, s):
         return x*m + b                                          D = np.zeros(len(s))
                                                                 D[0] = s[1]
                                                                 D[1] = -9.8 * s[0]
                                                                 return D
								 

      int, err = scipy.integrate.quad(f1, 0.0, 4.0, args=(2.0, 1.0))

      sol = scipy.integrate.solve_ivp(deriv, (t0, t1), [x0, v0])
      print(sol.t, sol.y[0])

## Fitting

      params, covar = scipy.optimize.curve_fit(f1, xx, yy, p0)
      par1 = params[0]
      err1 = np.sqrt(covar[0][0])

      scipy.stats.chi2.pdf()
      scipy.stats.chi2.sf(chisq, ndof)

      scipy.linalg.inv(A)
      scipy.linalg.solve(A,b)

      root = scipy.optimize.fsolve(f1, x0, args=(2.0,1.0))
      root = scipy.optimize.brentq(f1, x0, x1, args=(2.0,1.0))


