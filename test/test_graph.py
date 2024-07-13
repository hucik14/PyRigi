from pyrigi.graph import Graph
import pyrigi.graphDB as graphs
from pyrigi.exception import LoopError

import pytest
from sympy import Matrix


@pytest.mark.parametrize(
    "graph",
    [
        graphs.Complete(2),
        graphs.Complete(3),
        graphs.Complete(4),
        graphs.CompleteBipartite(3, 3),
        graphs.CompleteBipartite(3, 4),
        graphs.CompleteBipartite(4, 4),
        graphs.Diamond(),
        graphs.K33plusEdge(),
        graphs.ThreePrism(),
        graphs.ThreePrismPlusEdge(),
    ],
)
def test_rigid_in_d2(graph):
    assert graph.is_rigid(dim=2, combinatorial=True)
    assert graph.is_rigid(dim=2, combinatorial=False)


@pytest.mark.parametrize(
    "graph",
    [
        graphs.CompleteBipartite(1, 3),
        graphs.CompleteBipartite(2, 3),
        graphs.Cycle(4),
        graphs.Cycle(5),
        graphs.Path(3),
        graphs.Path(4),
    ],
)
def test_not_rigid_in_d2(graph):
    assert not graph.is_rigid(dim=2, combinatorial=True)
    assert not graph.is_rigid(dim=2, combinatorial=False)


@pytest.mark.parametrize(
    "graph",
    [
        graphs.CompleteBipartite(1, 3),
        graphs.CompleteBipartite(2, 3),
        graphs.CompleteBipartite(3, 3),
        graphs.Complete(2),
        graphs.Complete(3),
        graphs.Cycle(4),
        graphs.Cycle(5),
        graphs.Diamond(),
        graphs.Path(3),
        graphs.Path(4),
        graphs.ThreePrism(),
    ],
)
def test_2_3_sparse(graph):
    assert graph.is_sparse(2, 3)


@pytest.mark.parametrize(
    "graph",
    [
        graphs.Complete(4),
        graphs.CompleteBipartite(3, 4),
        graphs.CompleteBipartite(4, 4),
        graphs.K33plusEdge(),
        graphs.ThreePrismPlusEdge(),
    ],
)
def test_not_2_3_sparse(graph):
    assert not graph.is_sparse(2, 3)


@pytest.mark.parametrize(
    "graph",
    [
        graphs.Complete(2),
        graphs.Complete(3),
        graphs.CompleteBipartite(3, 3),
        graphs.Diamond(),
        graphs.ThreePrism(),
    ],
)
def test_2_3_tight(graph):
    assert graph.is_tight(2, 3)


@pytest.mark.parametrize(
    "graph",
    [
        graphs.Complete(4),
        graphs.CompleteBipartite(1, 3),
        graphs.CompleteBipartite(2, 3),
        graphs.CompleteBipartite(3, 4),
        graphs.CompleteBipartite(4, 4),
        graphs.Cycle(4),
        graphs.Cycle(5),
        graphs.K33plusEdge(),
        graphs.Path(3),
        graphs.Path(4),
        graphs.ThreePrismPlusEdge(),
    ],
)
def test_not_2_3_tight(graph):
    assert not graph.is_tight(2, 3)


@pytest.mark.parametrize(
    "graph",
    [
        graphs.Complete(2),
        graphs.Complete(3),
        graphs.CompleteBipartite(3, 3),
        graphs.Diamond(),
        graphs.ThreePrism(),
    ],
)
def test_min_rigid_in_d2(graph):
    assert graph.is_min_rigid(dim=2, combinatorial=True)
    assert graph.is_min_rigid(dim=2, combinatorial=False)


@pytest.mark.parametrize(
    "graph",
    [
        graphs.Complete(4),
        graphs.CompleteBipartite(1, 3),
        graphs.CompleteBipartite(2, 3),
        graphs.CompleteBipartite(3, 4),
        graphs.CompleteBipartite(4, 4),
        graphs.Cycle(4),
        graphs.Cycle(5),
        graphs.K33plusEdge(),
        graphs.Path(3),
        graphs.Path(4),
        graphs.ThreePrismPlusEdge(),
    ],
)
def test_not_min_rigid_in_d2(graph):
    assert not graph.is_min_rigid(dim=2, combinatorial=True)
    assert not graph.is_min_rigid(dim=2, combinatorial=False)


