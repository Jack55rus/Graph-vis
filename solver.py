from abc import ABC, abstractmethod
import numpy as np

class path_finder(ABC):
    def __init__(self, G=None):
        super().__init__()
        if G == None:
            self.G = {}
        else:
            self.G = G
    @abstractmethod
    def find_shortest_path(self, start_node=None, target_node=None):
        pass

    @abstractmethod
    def calc_shortest_path(self):
        pass
    start_node = None
    target_node = None
    vertices = {} # dict of vertices and s.p. to them, be default = inf
    sp_set = {} # dict of vertices we kbow s.p. to
    P = {} # dict of predecessors


class Dijkstra(path_finder):
    def __init__(self):
        super().__init__()
    visited_nodes = list()

    def __init_nodes(self, nodes):
        for v in nodes:
            if v == self.start_node:
                self.vertices[v] = 0
            else:
                self.vertices[v] = np.inf

    def __extract_min(self):
        min = np.inf
        v_min = np.inf
        for v in self.vertices: # v = vertices, self.vertices[v] = distance
            if self.vertices[v] < min:
                min = self.vertices[v]
                v_min = v
        return self.vertices.pop(v_min), min

    def __relax(self, u, v, w):
        if self.vertices[v] > self.vertices[u] + w(u,v) # in class Graph we have to implement w(u,v) function

    def find_shortest_path(self,  start_node=None, target_node=None):
        while len(self.vertices) != 0:
            node, val = self.__extract_min()
            self.sp_set[node] = val


        

