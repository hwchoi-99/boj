from collections import deque
import sys
input = sys.stdin.readline

# 22479 코드를 BFS로 변경
def BFS(v):
	global cnt
	# A
	visited[v] = True
	queue = deque([v])
	while queue:
		v = queue.popleft()
		for i in graph[v]:
			if not visited[i]:
				queue.append(i)
				visited[i] = True
		# DFS에서는 A에 위치하고 있었음
		order[v] = cnt
		cnt += 1

n, m, r = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
	x, y = map(int, input().split())
	graph[x].append(y)
	graph[y].append(x)

for srt in graph:
	srt.sort()

visited = [False] * (n + 1)
order = [0] * (n + 1)
cnt = 1
BFS(r)

[print(order[i]) for i in range(1, n + 1)]