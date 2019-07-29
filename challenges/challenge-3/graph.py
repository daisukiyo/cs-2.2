import vertex

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

    def add_vertex(self, key):
        """Add a new vertex object to the graph with its respective key."""
        self.vertCount += 1
        addedVertex = vertex.Vertex(key)
        self.vertList[key] = addedVertex
        return addedVertex

    def get_vertex(self, key):
        """Return the vertex if it exists."""
        if key in self.vertList:
            return self.vertList[key]
        else:
            return None

    def add_edge(self, f, t, cost=1):
        """Add an edge from vertex f(from) to vertex t (to) with a cost."""
        if f not in self.vertList:
            self.add_vertex(f)
        if t not in self.vertList:
            self.add_vertex(t)
        self.vertList[f].add_neighbor(self.vertList[t], cost)

    def get_vertices(self):
        """Return all the vertices in the graph."""
        return self.vertList.keys()

    def __iter__(self):
        """Iterate over the vertext objects in the graph."""
        return iter(self.vertList.values())

    def get_all_edges(self):
        """Return the sum of all unique edges from every vertex."""
        sum = 0
        for vertex in self:
            sum += vertex.get_edges()
        return sum

    def recursive_dfs(self, start, end, visited=None):
       
        if visited is None:
           visited = set()
      
        # print(start)
        visited.add(start)
        # print(visited)

        neighbors = set([x for x in start.get_neighbors()])
 
        for next in neighbors - visited:
            if next == end:
                visited.add(next)
                print("There exists a path between vertex 1 and 5: TRUE")
                print("Vertices in the path:", [int(x.id) for x in visited])
            # else:
            #     print("There exists a path between vertex 1 and 5: FALSE")
            self.recursive_dfs(next, end, visited)
        
        # return visited