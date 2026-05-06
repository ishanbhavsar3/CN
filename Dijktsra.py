import heapq 
 
def dijkstra(graph, start_node): 
    # Initialize distances as infinity 
    distances = {node: float('infinity') for node in graph} 
    distances[start_node] = 0 
    priority_queue = [(0, start_node)] 
 
    while priority_queue: 
        current_distance, current_node = heapq.heappop(priority_queue) 
 
        # Skip if we found a better path already 
        if current_distance > distances[current_node]: 
            continue 
 
        for neighbor, weight in graph[current_node].items(): 
            distance = current_distance + weight 
            if distance < distances[neighbor]: 
                distances[neighbor] = distance 
                heapq.heappush(priority_queue, (distance, neighbor)) 
     
    return distances 
 
# Example Graph 
my_graph = { 
    'A': {'B': 2, 'C': 5}, 
    'B': {'A': 2, 'C': 1, 'D': 4}, 
    'C': {'A': 5, 'B': 1, 'D': 1}, 
    'D': {'B': 4, 'C': 1} 
} 
 
print("Shortest Paths from A:", dijkstra(my_graph, 'A'))