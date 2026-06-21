class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        mavorqeli = (n, edges, labels, k)
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
        pq = [(0, 0, labels[0], 1)]
        dist = {}
        dist[(0, labels[0], 1)] = 0
        while pq:
            cost, node, last_char, consec = heapq.heappop(pq)
            if node == n - 1:
                    return cost
            for nei, w in graph[node]:
                new_cost = cost + w
                new_char = labels[nei]
                if new_char == last_char:
                    new_consec = consec + 1
                else:
                    new_consec = 1
                if new_consec <= k:
                    state = (nei, new_char, new_consec)
                    if state not in dist or new_cost < dist[state]:
                        dist[state] = new_cost
                        heapq.heappush(pq, (new_cost, nei, new_char, new_consec))
        return -1