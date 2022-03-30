from search import *
from collections import deque as dq
import math


class LocationGraph(ExplicitGraph):

    def __init__(self, nodes, locations, edges, starting_nodes, goal_nodes):
        self.nodes = nodes
        self.locations = locations
        self.edges = edges
        self._starting_nodes = starting_nodes
        self.goal_nodes = goal_nodes


    def starting_nodes(self):
        return self._starting_nodes

    def get_dist(self, a, b):
        node1_x, node1_y = self.locations[a]
        node2_x, node2_y = self.locations[b]
        return math.sqrt((node2_x - node1_x) ** 2 + (node2_y - node1_y) ** 2)


    def is_goal(self, node):
        return node in self.goal_nodes

    def _find_neihbours(self, node):
        neighbours = []
        for edge in self.edges:
            x,y = edge
            if x == node:
                neighbours.append(x)
            elif y == node:
                neighbours.append(y)
        return neighbours

    def outgoing_arcs(self, node):
        arcs = set()
        neighbours = self._find_neihbours(node)
        for i in neighbours:
            arcs.add(Arc(node,i,action=f"{node}->{i}",cost=self.get_dist(i,node)))
        return sorted(arcs)




graph = LocationGraph(nodes=set('ABC'),
                      locations={'A': (0, 0),
                                 'B': (3, 0),
                                 'C': (3, 4)},
                      edges={('A', 'B'), ('B','C'),
                             ('C', 'A')},
                      starting_nodes=['A'],
                      goal_nodes={'C'})


for arc in graph.outgoing_arcs('A'):
    print(arc)

for arc in graph.outgoing_arcs('B'):
    print(arc)

for arc in graph.outgoing_arcs('C'):
    print(arc)
