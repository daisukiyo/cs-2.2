from itertools import islice


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

    def addNeighbor(self, vertex, weight=0):
        """Add a neighbor as well as its weighted edge."""
        if vertex not in self.neighbors:
            self.neighbors[vertex] = weight

    def __str__(self):
        """Output the list of adjacent values (neighbors) of this vertex."""
        return str(self.id) + " adj to " + str([x.id for x in self.neighbors])

    def getNeighbors(self):
        """Return the neighbors of this vertex."""
        return self.neighbors

    def getId(self):
        """Return the id of this vertex."""
        return self.id

    def getEdgeWeight(self, vertex):
        """Return the weight of this edge."""
        return self.neighbors[vertex]

    def getEdges(self):
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
        self.vertList = {}
        self.vertCount = 0

    def addVertex(self, key):
        """Add a new vertex object to the graph with its respective key."""
        self.vertCount += 1
        addedVertex = Vertex(key)
        self.vertList[key] = addedVertex
        return addedVertex

    def getVertex(self, key):
        """Return the vertex if it exists."""
        if key in self.vertList:
            return self.vertList[key]
        else:
            return None

    def addEdge(self, f, t, cost=0):
        """Add an edge from vertex f(from) to vertex t (to) with a cost."""
        if f not in self.vertList:
            self.addVertex(f)
        if t not in self.vertList:
            self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        """Return all the vertices in the graph."""
        return self.vertList.keys()

    def __iter__(self):
        """Iterate over the vertext objects in the graph."""
        return iter(self.vertList.values())

    def getAllEdges(self):
        """Return the sum of all unique edges from every vertex."""
        sum = 0
        for vertex in self:
            sum += vertex.getEdges()
        return sum


if __name__ == "__main__":

    # IMPORT DATA FROM TEXT FILE
    graphData = "graph_data.txt"

    # CONVERTS THE 2ND LINE (VERTICES) INTO A LIST OF VERTICES
    verticeList = list(open(graphData).readlines()[1].strip().split(","))

    # CONVERTS EVERY LINE AFTER THE 2ND INTO A 2D-ARRAY OF CONNECTIONS
    with open(graphData) as gd:
        edgeList = []
        for line in islice(gd, 2, None):
            tripletString = (line.strip())
            edgeList.append((list(tripletString.strip("()").split(","))))

    # CREATE GRAPH DATA STRUCTURE
    g = Graph()

    # ITERATE THROUGH LIST OF VERTICES
    for vertex in verticeList:
        # ADD EACH VERTEX TO GRAPH
        g.addVertex(vertex)

    # ITERATE THROUGH LIST OF EDGES
    for edge in edgeList:
        g.addEdge(edge[0], edge[1], edge[2])

    # DISPLAY NUMBER OF VERTICES
    print("# Vertices: " + str(len(verticeList)))
    # DISPLAY NUMBER OF EDGES
    print("# Edges: " + str(g.getAllEdges()))
    # DISPLAY EDGE LIST
    print("Edge List:")
    for v in g:
        for w in v.getNeighbors():
            print("(%s,%s,%s)" % (v.getId(), w.getId(), v.getEdgeWeight(w)))
