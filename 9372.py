### 백준 9372번

from sys import stdin
input = stdin.readline

def DFS(v):
  global cnt
  visited[v] = True
  cnt += 1
  for i in graph[v]:
    if not visited[i]:
      DFS(i)

for _ in range(int(input())):
  n, m = map(int, input().split())
  graph = [[] for _ in range(n + 1)]
  for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
  visited = [False] * (n + 1)

  cnt = 0
  DFS(1)
  # 모든 노드가 연결되어 있으므로 간선의 최대 수는 (노드 수) - 1
  print(cnt-1)
