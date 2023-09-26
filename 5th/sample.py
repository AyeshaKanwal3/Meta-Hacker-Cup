def floyd_warshall(graph, N):
    # Initialize the distance matrix with infinity values
    dist = [[float('inf')] * (N + 1) for _ in range(N + 1)]

    # Set the distance for direct edges to 1
    for u in range(1, N + 1):
        dist[u][u] = 0
        for v in graph[u]:
            dist[u][v] = 1
            dist[v][u] = 1

    # Floyd-Warshall algorithm to compute minimum distances
    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

# Read the number of test cases
T = int(input())

for case in range(1, T + 1):
    N, M = map(int, input().split())
    graph = {i: [] for i in range(1, N + 1)}

    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    dist = floyd_warshall(graph, N)  # Precompute minimum distances

    Q = int(input().strip())
    queries = [tuple(map(int, input().split())) for _ in range(Q)]

    # Process the queries
    results = []
    for query in queries:
        a, b = query
        min_distance = dist[a][b]
        results.append(min_distance)

    # Calculate the difference between sums of minimum distances
    diff = sum(results[::2]) - sum(results[1::2])

    # Print the result for the current test case
    print(f"Case #{case}: {diff}")

