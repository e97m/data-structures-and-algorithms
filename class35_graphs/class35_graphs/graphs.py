
class Node:
    '''
    A class to create a node
    Input: the value of the data for the node.
    constructor: vlaue, next (pointer to the next)
    '''
    def __init__(self,value):
        self.value = value
        self.next = None


class Queue:
    '''
    A class to creat a queue
    Input: no input
    constructor: front node, rear node
    '''

    def __init__(self):
        self.front = None
        self.rear = None

    
    def enqueue(self, new_value):
        '''
        A method to add a node to the queue (to the rear)
        Input: new value
        '''
        if type(new_value) is Node:
            return 'Please enter a value and it will converted to Node automaticly'
        else:
            new_node = Node(new_value)
        if not self.front:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node


    def dequeue(self):
        '''
        A method to remove a node from the queue (from front)
        Input: nothing
        '''
        if self.is_empty():
            return 'The queue is empty'
        else:
            old_front = self.front
            self.front = self.front.next
            old_front.next = None
        return old_front.value


    
    def peek(self):
        '''
        A method to show the front of the queue
        '''
        if self.is_empty():
            return 'The queue is empty'
        else:
            return self.front.value
    

    def is_empty(self):
        '''
        A method to check if the queue is empty or not
        Input: nothing
        Output: boolian (True if the queue is empty)
        '''
        if self.front is None:
            return True
        else:
            return False


class Stack:
    '''
    A class to creat a stack
    Input: no input
    constructor: top node
    '''

    def __init__(self):
        self.top = None


    def push(self, new_value):
        '''
        A method to add a node to the stack
        Input: new_value
        '''
        if type(new_value) is Node:
            return 'Please enter a value and it will converted to Node automaticly'
        else:
            new_node = Node(new_value)
        new_node.next = self.top
        self.top = new_node
    

    def pop(self):
        '''
        A method to remove a node from the stack
        Input: nothing
        '''
        if self.is_empty():
            return 'The stack is empty'
        old_top = self.top
        self.top = self.top.next
        old_top.next = None
        return old_top.value


    def peek(self):
        '''
        A method to show the top of the stack
        '''
        if self.is_empty():
            return 'The stack is empty'
        else:
            return self.top.value
    

    def is_empty(self):
        '''
        A method to check if the stack is empty or not
        Input: nothing
        Output: boolian (True if the stack is empty)
        '''
        if self.top is None:
            return True
        else:
            return False


class Vertex:
    '''
    A class to creat a vertex
    Input: no input
    constructor: value, edges (list of edges)
    '''
    def __init__(self, value):
        self.value = value
        self.edges = []


class Graph:
    def __init__(self):
        self.adjacency_list = {}


    def add_node(self, value):
        '''
        Add a node (vertex) to the graph
        Input: value
        output: the added node (vertex)
        '''
        new_vertex = Vertex(value)
        self.adjacency_list[value] = new_vertex
        return new_vertex


    def add_edge(self, vertex1, vertex2, weight=None):
        '''
        Adds a new edge between two nodes (vertecies) in the graph
        Input: vertex1, vertex2, weight
        output: nothing
        '''
        if vertex1 not in self.adjacency_list:
            self.add_node(vertex1)
        if vertex2 not in self.adjacency_list:
            self.add_node(vertex2)
        if weight is None:
            self.adjacency_list[vertex1].edges.append(vertex2)
            self.adjacency_list[vertex2].edges.append(vertex1)
        else:
            self.adjacency_list[vertex1].edges.append((vertex2, weight))
            self.adjacency_list[vertex2].edges.append((vertex1, weight))

 
    def get_nodes(self):
        '''
        Returns all of the nodes (verticies) in the graph as a collection
        Input: nothing
        output: set of nodes (verticies)
        '''
        verticies = set()
        for key in self.adjacency_list:
            verticies.add(key)
        return verticies


    
    def get_neighbors(self, vertex):
        '''
        Returns a collection of edges connected to the given node (vertex) including the weight of the connection
        Input: node (vertex)
        output: collection of edges
        '''
        return self.adjacency_list[vertex].edges


    def size(self):
        '''
        Returns the total number of nodes (verticies) in the graph
        Input: nothing
        output: int (number of nodes/verticies)
        '''
        return len(self.adjacency_list)


    def breadth_first(self, vertex):
        '''
        Returns a collection of nodes in the graph starting from the given node in breadth first order
        Input: vertex
        output: collection of nodes (verticies)
        '''
        verticies = []
        breadth = Queue()
        visited = set()
        breadth.enqueue(vertex)
        visited.add(vertex)
        while not breadth.is_empty():
            front = breadth.dequeue()
            verticies.append(front)
            for neighbor in self.get_neighbors(front):
                if neighbor not in visited:
                    breadth.enqueue(neighbor)
                    visited.add(neighbor)
        return verticies


    def depth_first(self, vertex):
        '''
        Returns a collection of nodes in the graph starting from the given node in depth first order
        Input: vertex
        output: collection of nodes (verticies)
        '''
        verticies = []
        depth = Stack()
        visited = set()
        depth.push(vertex)
        visited.add(vertex)
        while depth.is_empty() is not True:
            top = depth.pop()
            verticies.append(top)
            for neighbor in self.get_neighbors(top):
                if neighbor not in visited:
                    depth.push(neighbor)
                    visited.add(neighbor)
        return verticies


    def __str__(self):
        '''
        print the adjacency list of the graoh
        '''
        output = '\n' + 'vertex :  edges \n'
        for key in self.adjacency_list:
            output += f'{key}      :  {self.adjacency_list[key].edges}  \n'
        return  output


if __name__ == '__main__':
    graph = Graph()
    graph.add_node(0)
    graph.add_node('1')
    graph.add_node(2)
    graph.add_node(3)
    graph.add_edge(0, '1')
    graph.add_edge(0, 2)
    graph.add_edge('1', 2)
    graph.add_edge(2, 0)
    graph.add_edge(2, 3)
    graph.add_edge(3, 3)
    print(graph)
    print(graph.get_neighbors(2))
    print(graph.size())
    print(graph.breadth_first(2))
    print(graph.depth_first(2))