@pytest.mark.parametrize(
    "graph",
    [
        graphs.Complete(2),
        graphs.Complete(3),
        graphs.Complete(4),
        graphs.CompleteBipartite(3, 4),
        graphs.CompleteBipartite(4, 4),
        graphs.K33plusEdge(),
        graphs.ThreePrismPlusEdge(),
    ],
)
def test_globally_rigid_in_d2(graph):
    assert graph.is_globally_rigid(dim=2)


@pytest.mark.parametrize(
    "graph",
    [
        graphs.CompleteBipartite(1, 3),
        graphs.CompleteBipartite(2, 3),
        graphs.CompleteBipartite(3, 3),
        graphs.Cycle(4),
        graphs.Cycle(5),
        graphs.Diamond(),
        graphs.Path(3),
        graphs.Path(4),
        graphs.ThreePrism(),
    ],
)
def test_not_globally_in_d2(graph):
    assert not graph.is_globally_rigid(dim=2)


def test_min_rigid_subgraphs():
    G = Graph(
        [
            (0, 1),
            (1, 2),
            (2, 3),
            (3, 4),
            (4, 5),
            (5, 0),
            (0, 3),
            (1, 4),
            (2, 5),
            (0, "a"),
            (0, "b"),
            ("a", "b"),
        ]
    )
    assert [set(H) for H in G.min_rigid_subgraphs()] == [
        set([0, "a", "b"]),
        set([0, 1, 5, 3, 2, 4]),
    ] or [set(H) for H in G.min_rigid_subgraphs()] == [
        set([0, 1, 5, 3, 2, 4]),
        set([0, "a", "b"]),
    ]

    G = Graph([(0, 1), (1, 2), (2, 0), (3, 4), (4, 5), (5, 3)])
    assert [set(H) for H in G.max_rigid_subgraphs()] == [
        set([0, 1, 2]),
        set([3, 4, 5]),
    ] or [set(H) for H in G.max_rigid_subgraphs()] == [
        set([3, 4, 5]),
        set([0, 1, 2]),
    ]

    G = graphs.ThreePrism()
    min_subgraphs = G.min_rigid_subgraphs()
    assert len(min_subgraphs) == 2 and (
        min_subgraphs == [[0, 1, 2], [3, 4, 5]]
        or min_subgraphs == [[3, 4, 5], [0, 1, 2]]
    )


def test_max_rigid_subgraphs():
    G = Graph(
        [
            (0, 1),
            (1, 2),
            (2, 3),
            (3, 4),
            (4, 5),
            (5, 0),
            (0, 3),
            (1, 4),
            (2, 5),
            (0, "a"),
            (0, "b"),
            ("a", "b"),
        ]
    )
    assert [set(H) for H in G.max_rigid_subgraphs()] == [
        set([0, "a", "b"]),
        set([0, 1, 5, 3, 2, 4]),
    ] or [set(H) for H in G.max_rigid_subgraphs()] == [
        set([0, 1, 5, 3, 2, 4]),
        set([0, "a", "b"]),
    ]

    G = Graph([(0, 1), (1, 2), (2, 0), (3, 4), (4, 5), (5, 3)])
    assert [set(H) for H in G.max_rigid_subgraphs()] == [
        set([0, 1, 2]),
        set([3, 4, 5]),
    ] or [set(H) for H in G.max_rigid_subgraphs()] == [
        set([3, 4, 5]),
        set([0, 1, 2]),
    ]

    G = graphs.ThreePrism()
    G.delete_edge([4, 5])
    max_subgraphs = G.max_rigid_subgraphs()
    assert len(max_subgraphs) == 1 and max_subgraphs[0] == [0, 1, 2]


