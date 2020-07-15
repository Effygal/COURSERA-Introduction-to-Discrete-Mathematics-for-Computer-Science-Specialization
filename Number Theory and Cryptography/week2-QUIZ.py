#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 18:41:25 2020

@author: effygal


"""
#Greatest Common Divisor: Code
#Euclid's algorithm, efficient implementation:
def gcd(a, b):
  assert a >= 0 and b >= 0 and a + b > 0

  while a > 0 and b > 0:
    if a >= b:
      a = a % b
    else:
      b = b % a

  return max(a, b)


"""Extended Euclid's Algorithm: Code
The function extended_gcd(a,b) returns three values: the greatest common divisor of a and b: d=gcd(a,b); and two numbers x and y such that
d = ax + by"""
def extended_gcd(a, b):
  assert a >= b and b >= 0 and a + b > 0

  if b == 0:
    d, x, y = a, 1, 0
  else:
    (d, p, q) = extended_gcd(b, a % b)
    x = q
    y = p - q * (a // b)

  assert a % d == 0 and b % d == 0
  assert d == a * x + b * y
  return (d, x, y)

extended_gcd(10,6)
extended_gcd(7,5)
extended_gcd(391,299)
extended_gcd(239,201)

"""Tile a Rectangle with Squares
Given an n \times mn×m grid (where n,mn,m are integers), 
you would like to tile it with the minimal number of same size squares. 
Clearly, it can always be tiled with nmnm squares of size 1 \times 11×1, 
but it is not always optimal. For example, a 6 \times 106×10 grid can be tiled by 15 squares of size 2 \times 22×2:
Your goal in this problem is to implement a function squares(n, m) 
that returns the minimum number of same size squares required to tile a grid of size n \times mn×m. 
Your code should work fast (in less than a second) even for n,mn,m up to 1\,000\,000\,0001000000000.
 """
def squares(n, m):
  def gcd(n, m):
      assert n >= 0 and m >= 0 and n + m > 0
      while n > 0 and m > 0:
          if n >= m:
              n = n % m
          else:
              m = m % n
      return max(n, m)
  
  return n * m / gcd(n,m)**2  

"""Least Common Multiple: Code
Now that you know a connection between gcd and lcm, write an efficient algorithm for finding the least common multiple of two positive integers.
"""
def lcm(a, b):
  assert a > 0 and b > 0
  def gcd(a, b):
      assert a >= 0 and b >= 0 and a + b > 0
      while a > 0 and b > 0:
          if a >= b:
              a = a % b
          else:
              b = b % a
      return max(a, b) 
  
  
  return a*b/gcd(a,b)

"""Diophantine Equations: Code
Try to use extended Euclid's algorithm to solve Diophantine equations efficiently.
Given three numbers a>0a>0, b>0b>0, and cc, the algorithm should return some x and y such that
a x + b y = c ax+by=c"""

def gcd(a, b):
  assert a >= 0 and b >= 0 and a + b > 0

  while a > 0 and b > 0:
    if a >= b:
      a = a % b
    else:
      b = b % a
  return max(a, b)
      
def diophantine(a, b, c):
    assert c % gcd(a, b) == 0
    t = c / gcd(a, b)
    if b == 0:
        x, y = 1, 0
    else:
        p, q = diophantine(b, a % b, c/t)
        x = q
        y = p - q * (a // b)
    return (x*t, y*t)

"""Modular Division: Code
Now that you know how to use extended Euclid's algorithm for finding modular inverses, 
implement an efficient algorithm for dividing b by a modulo n.
Given three integers a, b, and n, such that gcd(a,n)=1 and n > 1, 
the algorithm should return an integer x such that
0 <= x <= n−1, and
b / a = x (mod n) (that is, b = ax (mod n)).
"""
def gcd(a, b):
  assert a >= 0 and b >= 0 and a + b > 0

  while a > 0 and b > 0:
    if a >= b:
      a = a % b
    else:
      b = b % a
  return max(a, b)
  
def divide(a, b, n):
    assert n > 1 and a > 0 and gcd(a, n) == 1
    def extended_gcd(a, b):    
      if b == 0:
        d, x, y = a, 1, 0
      else:
        (d, p, q) = extended_gcd(b, a % b)
        x = q
        y = p - q * (a // b)
    
      assert a % d == 0 and b % d == 0
      assert d == a * x + b * y
      return (d, x, y)
    d, x, y = extended_gcd(a, n)
    s = (b * x) % n
    assert 0 <= s and s <= n-1
    return (s)
#print(divide(2, 7, 9))
 # return the number x s.t. x = b / a (mod n) and 0 <= x <= n-1.























