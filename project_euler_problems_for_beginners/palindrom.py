# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 16:36:59 2018

@author: leon-
"""

a = 100
b = 100
x = 1
i = True

while i:
    c = a * b
    if c > x and str(c) == str(c)[::-1]:
        x = c
        a1 = a
        b1 = b
    a = a+1
    if a >= 1000:
        a = 100
        b = b + 1
        if b >= 1000:
            i = False
            
print("höchstes palindromisches Produkt aus zwei dreistelligen Zahlen: ", a1, "*", b1, "=", x)