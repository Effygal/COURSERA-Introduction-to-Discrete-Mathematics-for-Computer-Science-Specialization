#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 21:30:26 2020

Mathematical thinking in Computer Science
week6-quizz
@author: effygal

"""
"""
Is a permutation even?
"""
def is_permutation(p):
  return (set(p)==set(range(len(p))))
       
print (is_permutation([0]))
print (is_permutation([0,2,1]))
print (is_permutation([1,2,3]))

def is_even(p):
    count = 0
    for i in range(len(p)):
        for j in range(i+1, len(p)):
            if p[i] > p[j]:
                p[i], p[j] = p[j], p[i]
                count += 1
    return count % 2 == 0
                
print(is_even([0,3,2,4,5,6,7,1,9,8] ))

