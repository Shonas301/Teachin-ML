# There are two main ways to represent a graph in CS:
# Adjacency Matrix, and Adjacency Lists
#
# Matrix Version:
#    A   B   C   D   E
# A  0   1   0   0   0
# B  1   0   1   0   0
# C  0   1   0   0   0
# D  0   0   0   0   1
# E  0   0   0   1   0
# Here each matrix represents a line between the two nodes, in this example it 
# is bidirectional, where each node has an edge between both if it exists.
# This is a terrible way to represent it in python, especially because arrays
# in python are not initialized with a set length and instead are "lists" 
# which can hold anything.
#
# Adjacency List:
# A: (B)
# B: (A, C)
# C: (B)
# D: (E) 
# E: (D)
# This is by far the best way to store it in python, and you should store it as
# A Dict of "Sets" so that no item is ever stored twice. Here is a good 
# implementation

from collections import defaultdict


class Graph(object):
    """ Graph data structure, undirected by default. """

    def __init__(self, connections, directed=False):
        self._graph = defaultdict(set)
        self._directed = directed
        self.add_connections(connections)

    def add_connections(self, connections):
        """ Add connections (list of tuple pairs) to graph """

        for node1, node2 in connections:
            self.add(node1, node2)

    def add(self, node1, node2):
        """ Add connection between node1 and node2 """

        self._graph[node1].add(node2)
        if not self._directed:
            self._graph[node2].add(node1)

    def remove(self, node):
        """ Remove all references to node """

        for n, cxns in self._graph.iteritems():
            try:
                cxns.remove(node)
            except KeyError:
                pass
        try:
            del self._graph[node]
        except KeyError:
            pass

    def is_connected(self, node1, node2):
        """ Is node1 directly connected to node2 """

        return node1 in self._graph and node2 in self._graph[node1]

    def find_path(self, node1, node2, path=[]):
        """ Find any path between node1 and node2 (may not be shortest) """

        path = path + [node1]
        if node1 == node2:
            return path
        if node1 not in self._graph:
            return None
        for node in self._graph[node1]:
            if node not in path:
                new_path = self.find_path(node, node2, path)
                if new_path:
                    return new_path
        return None

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))


