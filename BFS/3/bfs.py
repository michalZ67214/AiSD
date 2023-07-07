from collections import deque

def BFS(graph, s):
    visited = set()
    queue = dueue([s])
    
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex)
            visited.add(vertex)
            neighbors = graph[vertex]
            queue.extend(neighbors)