def test_str():
    G = Graph([[2, 1], [2, 3]])
    assert str(G) == "Graph with vertices [1, 2, 3] and edges [[1, 2], [2, 3]]"
    G = Graph([(chr(i + 67), i + 1) for i in range(3)] + [(i, i + 1) for i in range(3)])
    assert str(G) == (
        "Graph with vertices ['C', 1, 'D', 2, 'E', 3, 0] "
        "and edges [('C', 1), (1, 0), (1, 2), ('D', 2), (2, 3), ('E', 3)]"
    )
    G = Graph.from_vertices(["C", 1, "D", 2, "E", 3, 0])
    assert str(G) == "Graph with vertices ['C', 1, 'D', 2, 'E', 3, 0] and edges []"


def test_vertex_edge_lists():
    G = Graph([[2, 1], [2, 3]])
    assert G.vertex_list() == [1, 2, 3]
    assert G.edge_list() == [[1, 2], [2, 3]]
    G = Graph([(chr(i + 67), i + 1) for i in range(3)] + [(i, i + 1) for i in range(3)])
    assert set(G.vertex_list()) == set(["C", 1, "D", 2, "E", 3, 0])
    assert set(G.edge_list()) == set(
        [("C", 1), (1, 0), (1, 2), ("D", 2), (2, 3), ("E", 3)]
    )
    G = Graph.from_vertices(["C", 1, "D", 2, "E", 3, 0])
    assert set(G.vertex_list()) == set(["C", 2, "E", 1, "D", 3, 0])
    assert G.edge_list() == []


def test_adjacency_matrix():
    G = Graph()
    assert G.adjacency_matrix() == Matrix([])
    G = Graph([[2, 1], [2, 3]])
    assert G.adjacency_matrix() == Matrix([[0, 1, 0], [1, 0, 1], [0, 1, 0]])
    assert G.adjacency_matrix(vertex_order=[2, 3, 1]) == Matrix(
        [[0, 1, 1], [1, 0, 0], [1, 0, 0]]
    )
    assert graphs.Complete(4).adjacency_matrix() == Matrix.ones(4) - Matrix.diag(
        [1, 1, 1, 1]
    )
    G = Graph.from_vertices(["C", 1, "D"])
    assert G.adjacency_matrix() == Matrix.zeros(3)
    G = Graph.from_vertices_and_edges(["C", 1, "D"], [[1, "D"], ["C", "D"]])
    assert G.adjacency_matrix(vertex_order=["C", 1, "D"]) == Matrix(
        [[0, 0, 1], [0, 0, 1], [1, 1, 0]]
    )
    M = Matrix([[0, 1, 0], [1, 0, 1], [0, 1, 0]])
    assert G.from_adjacency_matrix(M).adjacency_matrix() == M


@pytest.mark.parametrize(
    "graph, gint",
    [
        [graphs.Complete(2), 1],
        [graphs.Complete(3), 7],
        [graphs.Complete(4), 63],
        [graphs.CompleteBipartite(3, 4), 507840],
        [graphs.CompleteBipartite(4, 4), 31965120],
        [graphs.ThreePrism(), 29327],
    ],
)
def test_integer_representation(graph, gint):
    assert graph.to_int() == gint
    assert Graph.from_int(gint).is_isomorphic(graph)
    assert Graph.from_int(gint).to_int() == gint
    assert Graph.from_int(graph.to_int()).is_isomorphic(graph)


def test_integer_representation_fail():
    with pytest.raises(ValueError):
        Graph([]).to_int()
    with pytest.raises(ValueError):
        M = Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]])
        G = Graph.from_adjacency_matrix(M)
        G.to_int()
    with pytest.raises(ValueError):
        Graph.from_int(0)
    with pytest.raises(TypeError):
        Graph.from_int(1 / 2)
    with pytest.raises(TypeError):
        Graph.from_int(1.2)
    with pytest.raises(ValueError):
        Graph.from_int(-1)


@pytest.mark.parametrize(
    "method, params",
    [
        ["is_rigid", []],
        ["is_min_rigid", []],
        ["is_redundantly_rigid", []],
        ["is_vertex_redundantly_rigid", []],
        ["is_k_vertex_redundantly_rigid", [2]],
        ["is_k_redundantly_rigid", [2]],
        ["is_globally_rigid", []],
        ["is_Rd_dependent", []],
        ["is_Rd_independent", []],
        ["is_Rd_circuit", []],
        ["is_Rd_closed", []],
        ["max_rigid_subgraphs", []],
        ["min_rigid_subgraphs", []],
    ],
)
def test_loops(method, params):
    with pytest.raises(LoopError):
        G = Graph([[1, 2], [1, 1], [2, 3], [1, 3]])
        func = getattr(G, method)
        func(*params)


