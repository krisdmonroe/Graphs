class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)
class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()  # set of edges from this vert

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    print(graph.vertices)
    for parent, child in ancestors:
        graph.add_vertex(parent)
        graph.add_vertex(child)
        graph.add_edge(child, parent)

    q = Queue()
    q.enqueue([starting_node])
    farthest = 1
    ancestor = -1
	# While the queue is not empty...
    while q.size() > 0:
		# Dequeue the first PATH
        path = q.dequeue()
        # print('this is path', path)
		# Grab the last vertex from the PATH
        last_vertex = path[-1]
        # print('this is vertex', vertex)
        # find the longest path here
        if len(path) >= farthest and last_vertex < ancestor or len(path) > farthest:
            ancestor = last_vertex
            farthest = len(path)
			# Then add A PATH TO its neighbors to the back of the queue
        for neighbor in graph.vertices[last_vertex]:
            # print(neighbor)
            # COPY THE PATH
            new_path = list(path)
            # APPEND THE NEIGHOR TO THE BACK
            new_path.append(neighbor)
            q.enqueue(new_path)
            # print(graph.vertices)
    return ancestor

if __name__ == "__main__":
    test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

    print(earliest_ancestor(test_ancestors, 3)) 
