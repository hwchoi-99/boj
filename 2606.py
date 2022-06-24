### 백준 2606번

# BFS에서 queue를 효율적으로 사용하기 위해 deque 사용
from collections import deque
computer = int(input())
case = int(input())
graph = [[] for _ in range(computer + 1)]
for _ in range(case):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    
for i in range(1, computer + 1):
    graph[i].sort()

cnt = -1
visited = [False] * (computer + 1)

def BFS(v):
    global cnt
    queue = deque([v])
    visited[v] = True
    while queue:
        v = queue.popleft()
        cnt += 1
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

BFS(1)
print(cnt)