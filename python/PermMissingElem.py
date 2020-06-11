# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 21:32:51 2020

@author: ahmad
"""


def solution(A):
    N = len(A)+1
    temp = []
    for i in range(1,N+1):
        temp.append(i)
    requiredSum = sum(temp)
    givenSum = sum(A)
    missingNumber = requiredSum -givenSum
    return missingNumber
        
    
def main():
    A = [1,2,3,5]
    result = solution(A)
    print(result)
        
if __name__ == '__main__':
    main()