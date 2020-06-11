# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 14:40:06 2020

@author: ahmad
"""


def solution(A):
    return True
    
def main():
    A  = [
        [10,2,5,1,8,20],
        [10,50,5,1]
        ]
    for item in A:
        result = solution(item)
        print(result)
    
if __name__ == '__main__':
    main()