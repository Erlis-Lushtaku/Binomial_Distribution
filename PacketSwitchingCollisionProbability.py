# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 20:38:23 2021

@author: Erlis Lushtaku
"""

import math
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure, plot, bar, pie, draw, scatter
import seaborn as sns
from numpy.random import *
from numpy import *
import pandas as pd

def combination(n, k):
    return math.factorial(n)/(math.factorial(k)*math.factorial(n-k))

def binomialDistribution(n, k, p):
    return combination(n, k) * pow(p, k) * pow(1-p, n-k)

def cumulativeDistribution(n, k1, k2, p):
    result = 0
    for i in range(k1, k2+1):
        result += binomialDistribution(n, i, p)
    return result

n = 35
k1 = 11
k2 = n
p = 0.1

print(cumulativeDistribution(n, k1, k2, p))

points1 = {k: binomialDistribution(n, k, p) for k in range(0, n+1, 3)}
print(points1)

points2 = {n: cumulativeDistribution(n, k1, n, p) for n in range(k1-1, 101, 10)}
print(points2)

points3 = {k-1: cumulativeDistribution(n, k, n, p) for k in range(2, n+1, 3)}
print(points3)


fig1 = figure(figsize = (15,5))
ax1 = fig1.add_subplot(1,1,1)
ax1.set_title('Probability mass function for different values of N', fontsize=20)

for n in range(10, 86, 25):
    points = {k: binomialDistribution(n, k, p) for k in range(0, n+1)}
    s = pd.Series(points)
    ax1.plot(s,label = 'n = ' + str(n))

ax1.legend(loc='best')


fig1 = figure(figsize = (15,5))
ax1 = fig1.add_subplot(1,1,1)
ax1.set_title('N changes, different values of K', fontsize=20)

for k1 in range(5, 21, 3):
    points = {n: cumulativeDistribution(n, k1, n, p) for n in range(k1, 100)}
    s = pd.Series(points)
    ax1.plot(s,label = 'k = ' + str(k1-1))

ax1.legend(loc='best')


fig1 = figure(figsize = (15,5))
ax1 = fig1.add_subplot(1,1,1)
ax1.set_title('Cumulative Distribution for Different Values of N', fontsize=20)

for n in range(10, 86, 25):
    points = {k: cumulativeDistribution(n, k, n, p) for k in range(0, n)}
    s = pd.Series(points)
    ax1.plot(s,label = 'n = ' + str(n))
    
ax1.legend(loc='best')