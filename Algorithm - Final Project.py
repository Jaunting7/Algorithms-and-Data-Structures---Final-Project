import sys

graph = {
    # H, K, Q, T are the charging stations
    'A': {'B': 6, 'F': 5},
    'B': {'A': 6, 'C': 5, 'G': 6},
    'C': {'B': 5, 'D': 7, 'H': 5},
    'D': {'C': 7, 'E': 7, 'I': 8},
    'E': {'D': 7, 'I': 6, 'N': 15},
    'F': {'A': 5, 'G': 8, 'J': 7},
    'G': {'B': 6, 'F': 8, 'H': 9, 'K': 8},
    'H': {'C': 5, 'G': 9, 'I': 12}, # Charging station
    'I': {'D': 8, 'E': 6, 'H': 12, 'M': 10},
    'J': {'F': 7, 'K': 5, 'O': 7},
    'K': {'G': 8, 'J': 5, 'L': 7}, # Charging Station
    'L': {'K': 7, 'M': 7, "P": 7},
    'M': {'I': 10, 'L': 7, 'N': 9},
    'N': {'E': 15, 'M': 9, 'R': 7},
    'O': {'J': 7, 'P': 13, 'S': 9}, 
    'P': {'L': 7, 'O': 13, 'Q': 8, 'U': 11},
    'Q': {'P': 8, 'R': 9}, # Charging Station
    'R': {'N': 7, 'Q': 9, 'W': 10},
    'S': {'O': 9, 'T': 9},
    'T': {'S': 9, 'U': 8}, # Charging Station
    'U': {'P': 11, 'T': 8, 'V': 8},
    'V': {'U': 8, 'W': 5},
    'W': {'R': 10, 'V': 5}
}


def Dijkstra(graph, source, dest):
    unvisited = set(graph.keys()) # Get all graphs keys (letters) then convert to a set
    current_node = source # Starts at source node so set current node to source
    nodes = {node: sys.maxsize for node in graph} # Dictionary with each node's values set to the max int value (infinite) | Used to hold the shortest known distance from source node
    nodes[source] = 0 # Set source node value to 0 (no distance from itself)
    path = {} # Keeps track of the shortest path from the source node to each node | key:value is neighbor_node:previous_node

    # When no graph
    if not graph:
        print("Empty Graph")
        return nodes

    while unvisited: # when all nodes are not visted

        # Track which node to go to next
        min_distance = sys.maxsize # Sets min distance to the max int value (infinite)
        for node in unvisited: # For the nodes that are unvisted
            if nodes[node] < min_distance: # If node value is less than min distance
                min_distance = nodes[node] # updates min distance
                current_node = node # set current node to the node

        if current_node == dest or nodes[current_node] == sys.maxsize: # If the current node is the destination or is max int value (infinite) then break and exit loop
            break 

        unvisited.remove(current_node) # Remove current node from unvisted

        # Update shortest known distances
        for neighbor, distance in graph[current_node].items(): # Initialize neighbor and distance from the graph dictionary's respective key's value dictionary
            if neighbor in unvisited: # If neighbor unvisited
                new_cost = nodes[current_node] + distance # add the distance (from current node to neighbor node) to the shortest known distance from source node to current node 
                if new_cost < nodes[neighbor]: # If the new distance is less then the current shortest distance stored in neighbor node
                    nodes[neighbor] = new_cost # update neighbor shortest distance with the new cost
                    path[neighbor] = current_node # update neighbor with the current node

    # When no path for destination
    if nodes[dest] == sys.maxsize:
        print("No path found")
        return None

    # Constructing the shortest path
    shortest_path = []
    while dest != source: # While dest not equal to source
        shortest_path.insert(0, dest)  # insert "dest" as first element
        dest = path[dest] # set dest to its predecessor node (essentially working backwards from destination to source node to construct the list)
    shortest_path.insert(0, source) # Finally, insert the source node at beginning
    return shortest_path, nodes


source_node = input("Enter your source destination: ")
destination_node_list = ["H", "K", "Q", "T"] # All charging station locations (destination nodes)
for node in destination_node_list:
    shortest_path, nodes = Dijkstra(graph, source_node, node)
    if shortest_path:
        print(f"The shortest path from {source_node} to {node} is: {' -> '.join(shortest_path)}")
        print(f"The total cost is: {nodes[node]}")