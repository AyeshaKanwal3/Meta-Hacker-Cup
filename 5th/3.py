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

# Read input from the input file
with open('input.txt', 'r') as input_file, open('output.txt', 'w') as output_file:
    T = int(input_file.readline().strip())

    for case in range(1, T + 1):
        N, M = map(int, input_file.readline().split())
        graph = {i: [] for i in range(1, N + 1)}

        for _ in range(M):
            u, v = map(int, input_file.readline().split())
            graph[u].append(v)
            graph[v].append(u)

        dist = floyd_warshall(graph, N)  # Precompute minimum distances

        Q = int(input_file.readline().strip())
        queries = [tuple(map(int, input_file.readline().split())) for _ in range(Q)]

        # Process the queries
        results = []
        for query in queries:
            a, b = query
            min_edge = dist[a][b]
            results.append(min_edge)

        # Write the results to the output file
        output_file.write(f"Case #{case}: {sum(results)}\n")

print("Output has been written to 'output.txt'.")
