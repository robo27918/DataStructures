class Graph:
    def __init__ (self, adjacency_list ={}):
        self.adjacency_list = {}
    
    def add_edge(self,node1,node2):
        if node1 not in self.adjacency_list:
            self.adjacency_list[node1] = []
        if node2 not in self.adjacency_list:
            self.adjacency_list[node2] = []
        self.adjacency_list[node1].append(node2)
        self.adjacency_list[node2].append(node1)
    
    def display(self):
        for k in self.adjacency_list.keys():
            print(f"{k} -> {self.adjacency_list[k]}")

def main():

    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 4)
    g.display()
if __name__ == "__main__":
    main()
