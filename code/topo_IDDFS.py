class IterativeDeepening:
    def __init__(self):
        self.stack = []
        self.numberOfNodes = 0
        self.depth = 0
        self.maxDepth = 0
        self.goalFound = False

    def iterativeDeepening(self, adjacencyMatrix, destination):
        self.numberOfNodes = len(adjacencyMatrix)
        while not self.goalFound:
            self.depthLimitedSearch(adjacencyMatrix, 0, destination)  # Start from node 0
            self.maxDepth += 1
            if self.goalFound:
                print(f"\nGoal {destination} found at depth {self.depth}")
                return
            self.depth = 0
            self.stack = []

    def depthLimitedSearch(self, adjacencyMatrix, source, goal):
        visited = [False] * self.numberOfNodes
        self.stack.append(source)

        while self.stack:
            element = self.stack.pop()
            if not visited[element]:
                visited[element] = True
                print(element + 1, end=' ')  # Print node index (1-based) for output

                if element == goal:
                    self.goalFound = True
                    self.depth += 1
                    return

                # Explore neighbors in reverse order (right to left in adjacency matrix)
                for neighbor in range(self.numberOfNodes - 1, -1, -1):
                    if adjacencyMatrix[element][neighbor] == 1 and not visited[neighbor]:
                        self.stack.append(neighbor)

if __name__ == "__main__":
    try:
        print("Enter the number of nodes in the graph\n")
        number_of_nodes = int(input().strip())

        adjacency_matrix = []

        print("Enter the adjacency matrix\n")
        for i in range(number_of_nodes):
            row = list(map(int, input().strip().split()))
            adjacency_matrix.append(row)

        print("Enter the destination for the graph\n")
        destination = int(input().strip())

        iterativeDeepening = IterativeDeepening()
        iterativeDeepening.iterativeDeepening(adjacency_matrix, destination - 1)  # Adjust for 0-based indexing
    except ValueError:
        print("Wrong Input format")
