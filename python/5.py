# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 10:29:53 2020

@author: ahmad
"""
def solution(N,A):
    counters=[0]*N
    print(counters)

    for op in A:
        if op <=N and op>=0:
            counters[op-1] += 1
        elif op == N+1 :
            maxVal = max(counters)
            counters = [maxVal]*N
    return counters

def main():
    A = [3, 4, 4, 6, 1, 4 ,4]
    N = 5
    result = solution(N,A)
    print(result)
    
        
if __name__ == '__main__':
    main()