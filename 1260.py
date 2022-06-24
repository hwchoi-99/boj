### 백준 1260번

from sys import stdin
input = stdin.readline

n, m, v = map(int, input().split())
# 1번 노드를 1번 인덱스로 하기 위해 "n + 1"로 그래프 범위 지정
graph = [[] for _ in range(n + 1)]
for _ in range(m):
	x, y = map(int, input().split())
	graph[x].append(y)
	graph[y].append(x)

# 작은 순서대로 정렬
for i in graph:
	i.sort()


visited_DFS = [False] * (n + 1)
def DFS(v):
	visited_DFS[v] = True
	print(v, end = ' ')
	for i in graph[v]:
		if not visited_DFS[i]:
			DFS(i)

from collections import deque
visited_BFS = [False] * (n + 1)
def BFS(v):
	queue = deque([v])
	visited_BFS[v] = True
	while queue:
		v = queue.popleft()
		print(v, end = ' ')
		for i in graph[v]:
			if not visited_BFS[i]:
				queue.append(i)
				visited_BFS[i] = True

DFS(v)
print()
BFS(v)



