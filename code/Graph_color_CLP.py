class GraphColoring:
    def __init__(self):
        self.V = 0
        self.num_of_colors = 0
        self.color = []
        self.graph = []
        self.state_names = []

    def create_adjacency_matrix(self, adjacency_list):
        vertices = sorted(adjacency_list.keys())
        self.state_names = vertices
        self.V = len(vertices)
        adj_matrix = [[0] * self.V for _ in range(self.V)]

        for i, vertex in enumerate(vertices):
            for neighbor in adjacency_list[vertex]:
                j = vertices.index(neighbor)
                adj_matrix[i][j] = 1

        return adj_matrix

    def graph_color(self, g, noc):
        self.V = len(g)
        self.num_of_colors = noc
        self.color = [0] * self.V
        self.graph = g

        try:
            self.solve(0)
            print("No solution")
        except Exception as e:
            print("\nSolution exists ")
            self.display()

    def solve(self, v):
        if v == self.V:
            raise Exception("Solution found")
        for c in range(1, self.num_of_colors + 1):
            if self.is_possible(v, c):
                self.color[v] = c
                self.solve(v + 1)
                self.color[v] = 0

    def is_possible(self, v, c):
        for i in range(self.V):
            if self.graph[v][i] == 1 and c == self.color[i]:
                return False
        return True

    def display(self):
        text_color = ["", "RED", "GREEN", "BLUE", "YELLOW", "ORANGE", "PINK",
                      "BLACK", "BROWN", "WHITE", "PURPLE", "VIOLET"]
        print("\nState Colors:")
        for i in range(self.V):
            state_name = self.state_names[i]
            color_name = text_color[self.color[i]]
            print(f"{state_name}: {color_name}")

def create_adjacency_list():
    adjacency_list = {
        'Western Australia': ['Northern Territory', 'South Australia'],
        'Northern Territory': ['Western Australia', 'Queensland', 'South Australia'],
        'South Australia': ['Western Australia', 'Northern Territory', 'Queensland', 'New South Wales', 'Victoria'],
        'Queensland': ['Northern Territory', 'South Australia', 'New South Wales'],
        'New South Wales': ['South Australia', 'Queensland', 'Victoria'],
        'Victoria': ['South Australia', 'New South Wales', 'Tasmania'],
        'Tasmania': ['Victoria']
    }
    return adjacency_list


if __name__ == "__main__":
    print("Graph Coloring Algorithm Test\n")
    gc = GraphColoring()

    australia_adjacency_list = create_adjacency_list()

    australia_adjacency_matrix = gc.create_adjacency_matrix(australia_adjacency_list)

    num_colors = int(input("Enter number of colors: "))

    gc.graph_color(australia_adjacency_matrix, num_colors)
