"""
<최단 경로 문제>
# 시작 정점에서 목표 정점까지 가는 간선의 가중치의 합이 최소가 되는 경로를 찾는 문제
# 최단 경로? 간선의 가중치가 있는 유향 그래프에서 두 정점 사이의 경로들 중 간선의 가중치의 합이 최소인 경로

1. 단일 시작점 최단 경로 문제
>> 출발점에서 다른 모든 정점들에 이르는 최단 경로를 구하는 문제
>> 해결1: 다익스트라(Dijkstra) 알고리즘: 음의 가중치를 허용하지 않음
>> 해결2: 벨만-포드(Bellman-Ford) 알고리즘: 음의 가중치 허용. 가중치 합이 음인 사이클은 허용하지 않음

2. 모든 쌍 최단 경로 문제
>> 모든 정점 쌍 간의 최단 경로를 구하는 문제
>> 해결: 플로이드 - 워샬 알고리즘 (동적계획법에서 다시 다룸)
"""



"""
<최단 경로 찾기 - 다익스트라 알고리즘>
# 시작 정점에서 거리가 최소인 정점부터 선택해 나가면서 최단 경로를 구하는 방식
# 탐욕 기법을 사용한 알고리즘으로 최소 신장 트리를 구하는 프림 알고리즘과 유사
# 시작 정점(r)에서 끝 정점(t)까지의 최단 경로에 정점 x가 존재

>> 최단 경로는 r에서 x까지의 최단 경로와 x에서 t까지의 최단 경로로 구성: r ~ x , x ~ t
>> 출발점 r에서 정점 v까지의 최단 경로 가중치 합 -> d[v]로 표기

# 시작점에서의 최단 경로를 찾은 정점들의 집합(S)을 관리
>> 초기 상태: S = {r}, d[r] = 0(자기 자신), d[v] = INF(자기 자신 외 나머지)
>> 최단 경로를 찾은 정점을 하나씩 집합 S에 추가
>> 집합 에스에 포함되지 않은 정점들 중에 출발점에 가장 가까운 정점 선택
# 탐욕적 방법으로 정점 선택하기

# D: 출발점에서 각 정점까지 최단 경로 가중치 합을 저장
# P: 최단 경로 트리 저장(부모 값 저장)
"""

#변수
N = 정점의 수 
G = 그래프
INF = 무한대 
r = 시작정점 


def Dijkstra(G, r):
    D = [INF] * N
    P = [None] * N
    visited = [False] * N
    D[r] = 0

    for _ in range(N):
        minIndex = -1
        min = INF
        for i in range(N): #최소 가중치 정점 찾기, 정점 N번 선택 후 종료
            if not visited[i] and D[i] < min:
                min = D[i]
                minIndex = i
        visited[minIndex] = True # 최소 가중치 정점 방문처리
        for v, val in G[minIndex]: # 인접한 정점에 대하여 최소 가중치 정점 찾기
            if not visited[v] and D[minIndex] + val < D[v]:
                D[v] = D[minIndex] + val
                P[v] = minIndex
                