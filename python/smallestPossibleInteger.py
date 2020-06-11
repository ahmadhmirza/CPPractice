# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 09:30:37 2020

@author: ahmad
"""


def solution_1(A):
    leastNumber = 1000000
    reqNumber = 1
    #handling for empty array
    if len(A)==0:
        return 1
    for n in range(1,len(A)+2):
        if n in A:
            pass
        else:
            reqNumber =  n
            if reqNumber <= leastNumber:
                leastNumber = reqNumber
                return leastNumber
    return leastNumber
        
def solution_2(A):
    countArray = [False] * len(A)
    print(countArray)
    for number in A:
        if number > 0:
            countArray[number-1] = True
    if False in countArray:
        index = countArray.index(False)
        return index+1
    else:
        return len(countArray)+1

def solution(A):
    #handling for empty array
    if len(A) == 0:
        return 1
    #array to hold all positive integers corresponding to the size of A
    diffArray = list(range(1,len(A)+1))
    try:
        #find the missing number
        result = set(diffArray).difference(set(A)).pop()
    except:
        #no number missing in the sequence return the next number that did not occur in the sequence
        result = max(A)+1
    return result


def main():
    A = [1, 3, 6, 4, 1, 2]
    B = []
    C = [1,2,3]
    result = solution(A)
    print(result)
    result = solution(B)
    print(result)
    result = solution(C)
    print(result)
    
        
if __name__ == '__main__':
    main()