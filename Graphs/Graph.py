from collections import defaultdict
from collections import deque
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

    
    def dfs_recursive(self,graph,node=None):
        def dfs_visit(node,graph):
            assert isinstance(graph,dict),"graph is not a dict"
            for neighbor in graph[node]:
                if neighbor not in parent:
                    parent[neighbor] = node
                    dfs_visit(neighbor,graph)
        parent = {}
        if node != None:
            parent[node]=None
            dfs_visit(node,graph)
        else:
            for node in graph:
                if node not in parent:
                    parent[node]= None
                    dfs_visit(node,graph)
        return parent
          
    def topological_sort(self,graph):
        '''
            Retunrs False if no cycle detected, otherwise True for cycle detection
        '''
        def dfs_visit(node,graph):
            assert isinstance(graph,dict),"graph is not a dictionary"
          
            if perm_marks[node]:
                return False
            if temp_marks[node]:
                return True
            temp_marks[node] = True
            for neighbor in graph[node]:
               
               if dfs_visit(neighbor,graph):
                   return True
            perm_marks[node] = True
          
            sort_list.appendleft(node)
            return False
        
        
         #left val= temp_mark,right_val= perm_mark
        temp_marks = defaultdict()
        perm_marks = defaultdict()
        for node in graph:
            temp_marks[node] =False
            perm_marks[node] =False
        sort_list = deque()
        
    
        for node in graph:
            if not temp_marks[node]:
                if dfs_visit(node,graph):
                    return "Graph is cyclic, no topological sort possible"
        return sort_list
    
    
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
    def findShortestPath(self,graph,srcNode,destNode):
        '''
            finding path use breadth-first search
        '''
        parentMap = {srcNode:None}
        seen = {srcNode}
        queue =[srcNode]

        while queue:
            curNode = queue.pop(0)
            
            for neighbor in graph[curNode]:
                if neighbor == destNode:
                    
                    parentMap[neighbor] = curNode
                    path = []
                    x = curNode
                    path.append(neighbor)
                    while x!= None:

                        path.append(x)
                        x = parentMap[x]
                  
                  
                    path = path [::-1]
                
                    return path
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)
                    parentMap[neighbor] = curNode
                
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
    graph3 = {
        'A':['B','D',],
        'B':['A','C',],
        'C': ["B",'F'],
        'D':["A","E"],
        'E': ['D','F'],
        "F":["E",'C'],
    }
    dag= {
        1:[2],
        2: [3],
        3:[1],
    
    

    }
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(1, 0)
    g.add_edge(2, 3)
    g.add_edge(2,0)
    g.add_edge(2, 4)
    # g.display()
    print(g.adjacency_list)
    print()
    g.dfs(g.adjacency_list,start_node=1)
    print()
    print(g.dfs_recursive(g.adjacency_list,0))
    print()
    print(g.topological_sort(dag))


if __name__ == "__main__":
    main()
