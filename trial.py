from abc import ABC, abstractmethod


class Graph:
    def __init__(self, graph_dict=None, directed=False, weighted=False):
        super().__init__()
        if graph_dict == None:
            self.graph_dict = {}
        else:
            self.graph_dict = graph_dict
        self.directed = directed
        self.weighted = weighted

    def add_vertex(self, vertex):
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = list()

    # @abstractmethod
    def add_edge(self, edge):
        if len(edge) == 3:
            (vertex1, vertex2, weight) = tuple(edge)
            self.weighted = True
        elif len(edge) == 2:
            (vertex1, vertex2) = tuple(edge)
            weight = 0
            self.weighted = False
        else:
            print('Wrong edge format')
        if vertex1 in self.graph_dict and vertex2 in self.graph_dict:
            if self.directed:  # if directed -> the path is FROM vertex1 TO vertex2
                self.graph_dict[vertex1].append((vertex2, weight))
            else:  # if undirected, they are interchangeable
                self.graph_dict[vertex1].append((vertex2, weight))
                self.graph_dict[vertex2].append((vertex1, weight))
        else:
            print('You\'ve specified wrong edges')

    def vertices(self):
        return list(self.graph_dict.keys())

    def generate_edges(self):
        edges = {}
        undir_used_edges = list()
        for vertex in self.graph_dict:
            for neighbor in self.graph_dict[vertex]:
                curr_edge = vertex + neighbor[0]
                undir_used_edges.append(neighbor[0]+vertex)
                if self.directed:
                    VertexToNeighbor = '{} --> {}'.format(vertex, neighbor[0])
                else:
                    if curr_edge in undir_used_edges:
                        continue
                    VertexToNeighbor = '{} --- {}'.format(vertex, neighbor[0])
                if neighbor[1] == 0:
                    edges[VertexToNeighbor] = ''
                else:
                    edges[VertexToNeighbor] = neighbor[1]

        return edges

    def edges(self):
        return self.generate_edges()

    def weight_between_nodes(self, u, v):
        if

    def isAdjacent(self, v1, v2):  # checks whether the two given nodes are adjacent; for directed order matters
        if v1 not in self.graph_dict or v2 not in self.graph_dict:
            print('At least one of the vertices is not presented in the graph. False will be returned')
            return False
        elif str(v1)+' --> '+str(v2)in self.edges():
            return True
        elif str(v1)+' --- '+str(v2) in self.edges() or str(v2)+' --- '+str(v1) in self.edges():
            return True
        else:
            return False


# rewrite generate_edges so that the returned result is a dict, not a list


G = {
    'A': [('B', 6)],
    'B': [('C', 1)],
    'C': [('A', 3), ('D', 1)],
    'D': []
}


g = Graph(G, directed=True)
# g.add_vertex('A')
# g.add_vertex('B')
# g.add_vertex('C')
# g.add_vertex('D')
# g.add_vertex('E')
#
# g.add_edge(('A', 'D', 1))
# g.add_edge(('A', 'B', 6))
# g.add_edge(('D', 'B', 2))
# g.add_edge(('B', 'E', 2))
# g.add_edge(('B', 'C', 5))
# g.add_edge(('E', 'C', 5))
# g.add_edge(('D', 'E', 1))

print('vertices of g:', g.vertices())
print('edges of g:', g.edges())
print(g.isAdjacent('B', 'C'))
# print(g.graph_dict['D'])


