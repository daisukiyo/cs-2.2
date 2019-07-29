import graph
import sys
from itertools import islice

if __name__ == "__main__":

    # IMPORT DATA FROM TEXT FILE
    graph_data = sys.argv[1]

    # GRAPH TYPE
    graph_type = open(graph_data).readlines()[0].strip()
    if graph_type == "G":
        graph_type = "Undirected Graph"
    elif graph_type == "D":
        graph_type = "Directed Graph"
    else:
        sys.exit("invalid graph data. please specify a type of graph.")
    
    # CONVERTS THE 2ND LINE (VERTICES) INTO A LIST OF VERTICES
    vertice_list = list(open(graph_data).readlines()[1].strip().split(","))

    # CONVERTS EVERY LINE AFTER THE 2ND INTO A 2D-ARRAY OF CONNECTIONS
    with open(graph_data) as gd:
        edge_list = []
        for line in islice(gd, 2, None):
            triplet_string = (line.strip())
            edge_list.append((list(triplet_string.strip("()").split(","))))

    # CREATE GRAPH DATA STRUCTURE
    g = graph.Graph()

    # print(vertice_list)

    # ITERATE THROUGH LIST OF VERTICES
    for vertex in vertice_list:
        # ADD EACH VERTEX TO GRAPH
        g.add_vertex(vertex)

    # ITERATE THROUGH LIST OF EDGES
    for edge in edge_list:
        g.add_edge(edge[0], edge[1])

    # # DISPLAY NUMBER OF VERTICES
    # print("# Vertices: " + str(len(vertice_list)))
    # # DISPLAY NUMBER OF EDGES
    # print("# Edges: " + str(g.get_all_edges()))
    # # DISPLAY EDGE LIST
    # print("Edge List:")
    # for v in g:
    #     for w in v.get_neighbors():
    #         print("(%s,%s)" % (v.get_id(), w.get_id()))
    start = g.get_vertex(sys.argv[2])
    end = g.get_vertex(sys.argv[3])
    g.recursive_dfs(start, end)