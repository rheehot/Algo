# BJ 15686 

import sys
import itertools
sys.stdin = open('input.txt','r')


N, M = map(int,input().split())
mat = [list(map(int,input().split())) for _ in range(N)]

def isPath(x,y):
    if 0 <= x <= N-1 and 0 <= y <= N-1:
        return True
    else:
        return False


dx = [0,0,-1,1]
dy = [-1,1,0,0]

def BFS(depth,x,y):
    visited = [[0]*N for _ in range(N)]
    queue = []
    queue.append((depth,x,y))
    while queue:
        dep, x, y = queue.pop(0)
        if not visited[x][y]:
            visited[x][y] = 1
            for i in range(4):
                nX = x + dx[i]
                nY = y + dy[i]
                if isPath(nX,nY):
                    if mat[nX][nY] == 2:
                        return dep + 1
                    queue.append((dep+1,nX,nY))

house = []
chicken = []
for x in range(N):
    for y in range(N):
        if mat[x][y] == 1:
            house.append((x,y))
        elif mat[x][y] == 2:
            chicken.append((x,y))
            # 치킨집 지워두기 
            mat[x][y] = 0

comb = itertools.combinations(chicken,M)
minRes = []

for survive in comb:
    for a,b in survive:
        mat[a][b] = 2
    # print(mat)
    res = 0
    for c,d in house:
        # print(c,d)
        res += BFS(0,c,d)
        # print(res)
    minRes.append(res)
    for a,b in survive:
        mat[a][b] = 0
print(min(minRes))








