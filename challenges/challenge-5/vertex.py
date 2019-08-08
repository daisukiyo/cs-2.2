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

    def __repr__(self):
        return 'Vertex({!r})'.format(self.id)

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