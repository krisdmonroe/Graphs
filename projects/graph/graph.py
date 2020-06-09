"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()  # set of edges from this vert

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty queue and enqueue the starting vertex ID
        q = Queue()
        q.enqueue(starting_vertex)

		# Create a Set to store visited vertices
        visited = set()

		# While the queue is not empty...
        while q.size() > 0:
			# Dequeue the first vertex
            v = q.dequeue()
			# If that vertex has not been visited...
            if v not in visited:
				# Visit it
                print(v)

				# Mark it as visited...
                visited.add(v)

				# Then add all of its neighbors to the back of the queue
                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        #use a stack instead of a queue, enque becomes push and deque becomes pop
        s = Stack()
        s.push(starting_vertex)

        visited = set()

        while s.size() > 0:
            v = s.pop()
            if v not in visited:
                print(v)
                visited.add(v)
                for next_vert in self.get_neighbors(v):
                    s.push(next_vert)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        print(starting_vertex)
        if visited is None:
            visited = set()
        
        visited.add(starting_vertex)

        for next_vert in self.get_neighbors(starting_vertex):
            if next_vert not in visited:
                self.dft_recursive(next_vert, visited)
        



    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        q = Queue()
        q.enqueue([starting_vertex])
		# Create a Set to store visited vertices
        visited = set()
		# While the queue is not empty...
        while q.size() > 0:
			# Dequeue the first PATH
            path = q.dequeue()
            # print('this is path', path)
			# Grab the last vertex from the PATH
            last_vertex = path[-1]
            # print('this is vertex', vertex)
			# If that vertex has not been visited...
            if last_vertex not in visited:
				# CHECK IF IT'S THE TARGET
                if last_vertex == destination_vertex:
				  # IF SO, RETURN PATH
                    return path
				# Mark it as visited...
                visited.add(last_vertex)
				# Then add A PATH TO its neighbors to the back of the queue
                for neighbor in self.get_neighbors(last_vertex):
                    # print(neighbor)
				    # COPY THE PATH
                    new_path = list(path)
				    # APPEND THE NEIGHOR TO THE BACK
                    new_path.append(neighbor)
                    q.enqueue(new_path)
#cleaner more helpful version------------------------------------
# # Create a queue and enqueue starting vertex
#         q = Queue()
#         # Enqueues the starting vertex
#         q.enqueue([starting_vertex]) # creates an array
#         # Create a set to store the vertices
#         visited = set()
#         # While the queue is not empty
#         while q.size() > 0:
#             # dequeue the first path
#             #Since creating a path, order matters
#             path = q.dequeue()
#             # grab the vertex from the end of the path
#             vertex = path[-1]
#             # check if it's been visited
#             # if it hasn't been
#             if vertex not in visited:
#                 # mark as visited
#                 visited.add(vertex)
#                 # check if it is the "target"
#                 if vertex == destination_vertex:
#                     # if it is, return the path
#                     return path
#                 # enqueue a path to all neighbors
#                 for neighbor in self.get_neighbors(vertex):
#                     #make a copy of the path
#                     new_path = list(path) #constructor built in python
#                     # adds the copy
#                     new_path.append(neighbor)
#                     q.enqueue(new_path)

                    


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        #give right answer not right way to solve
        # s = Stack()
        # s.push(starting_vertex)

        # visited = []
        
        # while s.size() > 0:
        #     v = s.pop()
        #     if v not in visited:
        #         print(v)
        #         if v == destination_vertex:
        #             return visited
        #         visited.append(v)
        #         for next_vert in self.get_neighbors(v):
        #             s.push(next_vert)
        #             if next_vert == destination_vertex:
        #                 visited.append(next_vert)
        #                 return visited
# -----------------------------------------------------------------
        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        s = Stack()
        s.push([starting_vertex])
		# Create a Set to store visited vertices
        visited = set()
		# While the queue is not empty...
        while s.size() > 0:
			# Dequeue the first PATH
            path = s.pop()
            # print('this is path', path)
			# Grab the last vertex from the PATH
            last_vertex = path[-1]
            # print('this is vertex', vertex)
			# If that vertex has not been visited...
            if last_vertex not in visited:
				# CHECK IF IT'S THE TARGET
                if last_vertex == destination_vertex:
				  # IF SO, RETURN PATH
                    return path
				# Mark it as visited...
                visited.add(last_vertex)
				# Then add A PATH TO its neighbors to the back of the queue
                for neighbor in self.get_neighbors(last_vertex):
                    # print(neighbor)
				    # COPY THE PATH
                    new_path = list(path)
				    # APPEND THE NEIGHOR TO THE BACK
                    new_path.append(neighbor)
                    s.push(new_path)
                    # or ---------------------
                    # s.push(path + [neighbor])

    def dfs_recursive(self, starting_vertex, destination_vertex, path=None, visited=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()

        if path is None:
            path = []
            
        visited.add(starting_vertex)
        path = path + [starting_vertex]
        # print('this is path', path)

        if starting_vertex == destination_vertex:
            return path

        for next_vert in self.get_neighbors(starting_vertex):
            if next_vert not in visited:
                new = self.dfs_recursive(next_vert, destination_vertex,path=path,visited=visited)

                if new is not None:
                    return new
        
        # # Starting out with visited defaulting to None
        # if visited is None:
        #     # returns an empty set
        #     visited = set()
        # # Start the path with default of None
        # if path is None:
        #     # The path will then return an empty list
        #     path = []
        # # Check if vertex (node) has been visited
        # if starting_vertex not in visited:
        #     visited.add(starting_vertex) 
        #     # make a copy of the path
        #     new_path = list(path)
        #     #or can use
        #     #path = path + [starting_vertex] and won't need line 228
        #     # add the copied path to the starting_vertex
        #     new_path.append(starting_vertex)
        #     # Checks if the starting_vertex and destination_vertex are the same
        #     if starting_vertex == destination_vertex:
        #         # if it is, then return the new_path
        #         return new_path
        #     for neighbor in self.get_neighbors(starting_vertex):
        #         new_dfs_path = self.dfs_recursive(neighbor, destination_vertex, visited, new_path)
        #         if new_dfs_path is not None:
        #             return new_dfs_path
        # return None

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
