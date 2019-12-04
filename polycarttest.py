import polcart as pol
import cmath
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import style
import csv
from math import sqrt
print("hmm")
# a,b = pol.to_cartesian(0.55, 10, theta_units="degrees")
# print(a,b)
# c = complex(a,b)
# print(c)
# d = abs(c)
# print(d)
# e = np.absolute(c)
# print(e)
# with open('HMC636ST89.csv', 'r') as csv_file:
	# csv_reader = csv.reader(csv_file)
	
	# for line in csv_reader:
		# print(line[1])
#q,w,e,r,t,y,u,i,o = np.loadtxt('HMC636ST89.csv', unpack=True)
#q,w,e,r,t,y,u,i,o = np.genfromtxt('HMC636ST89.csv',delimiter=' ',dtype=None)
		
dt = np.dtype([('freq', float), 
				('s11m', float),
				('s11a', float), 
				('s21m', float), 
				('s21a', float),
				('s12m', float),
				('s12a', float),
				('s22m', float),
				('s22a', float)
				])
result = np.loadtxt('HMC636ST89.csv', delimiter = ',', dtype=dt )
# print(result[0])
# print(result[0]['freq'], result[0]['s22a'])

i=92

freq = result[i]['freq']
s11m = result[i]['s11m']
s11a = result[i]['s11a']
s21m = result[i]['s21m']
s21a = result[i]['s21a']
s12m = result[i]['s12m']
s12a = result[i]['s12a']
s22m = result[i]['s22m']
s22a = result[i]['s22a']
print(freq, s11m, s11a, s21m, s21a, s12a, s12a, s22m, s22a)

s11r, s11i = pol.to_cartesian(s11m, s11a, theta_units="degrees")
print("s11r and s11i is ", s11r, s11i)
s11c = complex(s11r, s11i)
print("s11c is", s11c)
s11abs = abs(s11c)
print("s11abs is", s11abs)


s21r, s21i = pol.to_cartesian(s21m, s21a, theta_units="degrees")
print("s21r and s21i is ", s21r, s21i)
s21c = complex(s21r, s21i)
print("s21c is", s21c)
s21abs = abs(s21c)
print("s21abs is", s21abs)


s12r, s12i = pol.to_cartesian(s12m, s12a, theta_units="degrees")
print("s12r and s12i is ", s12r, s12i)
s12c = complex(s12r, s12i)
print("s12c is", s12c)
s12abs = abs(s12c)
print("s12abs is", s12abs)


s22r, s22i = pol.to_cartesian(s22m, s22a, theta_units="degrees")
print("s22r and s22i is ", s22r, s22i)
s22c = complex(s22r, s22i)
print("s22c is", s22c)
s22abs = abs(s22c)
print("s22abs is", s22abs)

numer = 1-s11abs**2
delta = (s11c*s22c)-(s12c*s21c)
print("numer is", numer)
print("delta is", delta)
a=complex(1,4)
b=complex(2,2)
print(a,b)
c = a*b
print(c)
