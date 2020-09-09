#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 21:22:14 2020

@author: effygal
GraphTheory week2-Note
"""
"""
In this notebook, we'll implement a program that we'll solve the Guarini puzzle in blink of an eye!

Before starting to implement, let's agree on the following representation of a configuration. First, let's enumerate the eight essential cells of a 3x3 board as follows:


By a configuration we mean a placement of two white and two black knight on this board. We will represent it as a string of length eight. Its i-th symbol is equal to "*", if there is no knight in the i-th cell of the board. It is equal to "B" or "W", if the i-th cell contains a black or white knight, respectively. See an example below.

We now start creating the graph of all configurations. Below, we iterate through all possible strings of length 8 with two W's and two B's. For this, we iterate through all possible four indices of W's and B's (out of eight possible positions).


"""
import networkx as nx
import itertools as it

G = nx.Graph()

for wb_indices in it.permutations(range(8), 4):
    configuration = ['*'] * 8
    configuration[wb_indices[0]] = 'W'
    configuration[wb_indices[1]] = 'W'
    configuration[wb_indices[2]] = 'B'
    configuration[wb_indices[3]] = 'B'

    G.add_node("".join(configuration))
    
"""We then add edges to the graph. For this, we first fill in a list moves: moves[i] are the numbers of cells where a knight can move from the i-th cell."""
    
moves = [[] for _ in range(8)]
moves[0] = [4, 6]
moves[1] = [5, 7]
moves[2] = [3, 6]
moves[3] = [2, 7]
moves[4] = [0, 5]
moves[5] = [1, 4]
moves[6] = [0, 2]
moves[7] = [1, 3]

"""Adding edges to the graph:"""
for node in G.nodes():
    configuration = [c for c in node]

    for i in range(8):
        if configuration[i] != "*":
            for new_pos in moves[i]:
                if configuration[new_pos] != "*":
                    continue
                new_configuration = list(configuration)

                new_configuration[i] = "*"
                new_configuration[new_pos] = configuration[i]

                if not G.has_edge("".join(configuration), "".join(new_configuration)):
                    G.add_edge("".join(configuration), "".join(new_configuration))
                    
"""OK, the graph has been cooked! We can now analyze it. Let's first print its number of nodes, number of edges, and number of connected components."""

print(nx.number_of_nodes(G))
print(nx.number_of_edges(G))
print(nx.number_connected_components(G))

"""Well, the fact that the graph has two connected components is not surprising. The eight nodes of a 3x3 board form a cycle. Thus, one connected component contains all configurations where along this cycle two white knights are followed by two black knights, while the other connected components consists of all configurations where the white and black knights are interchanged.

"""
"""
Let’s now ensure that the configurations "W*B**W*B" and "B*B**W*W" are reachable from "W*W**B*B", while "W*B**B*W" is not.
"""

assert "W*B**W*B" in nx.node_connected_component(G, "W*W**B*B")
assert "B*B**W*W" in nx.node_connected_component(G, "W*W**B*B")
assert "W*B**B*W" not in nx.node_connected_component(G, "W*W**B*B")

"""The number of connected components of the resulting graph of configurations is not the only interesting property! We can now easily find an optimal (i.e., shortest) way of getting from one configuration to another one:

"""

print(" -> ".join(nx.shortest_path(G, "W*W**B*B", "B*B**W*W")))

import networkx as nx
import pygraphviz as pgv
from nxpd import draw, nxpdParams
nxpdParams['show'] = 'ipynb'


G = nx.DiGraph()
G.add_edges_from([('a', 'b'), ('b', 'c'), ('b', 'd'), ('d', 'c'), ('a', 'd')])
draw(G, layout='circo')

if nx.is_directed_acyclic_graph(G):
    print("Topological ordering of the nodes:", nx.topological_sort(G))
else:
    print("G contains a cycle, hence it cannot be topologically sorted.")
    
"""Topological ordering of the nodes: ['a', 'b', 'd', 'c']"""

draw(G, layout='dot')

"""Strongly Connected Components"""

import networkx as nx
import pygraphviz as pgv
from nxpd import draw, nxpdParams
nxpdParams['show'] = 'ipynb'


G = nx.DiGraph()
G.add_edges_from([('a', 'b'), ('b', 'c'), ('b', 'd'), ('d', 'c'), ('a', 'd'), ('e', 'd'), ('f', 'a'), ('b', 'f')])
draw(G, layout='circo')

print("Strongly connected components:")
#for scc in nx.strongly_connected_components(G)):
#    print()
    
import networkx as nx
import pygraphviz as pgv
from nxpd import draw, nxpdParams
nxpdParams['show'] = 'ipynb'

#G = nx.DiGraph([('f', 'e'), ('d', 'c'), ('a', 'b'), ('c', 'd'), ('c', 'f'), ('f', 'd'), ('b', 'a'), ('a', 'd'), ('d', 'a'), ('e', 'a'), ('b', 'f'), ('a', 'c'), ('d', 'b')])
G = nx.DiGraph([('a', 'b'), ('b', 'c'), ('c', 'e'), ('e', 'a'), ('a', 'd'), ('d', 'c'), ('c', 'a')])
draw(G, layout='circo')

if nx.is_eulerian(G):
    cycle = nx.eulerian_circuit(G)
    
    edge_number = 1
    for e in cycle:
        G[e[0]][e[1]]['label'] = str(edge_number)
        edge_number += 1
else:
    print("There is no Eulerian cycle in this graph")
    
draw(G, layout='circo')








