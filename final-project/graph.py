import random
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

    def journeyman(self):
        """Returns the vertice with the most connections."""
        most_tm = 0 # most teammates
        journeyman = ""
        for vertice in self.vertList.values():
            vertice_tm = len(vertice.get_neighbors()) # current vertice's teammate
            if  most_tm < vertice_tm :
                journeyman = vertice.id
                most_tm = vertice_tm
        return (journeyman, most_tm)

    def chemistry(self):
        """Returns the vertice with the heaviest edge"""
        years_played = tuple([0, "playerA", "playerB"])
        for vertice in self.vertList.values():
            for neighbor in vertice.get_neighbors():
                if neighbor.get_edge_wt(vertice) > years_played[0]:
                    years_played = (neighbor.get_edge_wt(vertice), vertice.get_id(), neighbor.get_id())
        print(years_played)

    def large_team(self):
        rand_key = random.choice(self.vertList.keys())
        clique = set(rand_key)
        vertList = [(k, v) for k, v in self.vertList.items() if k != rand_key]

        # iterate over remaining vertices
        for id, vtx in vertList:
            for neighbor in vtx.get_neighbors(as_string=True):
                if neighbor in clique:
                    clique.add(id)

        # return clique
        return clique