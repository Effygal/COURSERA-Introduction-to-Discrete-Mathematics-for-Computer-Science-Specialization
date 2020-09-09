#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 14:58:50 2020

@author: effygal 
week3 notebook

"""

import networkx as nx
import pygraphviz as pgv
from nxpd import draw, nxpdParams
nxpdParams['show'] = 'ipynb'


G = nx.Graph()
G.add_edges_from([
        ('a', 'b', {'weight':2, 'label': 2}), 
        ('a', 'c', {'weight':3, 'label': 3}), 
        ('a', 'd', {'weight':1, 'label': 1}), 
        ('a', 'e', {'weight':3, 'label': 3}), 
        ('b', 'c', {'weight':4, 'label': 4}), 
        ('c', 'd', {'weight':5, 'label': 5}), 
        ('d', 'e', {'weight':4, 'label': 4}), 
        ('e', 'a', {'weight':1, 'label': 1})
    ])
draw(G, layout='circo')

T = nx.minimum_spanning_tree(G)
for e in T.edges():
    G[e[0]][e[1]]['color'] = 'blue'
draw(G, layout='circo')

import networkx as nx
import pygraphviz as pgv
from nxpd import draw, nxpdParams
nxpdParams['show'] = 'ipynb'


G = nx.Graph()
G.add_edges_from([(1, 'b'), (1, 'c'), (1, 'd'), (2, 'a'), (2, 'c'), (2, 'e'), (3, 'b'),
                  (3, 'c'), (3, 'd'), (4, 'a'), (4, 'e'), (5, 'a'), (5, 'e')])
    
if nx.bipartite.is_bipartite(G):
    left, right = nx.bipartite.sets(G)
    for v in left:
        G.node[v]['color'] = 'blue'
    for v in right:
        G.node[v]['color'] = 'green'
else:
    print("This graph is not bipartite")

draw(G, layout='circo')

M = nx.max_weight_matching(G)
print(M)
for v1, v2 in M.items():
    G[v1][v2]['color'] = 'red'
draw(G, layout='circo')
