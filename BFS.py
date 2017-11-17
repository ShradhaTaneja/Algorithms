#!/usr/local/bin/python

# refer this if any doubts
# https://gist.github.com/daveweber/99ea4da41f42ac92cdbf
# https://gist.github.com/avrilcoghlan/8650958

#import queque

from queue import *
#graph = {'A': ['B', 'C', 'E'],
#         'B': ['A','D', 'E'],
#         'C': ['A', 'F', 'G'],
#         'D': ['B'],
#         'E': ['A', 'B','D'],
#         'F': ['C'],
#         'G': ['C']}

#graph = {
#        'A': ['B', 'D', 'C'],
#        'B': ['A', 'E'],
#        'C': ['A', 'F'],
#        'D': ['A', 'F'],
#        'E': ['B', 'F'],
#        'F': ['E', 'D', 'C']
#        }

graph = {
        '1': ['2', '4'],
        '2': ['3', '1'],
        '3': ['2', '4', '8', '9'],
        '4': ['1', '3', '5'],
        '5': ['4', '6', '7'],
        '6': ['5'],
        '7': ['5'],
        '8': ['3'],
        '9': ['3']
        }
def breadth_first_search(graph, start_node):
    visited = {}
    q = []
    bfs = []

    for node in graph.keys():
        visited[node] = False
    q.append(start_node)

    while(q):
        current = q.pop(0)
        for adj in graph[current]:
            if adj not in q and visited[adj] == False:
                q.append(adj)
        visited[current] = True
        bfs.append(current)
    return bfs

