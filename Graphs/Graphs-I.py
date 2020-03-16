#1 Using the graph shown in the picture above, write python code to represent the graph in an adjacency list.
class Graph:
    def __init__(self):
        self.vertices = {
                            "A": {"B":1},
                            "B": {"C": 3, "E": 1, "D": 2},
                            "C": {"E": 4},
                            "D": {"E": 2},
                            "E": {"F": 3},
                            "F": {},
                            "G": {"D": 1}
                        }
}

#2 Using the same graph you used for the first exercise, write python code to represent the graph in an adjacency matrix.
class Graph:
    def __init__(self):
        self.edges = [[0, 1, 0, 0, 0, 0, 0],
                      [0, 0, 3, 2, 1, 0, 0],
                      [0, 0, 0, 0, 4, 0, 0],
                      [0, 0, 0, 0, 2, 0, 0],
                      [0, 0, 0, 0, 0, 3, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 1, 0, 0, 0]]