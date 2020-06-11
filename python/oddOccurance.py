# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 20:16:57 2020

@author: ahmad
"""
import random


    
def solution_1(A):
    try:
        for item in A:
            temp = item
            itemIndex = A.index(item)
            A[itemIndex] = "x"
            if (item in A):
                newItemIndex = A.index(item)
                A[newItemIndex] = "x"
            else:
                return item
    except:
        pass

def arrayToHash(A):
    hashMap = {}
    for element in A:
        hashMap[random.getrandbits(128)] = element
    return hashMap

def solution(A):
    hashMap = arrayToHash(A)
    temp_dict = {}
    for key, value in hashMap.items():
        temp_dict.setdefault(value, set()).add(key)
    for key, values in temp_dict.items():
        if len(values) == 1:
            for item in values:
                return hashMap[item]
    return -1
        
def main():
    array_test = [1,2,1,2,2,3]
    result = solution(array_test)
    print(result)
    
if __name__ == '__main__':
    main()