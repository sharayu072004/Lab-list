def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()  # To keep track of visited nodes

    visited.add(node)  # Mark the current node as visited
    print(node, end=" ")  # Process the node (e.g., print it)

    for neighbor in graph.get(node, []):  # Explore neighbors
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

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

    start_node = input("\nEnter the starting node for DFS: ")

    print("\nDFS traversal:")
    dfs(graph, start_node)
