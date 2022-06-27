import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def DFS(v):
	global cnt
	# order[cnt] = v로 작성하고 아래에서 거치지 않는 노드를 따로 처리해 주어야 한다고 생각함
	# https://hueco.tistory.com/196 참고함
	order[v] = cnt
	cnt += 1
	visited[v] = True
	for i in graph[v]:
		if not visited[i]:
			DFS(i)

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
DFS(r)

[print(order[i]) for i in range(1, n + 1)]