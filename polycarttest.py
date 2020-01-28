import polcart as pol
import cmath
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import pyplot as plt1
from matplotlib import pyplot as plt2
from matplotlib import style
import csv
from math import sqrt
def printmu(result): #Function to print mu value
    xaxis = result['freq']
    yaxismu = result['mu']
    plt.figure(0)
    plt.plot(xaxis, yaxismu)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('mu')
    plt.axhline(y=1, color='r', linestyle='-') # Plotting the constant Y at mu=1.
    plt.title('Mu against Frequency to determine device stability')
    plt.show()
def printuni(result):
    xaxis = result['freq']
    yaxisuni = result['uni']
    plt.figure(1)
    plt.plot(xaxis, yaxisuni)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('U')
    plt.axhline(y=0.1, color='r', linestyle='-') # Plotting the uni assumption at 0.1 db.
    plt.title('Uniltateral assumption value against Frequency to determine unilateral assumption hold')
    plt.show()

def printgtumax(result):
    xaxis = result['freq']
    yaxisgtumax = result['gtumax']
    plt.figure(2)
    plt.plot(xaxis, yaxisgtumax)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('GtuMax')
    plt.title('GtuMax against Frequency to determine maximum available gain')
    plt.show()
            
dt = np.dtype( [('freq', float), #Data type created to read in CSV file and be able to
    ('s11m', float), #add columns for the 3 tests.
    ('s11a', float),
    ('s21m', float),
    ('s21a', float),
    ('s12m', float),
    ('s12a', float),
    ('s22m', float),
    ('s22a', float),
    ('mu', float),
    ('uni', float),
    ('gtumax', float)])
result = np.loadtxt('HMC636ST89.csv', delimiter = ',', dtype=dt ) 
for i in range(0, len(result)): #Creating an internal array called result to store values.
    freq = result[i]['freq']
    s11m = result[i]['s11m']
    s11a = result[i]['s11a']
    s21m = result[i]['s21m']
    s21a = result[i]['s21a']
    s12m = result[i]['s12m']
    s12a = result[i]['s12a']
    s22m = result[i]['s22m']
    s22a = result[i]['s22a']
    mu = result[i]['mu']
    uni = result[i]['uni']
    gtumax = result[i]['gtumax']
    
    #This page assigns internal S parameter variables within the for loop code
    print(i, freq, s11m, s11a, s21m, s21a, s12a, s12a, s22m, s22a)
    
    #------------- S11--------------
    s11r, s11i = pol.to_cartesian(s11m, s11a, theta_units="degrees")
    #print("s11r and s11i is ", s11r, s11i)
    s11c = complex(s11r, s11i)
    #print("s11c is", s11c)
    s11conj = np.conj(s11c)
    #print("s11conj is", s11conj)
    s11abs = abs(s11c)
    #print("s11abs is", s11abs)
    #------------- S11--------------
    
    #------------- S21--------------
    s21r, s21i = pol.to_cartesian(s21m, s21a, theta_units="degrees")
    #print("s21r and s21i is ", s21r, s21i)
    s21c = complex(s21r, s21i)
    #print("s21c is", s21c)
    s21abs = abs(s21c)
    #print("s21abs is", s21abs)
    #------------- S21--------------
    
    #------------- S12--------------
    s12r, s12i = pol.to_cartesian(s12m, s12a, theta_units="degrees")
    #print("s12r and s12i is ", s12r, s12i)
    s12c = complex(s12r, s12i)
    #print("s12c is", s12c)
    s12abs = abs(s12c)
    #print("s12abs is", s12abs)
    #------------- S12--------------
    
    #------------- S22--------------
    s22r, s22i = pol.to_cartesian(s22m, s22a, theta_units="degrees")
    #print("s22r and s22i is ", s22r, s22i)
    s22c = complex(s22r, s22i)
    #print("s22c is", s22c)
    s22abs = abs(s22c)
    #print("s22abs is", s22abs)
    #------------- S22--------------
    
    #------------- mu-------------- #Function to calculate device stability at each frequency
    numer = 1-s11abs**2
    delta = (s11c*s22c)-(s12c*s21c)
    denoma = abs(s22c - s11conj*delta)
    denomb = s12abs*s21abs
    mu = numer/denoma*denomb
    result[i]['mu'] = mu
    #------------- mu--------------
    
    #------------- uni-------------- #Function to calculate device unilateral assumption
    numer1 = s11abs*s12abs*s21abs*s22abs
    denom1a = 1-s11abs**2
    denom1b = 1-s22abs**2
    uni = numer1/(denom1a*denom1b)
    #print("numer1 is", numer1)
    #print("denom1a/denom1b is", denom1a, denom1b)
    #print("uni is", uni)
    result[i]['uni'] = uni
    #------------- uni--------------
    
    #------------- gtumax-------------- #Function to calculate maximum gain
    gsmax = 10*cmath.log10(1/(1-s11abs**2)).real
    glmax = 10*cmath.log10(1/(1-s22abs**2)).real
    go = 10*cmath.log10(s21abs**2).real
    gtumax = gsmax + glmax + go
    #print("gsmax is", gsmax)
    #print("glmax is", glmax)
    #print("go is", go)
    #print("gtumax is", gtumax)
    result[i]['gtumax'] = gtumax
    #------------- gtumax--------------
    
    #print("")
    #print(result[i])
    if result[i]['mu'] > 1:
    print("This device at frequency {:.3f} is stable.".format(result[i]['freq']))
    else:
    print("This device at frequency {:.3f} is unstable.".format(result[i]['freq']))
    
    
printmu(result)
printuni(result)
printgtumax(result)
        
    