# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 21:02:12 2020

@author: ahmad
"""

import math

def solution_1(X, Y, D):
    distanceCovered = X+D
    numberOfJumps = 1
    while True:
        distanceCovered = distanceCovered+D
        numberOfJumps += 1
        if (distanceCovered >= Y) :
            break
        else:
            pass
    return numberOfJumps
    

def solution(X, Y, D):
    jumpsRequired = (Y-X)/D
    
    return math.ceil(jumpsRequired)
    
def main():
    X = 10
    Y = 85
    D = 30
    result = solution(X,Y,D)
    print(result)
        
if __name__ == '__main__':
    main()