# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 21:57:52 2015

@author: Naqib
"""

import math
#list of primes
primes = [2,]
x = 1
while (len(primes)<=10):#10 is how many primes will be in the list
    x+=2
    zeros= []
    for prime in primes:
        zeros.append(x%prime)
    if 0 not in zeros:
        primes.append(x)
    
print (primes)        

