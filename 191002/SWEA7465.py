import sys
sys.stdin = open('input3.txt','r')
from pprint import pprint as pp

# DP 

def DP(pers):
    global cnt
    global res
    if res[pers]:
        return
    res[pers] = cnt    
    for j in vilDic[pers]:
        DP(j)
    

    

for T in range(int(input())):
    cnt = 1
    N, M = map(int,input().split())
    vilDic = {}
    for i in range(0,N+1):
        vilDic[i] = []
    mat = [[0]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        x, y = map(int,input().split())
        vilDic[x].append(y)
        vilDic[y].append(x)
    cnt = 0
    res = [0]*(N+1)
    for i in vilDic.keys():
        if i == 0:
            continue
        if res[i]:
            continue
        else:
            cnt += 1
            DP(i)

    print("#{} {}".format(T+1,max(res[1:])))


"""
for i in vilDic.keys():
    if res[i]:
        continue
    else:
        cnt += 1
        dp(i)


#plan
res = [0]*(N+1)
dp(n):
    0. 만약 res[n]이 있으면 그냥 무시  
    1. 없으면 cnt += 1 하고
    n을 키값으로 리스트에 있는 것들을 모두 cnt로 저장
"""




        


"""
# 딕셔너리로 하기엔 N(N-1)/2 가 너무 걸림. 
# append하면 시간 초과할 것 같아서 매트릭스로 받아서 값 바꾸고  
# DP로 짜야할듯!..
vilPeople = {}
for _ in range(M):
    x, y = map(int,input().split())
    if x not in vilPeople.keys():
        vilPeople[x] = []
    if y not in vilPeople.keys():
        vilPeople[y] = []
    vilPeople[x].append(y)
    vilPeople[y].append(x)
# print(vilPeople)
"""
