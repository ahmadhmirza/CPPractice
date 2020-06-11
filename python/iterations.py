# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def solution(N):
    #convert the integer to binary
    number = bin(N).strip("0b")
    pC=str(1)
    longestBinaryGap = 0
    binaryGap = 0
    print("Number: " + str(N) + "; Binary: " + str(number))
    for c in number:
        if (pC == "0" and c == "0") or (pC == "1" and c == "0"):
            binaryGap += 1
        if (pC == "0" and c == "1"):
            if longestBinaryGap <= binaryGap:
                longestBinaryGap = binaryGap
            binaryGap = 0
        pC = c
    return longestBinaryGap

def test(N):
    bC = solution(N)
    print("longest binary gap in "+ str(N)+" is: " + str(bC))
    print("===============================================")
    
def main():
    
    test_list =  [1,2,3,4,5,6,7,8,9,147,200,483,647,1041,32,2147483647]
    for number in test_list:
        test(number)
    
if __name__ == '__main__':
    main()