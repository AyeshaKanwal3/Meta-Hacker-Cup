# Function to find the minimum number of edges
def min_edges(graph, start, target):
    visited = set()
    queue = [(start, 0, -1)]  # The third element of the tuple is the previous node (-1 for the start node)
    min_edges = float('inf')

    while queue:
        node, edges, prev_node = queue.pop(0)

        if node == target:
            min_edges = min(min_edges, edges)

        visited.add((node, prev_node))

        for neighbor in graph[node]:
            if (neighbor, node) not in visited and (node, neighbor) not in visited:
                queue.append((neighbor, edges + 1, node))

    return min_edges if min_edges != float('inf') else -1

# Read input from the input file
with open('input.txt', 'r') as input_file:
    T = int(input_file.readline().strip())
    with open('output.txt', 'w') as output_file:  # Open the output file for writing
        for case in range(1, T + 1):
            N, M = map(int, input_file.readline().split())
            graph = {i: [] for i in range(1, N + 1)}

            for _ in range(M):
                u, v = map(int, input_file.readline().split())
                graph[u].append(v)
                graph[v].append(u)

            Q = int(input_file.readline().strip())
            queries = [tuple(map(int, input_file.readline().split())) for _ in range(Q)]

            # Process the queries
            results = []
            for query in queries:
                a, b = query
                min_edge = min_edges(graph, a, b)
                results.append(min_edge)

            # Write the results to the output file
            output_file.write(f"Case #{case}: {sum(results)}\n")
