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


    print("Question #1: Which player has had the most teammates?")
    print("Answer: %s with %s teammates." % (g.journeyman()[0], g.journeyman()[1]))
    print("\nQuestion #2: Which two players have the most chemistry?")
    print("Answer: %s & %s - %s Years as Teammates." % (g.chemistry()[1], g.chemistry()[2], g.chemistry()[0]))
    print("\nQuestion #3: Largest potential team?")
    player = input("Enter a player's name to find their largest potential team. \nLeave blank for a random player: ").title()
    print("Answer: %s" % ', '.join(g.clique(player)))


    