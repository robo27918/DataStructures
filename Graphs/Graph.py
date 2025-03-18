from collections import defaultdict
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
        seen.add(start_node)
        while stack:
            currNode = stack.pop()
            print(currNode)
            for neighbor in graph[currNode]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    stack.append(neighbor)
    
    def hasCycle(self,graph,start_node):
        '''
            #my assumption is it doesnt matter where you start
            use dfs to explore
            in the for loop if at any point we run into a neigbor that is in the seen set
            and its parent 
        '''
        parent_map = {}
        parent_map[start_node] = None #key is th current node , value is the parent
        stack = [start_node]
        seen = {start_node}
        
        while stack:
            currNode = stack.pop()
           
            # do some processing

            for neighbor in graph[currNode]:
                
              
                if neighbor not in seen:
                    seen.add(neighbor)
                    stack.append(neighbor)
                    parent_map[neighbor] = currNode
                elif neighbor != parent_map[currNode]:
                    #parent_map[currNode] = neighbor
                    print("parent_map",parent_map)
                    print("Cycle detected..")
                    print(currNode,neighbor)
                    return True
                    
        return False
    
    def displayCyclePath(self,graph,start_node):
        parent_map = {start_node:None}
        seen = {start_node}
        stack = [start_node]
        while stack:
            curNode = stack.pop()
            for neighbor in graph[curNode]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    stack.append(neighbor)
                    parent_map[neighbor] = curNode
                elif neighbor != parent_map[curNode]: # we are not simply detecting the parent node since this wouldn't be a cycle
                    print(parent_map)
                    # visitOrder = []
                    # endNode = parent_map[neighbor]
                    # visitOrder.append(endNode)
                    # visitOrder.append(neighbor)
                    # visitOrder.append(neighbor)
                    # visitOrder.append(curNode)

                    # while True:
                    #     if curNode == endNode:
                    #         break
                    #     visitOrder.append(curNode)
                    #     curNode = parent_map[curNode]
                    #     visitOrder.append(curNode)

                       
                    # order_str =''
                    # for i in range(0,len(visitOrder),2):
                    #     order_str += f'({visitOrder[i]} -> {visitOrder[i+1]})'
                    # print(order_str)

                    cycle_path = []
                    x = curNode
                    while x!= neighbor:
                        cycle_path.append(x)
                        x = parent_map[x]
                    cycle_path.append(neighbor)
                    cycle_path.reverse()

                    order_str = " -> ".join(cycle_path) + f' -> {neighbor}'
                    print('cycle detected', order_str)
                    

        

        


def main():
    graph = {
    'A': ['B'],
    'B': ['C'],
    'C': ['D'],
    'D': ['G'],
    'G': ['E'],
    'E': ['F'],
    'F': ['B']  # Cycle back to B
    }
    graph1 = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A'],
    'D': ['B'],
    'E': ['B']
    }
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(1, 0)
    g.add_edge(2, 3)
    g.add_edge(2,0)
    g.add_edge(2, 4)
    # g.display()
    print(g.displayCyclePath(graph,'A'))

if __name__ == "__main__":
    main()
