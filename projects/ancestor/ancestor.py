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
                    print(neighbor)
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
        # path = path + [starting_vertex]
        # print('this is path', path)
        new_path = list(path)
        new_path.append(starting_vertex)

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
def earliest_ancestor(ancestors, starting_node):
#     # print('this is ancestors', ancestors)
#     '''
#        10
#      /
#     1   2   4  11
#      \ /   / \ /
#       3   5   8
#        \ / \   \
#         6   7   9
#     '''
# Create an empty queue and enqueue A PATH TO the starting vertex ID
        q = Queue()
        q.enqueue([starting_node])
		# Create a Set to store visited vertices
        visited = {}
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
                for parent, child in ancestors:
				# Mark it as visited...
                    visited[last_vertex] = child
                    print(visited)
				# Then add A PATH TO its neighbors to the back of the queue
                # how to get the neighbor of this
                    print('this is last_vertex', last_vertex)
                    print('this is parent', parent)
                    # print(neighbor)
				    # COPY THE PATH
                    new_path = list(path)
				    # APPEND THE NEIGHOR TO THE BACK
                    new_path.append(parent)
                    q.enqueue(new_path)
#     # [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
#     # get parent child
#     # print('starting Node', starting_node)
    # for parent, child in ancestors:
    #     # get the child if it equals the starting node
    #     # so if 1 pass in the child of 10 is 1
    #     # if a child to the starting node exists it will continue
    #     if child == starting_node:
    #         # print(child)
    #         # pass in the parent
    #         # so if 1 passed in the parent of 1 is 10
    #         #set it to true so we can go through the if statement
    #         return earliest_ancestor(ancestors, parent, True)
    # if ancestor == True:
    #     # return the starting node
    #     # we passed in parent so we would return the parent of the child
    #     return starting_node
    # else:
    #     # if it doesnt equal true return -1
    #     return -1
        #given the dataset and the ID of an individual in the dataset
        #returns their earliest known ancestor  
        #the one at the farthest distance from the input individual.
        #If there is more than one ancestor tied for "earliest"
            #return the one with the lowest numeric ID
            #If the input individual has no parents
                # the function should return -1
#     # def dft_recursive(self, starting_vertex, visited=None):
#     #     """
#     #     Print each vertex in depth-first order
#     #     beginning from starting_vertex.

#     #     This should be done using recursion.
#     #     """
#     #     print(starting_vertex)
#     #     if visited is None:
#     #         visited = set()
        
#     #     visited.add(starting_vertex)

#     #     for next_vert in self.get_neighbors(starting_vertex):
#     #         if next_vert not in visited:
#     #             self.dft_recursive(next_vert, visited)
#     # '''
#     # Should print:
#     #     {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
#     #     {1: {3}, 2: {3}, 3: {6}, 4: {8, 5}, 5: {6, 7}, 6: set(), 7: set(), 8: {9}, 9: set(), 10: {1}, 11: {8}}
#     # '''
    
        

        