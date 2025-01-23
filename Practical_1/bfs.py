from collections import deque

def bfs(graph, start_node):
    visited = set()  # To keep track of visited nodes
    queue = deque([start_node])  # Use a queue to explore nodes level by level
    visited.add(start_node)  # Mark the start node as visited

    while queue:
        current = queue.popleft()  # Dequeue the next node
        print(current, end=" ")  # Process the node (e.g., print it)

        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                queue.append(neighbor)  # Enqueue unvisited neighbors
                visited.add(neighbor)

def build_graph():
    graph = {}
    n = int(input("Enter the number of edges in the graph: "))
    
    print("Enter the edges in the format 'node1 node2':")
    for _ in range(n):
        u, v = input().split()
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)  # Remove this line for directed graphs

    return graph

if __name__ == "__main__":
    print("Build the graph:")
    graph = build_graph()

    print("\nGraph representation (adjacency list):")
    for node, neighbors in graph.items():
        print(f"{node}: {neighbors}")

    start_node = input("\nEnter the starting node for BFS: ")

    print("\nBFS traversal:")
    bfs(graph, start_node)
