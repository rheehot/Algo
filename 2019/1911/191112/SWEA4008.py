# SWEA 4008 계산기
import sys
sys.stdin = open('4008.txt','r')
from pprint import pprint as pp


import itertools
int(input())
for T in range(1):
    N = int(input())
    plus, minus, multi, div = map(int,input().split())
    line = list(map(int,input().split()))
    calc = '+'*plus +'-'*minus + '*'*multi + '/'*div        
    calcDict = dict()

    # arr는 0~N calcArr는 0~N-1
    def calculator(arr,calcArr):
        if calcArr in calcDict.keys():
            return calcDict[calcArr]
        res = arr[0]
        dic = { 
            "+":(lambda a, b : a + b), 
            "-":(lambda a, b : a - b), 
            "*":(lambda a, b : a * b), 
            "/":(lambda a, b : int(a / b)), 
        }
        for i in range(1,len(arr)):
            if calcArr[0:i] not in calcDict.keys():
                res = dic[calcArr[i-1]](res,arr[i])
                calcDict[calcArr[0:i]] = res
            else:
                res = calcDict[calcArr[0:i]]
        return res

    minRes = 100000000
    maxRes = -100000000
    result = set()
    
    for i in set(itertools.permutations(calc,N-1)):
        res = calculator(line,i)
        print(i)
        if res >= maxRes:
            maxRes = res
        if res <= minRes:
            minRes = res
    print(f"#{T+1} {maxRes-minRes}")
    print(calcDict)