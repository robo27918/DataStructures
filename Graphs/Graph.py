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
    def bfs(self,graph,start_node,end=None):
        visited = set()
        q = [] #first in first out
        q.append(start_node)
        visited.add(start_node)

        while q:
            curr_node = q.pop(0)# fifo
            print(curr_node) # or process it
            for neighbor in graph[curr_node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)
    def dfs(self,graph,start_node,end_node=None):
        stack = []
        seen = set()
        stack.append(start_node)
        while stack:
            currNode = stack.pop()
            print(currNode)
            for neighbor in graph[currNode]:
                if neighbor not in seen:
                    seen.add(currNode)
                    stack.append(currNode)
            




def main():

    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(1, 0)
    g.add_edge(2, 3)
    g.add_edge(2,0)
    g.add_edge(2, 4)
    g.display()
    g.bfs(g.adjacency_list,0)

if __name__ == "__main__":
    main()
