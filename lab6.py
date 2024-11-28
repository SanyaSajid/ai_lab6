# Graph definition
graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': [],
    '8': []
}

# Depth-limited search (DFS with a limit)
def dls(node, graph, goal, depth, visited):
    print(node, end=" ")
    if node == goal:
        return True
    if depth <= 0:
        return False
    
    visited.append(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            if dls(neighbor, graph, goal, depth - 1, visited):
                return True
    return False

# Iterative deepening search (IDS)
def ids(graph, start, goal, max_depth):
    for depth in range(max_depth):
        visited = []
        print(f"\nDepth level: {depth}")
        if dls(start, graph, goal, depth, visited):
            print("\nGoal found!")
            return
    print("\nGoal not found within depth limit.")

# Driver code
print("Following is the Iterative Deepening Search")
ids(graph, start='5', goal='8', max_depth=5)  # Searching for node '8' starting from node '5'
