# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 17:21:00 2020

@author: ahmad
"""
import math
import itertools


def subsets(n,m):
    dice = [1,2,3,4,5,6]
    perms = itertools.combinations_with_replacement(dice, n)
    for i in perms:
         if sum(i) == m:
             yield i
             
def solution(A, F, M):
        missingSum = M*(len(A)+F) - sum(A)
        x=subsets(F,missingSum)
        return (list(x))
              
def main():
    A= [1,5,6]
    F=4
    M=3
    
    #A  = [3,2,4,3]
    #F=2
    #M=4
    
    result = solution(A,F,M)
    print(result)
    
if __name__ == '__main__':
    main()