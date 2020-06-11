# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 21:44:06 2020

@author: ahmad
"""
import sys 
import numpy as np

def solution_1(A):
    pDiff = sys.maxsize
    for i in range(0,len(A)-1):
        temp_L = A[:i+1]
        temp_R = A[i+1:len(A)]
        diff = abs(sum(temp_L)-sum(temp_R))
        if diff < pDiff:
            pDiff = diff
    return pDiff

#numpy solution
def solution_2(A):
    npA = np.asarray(A)
    pDiff = sys.maxsize
    for i in range(1,len(npA)):
        arrays = np.array_split(npA,[i])
        diff = abs(sum(arrays[0])-sum(arrays[1]))
        if diff < pDiff:
            pDiff = diff
    return pDiff

def solution(A):
    pDiff = sys.maxsize
    for i in range(0,len(A)):
        copyA = A
        tempL = []
        for j in range(0,i):
            #print(str(i) + ", " + str(j))
            tempL.append(copyA.pop(j))
        print(tempL)
        print(copyA)
        print("----")

def main():
    A = [3,1,2,4,3]
    result = solution(A)
    print(result)
        
if __name__ == '__main__':
    main()