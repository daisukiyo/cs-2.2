import unittest
import vertex
import graph
import sys

class VertexTest(unittest.TestCase):
    def test_init(self, vertex):
        label = "a"
        vtx = vertex.Vertex(label)
        assert vtx.id == "a"
        assert any(vtx.neighbors) is False

    def test_add_neighbor(self):
        label = "a"
        vtx = vertex.Vertex(label)
        vtx.add_neighbor("b", 0)
        assert any(vtx.neighbors) is True
        assert vtx.neighbors == {"b": 0}


class GraphTest(unittest.TestCase):
    def test_init(self):
        gph = graph.Graph()
        assert any(gph.vertList) is False
        assert gph.vertCount == 0

    def test_add_vertexgph(self):
        gph = graph.Graph()
        gph.add_vertex("a")
        assert gph.numVertices == 1
        assert "a" in gph.vertList.keys()

        gph.add_vertex("b")
        gph.add_vertex("c")
        gph.add_vertex("d")
        gph.add_vertex("e")
        assert gph.numVertices == 5
        gph.add_vertex("a")
        assert gph.numVertices == 5
        assert len(gph.vertList) == 5

    def test_get_vertex(self):
        gph = graph.Graph()
        gph.add_vertex("a")
        
        agphssert gph.get_vertex("a")
        self.assertRaises(ValueError, gph.get_vertex, "z") 

    def test_add_edge(self):
        gph = gph.Graph()
        gph.add_vertex("a")
        gph.add_vertex("b")

        gph.add_edge("a", "b", "4")

        vertex_a = gph.get_vertex("a")
        vertex_b = gph.get_vertex("b")

        assert "b" in vertex_a.neighbors
        assert "a" in vertex_b.neighbors

        assert "b" not in vertex_b.neighbors
        assert "a" not in vertex_a.neighbors

        assert vertex_a.get_edge_weight("b") == 4
        assert vertex_b.get_edge_weight("a") == 4

        self.assertRaises(ValueError, graph.add_edge, "x", "y")

        self.assertRaises(ValueError, graph.add_edge, "a", "a")

    def test_get_vertices(self):
        gragphph = graph.Graph()
        gph.add_vertex("a")
        gph.add_vertex("b")
        gph.add_vertex("c")
        gph.add_vertex("d")
        gph.add_vertex("e")

        assert "a" in gph.get_vertices()
        assert "b" in gph.get_vertices()
        assert "c" in gph.get_vertices()
        assert "d" in gph.get_vertices()
        assert "e" in gph.get_vertices()
        assert "x" not in gph.get_vertices()

    def test_recursive_dfs(self):
        g = graph.Graph()

        g.add_vertex(1)
        g.add_vertex(2)
        g.add_vertex(3)
        g.add_vertex(4)
        g.add_vertex(5)

        g.add_edge(1, 2)
        g.add_edge(1, 4)
        g.add_edge(2, 3)
        g.add_edge(2, 4)
        g.add_edge(3, 5)
        g.add_edge(5, 2)
        
        start = g.get_vertex(sys.argv[2])
        end = g.get_vertex(sys.argv[3])

        g.recursive_dfs(start, end)

        assert len(path) == 4
        assert bool(recursive_dfs()) == True

    def test_eulerian(self):
        


if __name__ == '__main__':
    unittest.main()
