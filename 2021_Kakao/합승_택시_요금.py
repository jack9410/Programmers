# 다익스트라로 시험때 맞았던 문제지만 검색으로 풀었다.
# 다익스트라 코딩 완벽하게 익히기
import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])
    # print(distances)

    while queue:
        curr_dist, curr_dest = heapq.heappop(queue)
        if distances[curr_dest] < curr_dist:
            continue

        for new_dest, new_dist in graph[curr_dest].items():
            distance =  curr_dist + new_dist
            if distance < distances[new_dest]:
                distances[new_dest] = distance
                heapq.heappush(queue, [distance, new_dest])
    return distances



def solution(n, s, a, b, fares):
    
    graph = {}

    for i in range(1, n+1):
        graph[i] = {}

    for i in fares:
        start, end, dist = i
        # print(start, end, dist)
        graph[start][end] = dist
        graph[end][start] = dist

    # print(graph)
    # print(dijkstra(graph, s))

    answer = float('inf')
    for i in dijkstra(graph, s).items():
        stopover = i[0]
        min_a = dijkstra(graph, stopover)[a]
        min_b = dijkstra(graph, stopover)[b]
        tmp = i[1] + min_a + min_b
        answer = min(tmp, answer)
    # print(answer)
    return answer

n, s, a, b = 6, 4, 6, 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
solution(n,s,a,b, fares)