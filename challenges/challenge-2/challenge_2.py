from itertools import islice
import sys

class Vertex:
    """A helper class designated for the graph class.

    Defines vertices and vertex neighbors
    """

    def __init__(self, vertex):
        """Initialize a vertex with its respective neighbors.

        Each vertex uses a dictionary to keep track of the vertices to which it
        is connected, and the weight of each edge.

        The key is the vertex

        The value is the weight of edge between self and neighbor

        """
        self.id = vertex
        self.neighbors = {}

    def add_neighbor(self, vertex, weight=0):
        """Add a neighbor as well as its weighted edge."""
        if vertex not in self.neighbors:
            self.neighbors[vertex] = weight

    def __str__(self):
        """Output the list of adjacent values (neighbors) of this vertex."""
        return str(self.id) + " adj to " + str([x.id for x in self.neighbors])

    def get_neighbors(self):
        """Return the neighbors of this vertex."""
        return self.neighbors

    def get_id(self):
        """Return the id of this vertex."""
        return self.id

    def get_edge_wt(self, vertex):
        """Return the weight of this edge."""
        return self.neighbors[vertex]

    def get_edges(self):
        """Get the edges of this vertex."""
        return len(self.neighbors.keys())


class Graph:
    """Create a new, empty graph.

    The following graph abastract data type is implemented via adjacency list

    Positives: Easy to solve graph traversal problems

    Negatives: Time to find edges is slightly more than in adjacency matrix

    """

    def __init__(self):
        """Initialize a graph object with an empty dictionary."""
        self.vert_list = {}
        self.vert_count = 0

    def add_vertex(self, key):
        """Add a new vertex object to the graph with its respective key."""
        self.vert_count += 1
        added_vertex = Vertex(key)
        self.vert_list[key] = added_vertex
        return added_vertex

    def get_vertex(self, key):
        """Return the vertex if it exists."""
        if key in self.vert_list:
            return self.vert_list[key]
        else:
            return None

    def add_edge(self, f, t, cost=1):
        """Add an edge from vertex f(from) to vertex t (to) with a cost."""
        if f not in self.vert_list:
            self.add_vertex(f)
        if t not in self.vert_list:
            self.add_vertex(t)
        self.vert_list[f].add_neighbor(self.vert_list[t], cost)

    def get_vertices(self):
        """Return all the vertices in the graph."""
        return self.vert_list.keys()

    def __iter__(self):
        """Iterate over the vertext objects in the graph."""
        return iter(self.vert_list.values())

    def get_all_edges(self):
        """Return the sum of all unique edges from every vertex."""
        sum = 0
        for vertex in self:
            sum += vertex.get_edges()
        return sum

    def breadth_first_search(self, start, end):
        """Compute the shortest path between two provided vertices in the graph.

        Runtime: n+m
        
        """
        visited = []
        bfs_queue = []
        path_trace= {}
        path = []
        distance = 0
        bfs_queue.append(start)
        visited.append(start)
        current_neighbor_count = 1
        while bfs_queue:
            while current_neighbor_count > 0:
                current_neighbor_count -= 1
                current_node = bfs_queue.pop(0)
                if current_node == end:
                    print("Vertices in shortest path: " + str(",".join(path)))
                    print("Number of edges in shortest path: " + str(distance))
                    return distance
                if self.vert_list[current_node]:
                    for i in [x.id for x in self.get_vertex(current_node).neighbors]:
                        if i not in visited:
                            bfs_queue.append(i)
                            visited.append(i)
                            path_trace[i] = current_node
                            if (i == end):
                                backwalk_id = end
                                while backwalk_id != start:
                                    path.insert(0, backwalk_id)
                                    backwalk_id = path_trace[backwalk_id]
                                path.insert(0, backwalk_id)

            current_neighbor_count = len(bfs_queue)
            distance += 1
            
        

if __name__ == "__main__":

    # IMPORT DATA FROM TEXT FILE
    graph_data = sys.argv[1]

    # CONVERTS THE 2ND LINE (VERTICES) INTO A LIST OF VERTICES
    vertice_list = list(open(graph_data).readlines()[1].strip().split(","))

    # CONVERTS EVERY LINE AFTER THE 2ND INTO A 2D-ARRAY OF CONNECTIONS
    with open(graph_data) as gd:
        edge_list = []
        for line in islice(gd, 2, None):
            triplet_string = (line.strip())
            edge_list.append((list(triplet_string.strip("()").split(","))))

    # CREATE GRAPH DATA STRUCTURE
    g = Graph()

    # ITERATE THROUGH LIST OF VERTICES
    for vertex in vertice_list:
        # ADD EACH VERTEX TO GRAPH
        g.add_vertex(vertex)

    # ITERATE THROUGH LIST OF EDGES
    for edge in edge_list:
        g.add_edge(edge[0], edge[1])

    g.breadth_first_search(sys.argv[2], sys.argv[3])