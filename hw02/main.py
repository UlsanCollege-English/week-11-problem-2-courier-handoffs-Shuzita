"""
HW02 — Courier Handoffs (BFS Shortest Path)

Implement:
- bfs_path(graph, s, t)
"""

from collections import deque

def bfs_path(graph, s, t):
    """Return a shortest path (fewest edges) from s to t as a list of nodes.

    If s == t, return [s]. If s or t not in graph, return None.
    """

    # If nodes don't exist, no path
    if s not in graph or t not in graph:
        return None

    # Trivial case
    if s == t:
        return [s]

    # BFS setup
    queue = deque([s])
    visited = {s}
    parent = {s: None}

    # BFS traversal
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if v not in visited:
                visited.add(v)
                parent[v] = u
                queue.append(v)

                if v == t:
                    # reconstruct path
                    path = [t]
                    cur = t
                    while parent[cur] is not None:
                        cur = parent[cur]
                        path.append(cur)
                    return list(reversed(path))

    # No path found
    return None
