# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 14:51:55 2020

@author: ahmad
"""
from functools import reduce

def getProduct(array):
    return reduce((lambda x, y: x * y), array) 
    

def solution_1(A):
    triplet=[1]*3
    #first iteration:
    triplet=A[:3]
    r_prod = getProduct(triplet)
    
    #reset triplet for further operations
    triplet=[1]*3
    for p in range(1,len(A)-2): # iterate over the array till 2nd-last item
        for q in range(p+1,len(A)-1):
            for r in range(q+1,len(A)):
                triplet=[A[p],A[q],A[r]]
                prod = getProduct(triplet)
                if prod>r_prod:
                    r_prod = prod
    return r_prod

def solution(A):
    if len(A) < 3:
        return -1  
    A.sort()
    max_Product =max( A[-3] * A[-2] * A[-1],A[0] * A[1] * A[-1])
    return max_Product
   
def main():
    A = [
        [-3,1,2,-2,5,6],
        [3,3,3],
        [-1,2,2],
        [-1,-2,-3,-4],
        [-4, -6, 3, 4, 5]
        ]
    for item in A:
        result = solution(item)
        print(result)
    
if __name__ == '__main__':
    main()