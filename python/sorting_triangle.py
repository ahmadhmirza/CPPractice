# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 15:51:27 2020

@author: ahmad
"""
def isTriangle(P,Q,R):
    if (P+Q>R) and (Q+R>P) and (R+P>Q):
        return True
    else:
        return False
    
def solution(A):
    for p in range(0,len(A)-2): # iterate over the array till 2nd-last item
        for q in range(p+1,len(A)-1):
            for r in range(q+1,len(A)):
                print(str(p) +","+str(q) +","+str(r))
                print("==")
                print(str(A[p]) +","+str(A[q]) +","+str(A[r]))
                print("")
                if isTriangle(A[p],A[q],A[r]):
                    return 1
    return 0
    
def main():
    A  = [
        [10,2,5,1,8,20],
        [10,50,5,1],
        [],
        [1,1,2,3,1,1,1,3,2,312,31,23,123,12,31,23,12,3,12,31,23,12,31]
        ]
    for item in A:
        result = solution(item)
        print(result)
        print("-----")
    
if __name__ == '__main__':
    main()