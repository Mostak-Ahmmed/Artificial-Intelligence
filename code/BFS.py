from collections import deque

# Function to print the path recursively
def print_path(parent, start, dest):
    if dest == start:
        print(start, end=' ')
    elif dest not in parent:
        print("No path exists")
    else:
        print_path(parent, start, parent[dest])
        print(dest, end=' ')

# Function to find the shortest path using BFS
def bfs_shortest_path(grid, start, dest):
    rows = len(grid)
    cols = len(grid[0])
    visited = set()
    queue = deque([start])
    parent = {}

    while queue:
        current = queue.popleft()
        if current == dest:
            print("Shortest Path:")
            print_path(parent, start, dest)
            return True
        visited.add(current)
        x, y = current
        neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        for neighbor in neighbors:
            nx, ny = neighbor
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != '#' and neighbor not in visited:
                queue.append(neighbor)
                parent[neighbor] = current
                visited.add(neighbor)
    return False

# Example usage
grid = [
    ['.', '.', '.', '.', '.', '.'],
    ['.', '#', '#', '#', '.', '.'],
    ['.', '.', '.', '.', '.', '.'],
    ['.', '.', '#', '.', '.', '.'],
    ['.', '.', '#', '.', '#', '.'],
    ['.', '.', '.', '.', '.', '.']
]

start_point = (0, 0)
destination_point = (5, 5)

if not bfs_shortest_path(grid, start_point, destination_point):
    print("Destination is unreachable")
