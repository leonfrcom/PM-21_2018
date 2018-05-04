# -*- coding: utf-8 -*-
"""
Created on Fri May  4 13:29:38 2018

@author: leonfrcom
"""

def on_square(n):
    x = 1
    for i in range(n - 1):
        x = 2 * x
    return x
def total_after(n):
    n = n - 1
    return (2**(n+1))-1


if __name__ == '__main__':
    while True:
        n_i = input("Welches Feld? (in Zahlen) ")
        try:
            n = int(n_i)
            
            if n > 64 or n == 0:
                print("Zahl zwischen 1 und 64 eingeben...")
                pass
            else:            
                b = on_square(n)
                print("Auf Feld", n, "liegen", b, "Körner.")
                c = total_after(n)
                print("Insgesamt liegen bis Feld", n, c, "Körner auf dem Schachbrett.")
            
        except ValueError:
            print("bitte eine Zahl eingeben")