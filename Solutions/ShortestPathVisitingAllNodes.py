class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        N = len(graph)

        q = deque()
        for i in range(N):
            q.append((1 << i, i, 0))

        visited = set()
        for i in range(N):
            visited.add((1 << i, i))

        while q:
            visited_nodes, node, ans = q.popleft()
            if visited_nodes == (1 << N) - 1:
                return ans

            for neighbor in graph[node]:
                updated_visited_nodes = visited_nodes | (1 << neighbor)
                if (updated_visited_nodes, neighbor) not in visited:
                    visited.add((updated_visited_nodes, neighbor))
                    q.append((updated_visited_nodes, neighbor, ans + 1))


"""You have an undirected, connected graph of n nodes labeled from 0 to n - 1. You are given an array graph where graph[i] is a list of all the nodes connected with node i by an edge.

Return the length of the shortest path that visits every node. You may start and stop at any node, you may revisit nodes multiple times, and you may reuse edges.



Example 1:


Input: graph = [[1,2,3],[0],[0],[0]]
Output: 4
Explanation: One possible path is [1,0,2,0,3]
Example 2:


Input: graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
Output: 4
Explanation: One possible path is [0,1,4,2,3]


Constraints:

n == graph.length
1 <= n <= 12
0 <= graph[i].length < n
graph[i] does not contain i.
If graph[a] contains b, then graph[b] contains a.
The input graph is always connected."""