def test_CompleteOnVertices():
    assert str(Graph.CompleteOnVertices([0, 1, 2, 3, 4, 5])) == str(graphs.Complete(6))
    assert Graph.CompleteOnVertices(
        ["a", "b", "c", "d", "e", "f", "g", "h"]
    ).is_isomorphic(graphs.Complete(8))
    assert Graph.CompleteOnVertices(["vertex", 1, "vertex_1", 3, 4]).is_isomorphic(
        graphs.Complete(5)
    )
    assert Graph.CompleteOnVertices(["vertex", 1]).is_isomorphic(graphs.Complete(2))
    assert Graph.CompleteOnVertices(["vertex"]).is_isomorphic(graphs.Complete(1))
    assert Graph.CompleteOnVertices(
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    ).is_isomorphic(graphs.Complete(20))


def test_check_edge_list():
    G = Graph.from_vertices_and_edges([1, 2, 3], [(1, 2), (2, 3)])
    G._check_edge((1, 2))
    G._check_edge([3, 2])
    G._check_edge_list([(1, 2), (2, 3)])
    G._check_edge_list([(1, 2)], [1, 2])
    G._check_edge_list([(2, 3)], [2, 3])
    with pytest.raises(ValueError):
        G._check_edge((1, 3))
    with pytest.raises(ValueError):
        G._check_edge((1, 4))
    with pytest.raises(ValueError):
        G._check_edge_list([(1, 2), (1, 3), (2, 3)])
    with pytest.raises(ValueError):
        G._check_edge_list([(1, 2), (2, 3)], [1, 2])
    with pytest.raises(TypeError):
        G._check_edge_list([(2,)])
    with pytest.raises(TypeError):
        G._check_edge_list([2, 3])
    with pytest.raises(TypeError):
        G._check_edge_list(["23"])


def test_check_edge_format_list():
    G = Graph.from_vertices_and_edges([1, 2, 3], [(1, 2), (2, 3)])
    G._check_edge_format((1, 3))
    G._check_edge_format([3, 1])
    G._check_edge_format_list([(1, 2), (1, 3)])
    G._check_edge_format_list([(1, 2), (1, 3), (2, 3)])
    with pytest.raises(ValueError):
        G._check_edge_format((1, 4))
    with pytest.raises(TypeError):
        G._check_edge_format_list([(2,)])
    with pytest.raises(TypeError):
        G._check_edge_format_list([2, 3])
    with pytest.raises(TypeError):
        G._check_edge_format_list(["23"])
    with pytest.raises(LoopError):
        G._check_edge_format([3, 3])
    with pytest.raises(LoopError):
        G._check_edge_format_list([(1, 1), (1, 3), (2, 3)])


def test_from_vertices_and_edges():
    G = Graph.from_vertices_and_edges([], [])
    assert G.vertex_list() == [] and G.edge_list() == []
    G = Graph.from_vertices_and_edges([0], [])
    assert G.vertex_list() == [0] and G.edge_list() == []
    G = Graph.from_vertices_and_edges([0, 1, 2, 3, 4, 5], [[0, 1]])
    assert G.vertex_list() == [0, 1, 2, 3, 4, 5] and G.edge_list() == [[0, 1]]
    G = Graph.from_vertices_and_edges([0, 1, 2], [[0, 1], [0, 2], [1, 2]])
    assert G.vertex_list() == [0, 1, 2] and G.edge_list() == [[0, 1], [0, 2], [1, 2]]
    G = Graph.from_vertices_and_edges(["a", "b", "c", "d"], [["a", "c"], ["a", "d"]])
    assert G.vertex_list() == ["a", "b", "c", "d"] and G.edge_list() == [
        ["a", "c"],
        ["a", "d"],
    ]
