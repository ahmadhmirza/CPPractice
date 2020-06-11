# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 12:08:12 2020

@author: ahmad
"""

impactFactor = {
        "A":1,
        "C":2,
        "G":3,
        "T":4
    }

def solution(S, P, Q):
    dnaSeq = list(S)
    NumOfQueries = len(P)
    lowestImpactFactor = 4
     lif_list =[]
    
    if (len(P)==len(Q)): #test if both arrays are equal
        for i in range(0,NumOfQueries):
            lower = P[i]
            upper = Q[i]
            if (lower == upper):
                iF = impactFactor[dnaSeq[lower]]
                lif_list.append(iF)
            else:
                for j in range(lower,upper+1):
                    try:
                        print(dnaSeq[j])
                        iF = impactFactor[dnaSeq[j]]
                    except Exception as e:
                        iF = 0 # incase of invalid sequence
                        
                    if iF<lowestImpactFactor:
                        lowestImpactFactor = iF
                lif_list.append(lowestImpactFactor)
                lowestImpactFactor=4
        return lif_list
    
    
def main():
    S = "CAGCCTA"
    P = [2,5,0]
    Q = [4,5,6]
    S="A"
    P= [0]
    Q= [0]
    S='TC'
    P=[0, 0, 1]
    Q=[0, 1, 1]
    result = solution(S,P,Q)
    print(result)
    
        
if __name__ == '__main__':
    main()