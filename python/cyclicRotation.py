# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 19:00:23 2020

@author: ahmad
"""

# Cyclic rotation
# param A, array
# param K, intereger number of rotation
def solution(A, K):
    try:
        for n in range(K,0,-1):
            temp = A[len(A)-1]
            for j in range(len(A)-1,0,-1):
                A[j] = A[j-1]
            A[0] = temp
        return A
    except Exception as e:
        print(str(e))
        return -1

def main():
    array_1 = []  
    result = solution(array_1,1)
    print(result)
        
if __name__ == '__main__':
    main()












































def main():
    A = [3, 8, 9, 7, 6]
    K = 3
    solution(A,K)