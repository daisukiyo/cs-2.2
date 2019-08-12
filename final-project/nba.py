import graph
import sys
from itertools import islice

if __name__ == "__main__":

    # IMPORT DATA FROM TEXT FILE
    graph_data = sys.argv[1]
    
    with open(graph_data) as gd:
        vertice_list = []
        for line in islice(gd, 0, 30):
            vertice_list.append(line.strip())

    # CONVERTS EVERY LINE AFTER THE 2ND INTO A 2D-ARRAY OF CONNECTIONS
    with open(graph_data) as gd:
        edge_list = []
        for line in islice(gd, 31, None):
            triplet_string = (line.strip())
            edge_list.append((list(triplet_string.strip("()").split(","))))

    # CREATE GRAPH DATA STRUCTURE
    g = graph.Graph()

    # ITERATE THROUGH LIST OF VERTICES
    for vertex in vertice_list:
        # ADD EACH VERTEX TO GRAPH
        g.add_vertex(vertex)

    # ITERATE THROUGH LIST OF EDGES
    for edge in edge_list:
        g.add_edge(edge[0].strip(), edge[1].strip(), int(edge[2]))
        g.add_edge(edge[1].strip(), edge[0].strip(), int(edge[2]))

    # # DISPLAY NUMBER OF VERTICES
    # print("# Vertices: " + str(len(vertice_list)))
    # # DISPLAY NUMBER OF EDGES
    # print("# Edges: " + str(g.get_all_edges()))
    # # DISPLAY EDGE LIST
    # print("Edge List:")
    # for v in g:
    #     for w in v.get_neighbors():
    #         print("(%s, %s, %s)" % (v.get_id(), w.get_id(), v.get_edge_wt(w)))

    print("Question #1: Which player has had the most teammates?")
    print("Answer: %s with %s teammates." % (g.journeyman()[0], g.journeyman()[1]))
    print("Question #2: Which two players have the most chemistry?")
    g.chemistry()
    print("Question #3: Largest potential team?")
    # g.large_team()

    