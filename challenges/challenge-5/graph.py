import vertex
import sys

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

    def recursive_dfs(self, start, end, visited=None, path=None):
        """Determine if there is a path between two vertices.

        Parameters:
            start (): the starting vertice
            end (): the ending vertice
            visited (set): unique vertices that have been visited
            path (list): vertices of the path

        Returns:
            Bool: Whether or not a path exists
        
        Analysis:
            Time Complexity: O(m + n)
            Space Complexity: O(n)
        
        """
        # initialize path list with starting vertice
        if path is None:
            path = [start]

        # initialize empty set for visited vertices
        if visited is None:
           visited = set()
      
        # add starting vertice to visited vertices
        visited.add(start)

        # store all neighbors of start vertice in set
        neighbors = set([x for x in start.get_neighbors()])
        
        # initialize loop count as 0
        loop_count = 0

        # iterate through vertices
        for next in neighbors - visited:
            # remove visited path if it results in a dead end (incomplete)
            if loop_count > 0:
                path.pop()

            # add to list of visited vertices
            path.append(next)

            # full path completed
            if next == end:
                visited.add(next)
                ordered_vertice_path = ([(x.id) for x in path])
                print("There exists a path between vertex %s and %s: TRUE" %(sys.argv[2], sys.argv[3]))
                print("Vertices in the path:", ','.join(ordered_vertice_path))
                return True

            loop_count += 1

            self.recursive_dfs(next, end, visited, path)

    def eulerian(self):
        """ Returns whether or not a graph contains a Eulerian Cycle"""
        for vertex in self.vertList.values():
            if len(vertex.neighbors.keys()) % 2 != 0:
                return False
        return True
    