Import heapq 
 
def bellman_ford(vertices, edges, start): 
    # Initialize distances 
    distances = {v: float('inf') for v in vertices} 
    distances[start] = 0 
 
    # Relax all edges |V| - 1 times 
    for _ in range(len(vertices) - 1): 
        for u, v, w in edges: 
            if distances[u] != float('inf') and distances[u] + w < distances[v]: 
                distances[v] = distances[u] + w 
 
    # Check for negative weight cycles 
    for u, v, w in edges: 
        if distances[u] != float('inf') and distances[u] + w < distances[v]: 
            print("Graph contains negative weight cycle") 
            return None 
 
    return distances 
 
# Vertices and Edges (Source, Destination, Weight) 
nodes = ['A', 'B', 'C', 'D'] 
edge_list = [('A', 'B', 4), ('A', 'C', 2), ('C', 'B', 1), ('B', 'D', 3), ('C', 'D', 5)] 
 
print("Shortest Paths from A:", bellman_ford(nodes, edge_list, 'A'))