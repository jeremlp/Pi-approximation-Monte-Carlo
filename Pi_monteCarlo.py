# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 02:40:37 2020

@author: Jeremy La Porte
Release V1.0
Pi approximation using Monte Carlo method
"""
from random import *
import matplotlib.pyplot as plt

data = 1000000
R=0
for i in range(data):
    x,y = random(),random()
    plt.scatter(x,y,c='r',s=0.4)
    if x**2 + y**2 <= 1:
        R= R+1
        plt.scatter(x,y,c='b',s=0.4)
        
print('moy', 4*R/data)

