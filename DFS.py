#!/usr/local/bin/python

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


#graph = {
#        'A': ['B', 'C'],
#        'B': ['A', 'D'],
#        'C': ['D', 'A'],
#        'D': ['E', 'B', 'C'],
#        'E': ['D', 'F'],
#        'F': ['E']
#        }

def depth_first_search(graph, start_node):
    visited = {}
    stack = []
    dfs = []

    for node in graph.keys():
        visited[node] = False

    stack.append(start_node)

    while(stack):
        print 'in stack', stack
        stack.pop()


def depth_first_search_copy(graph, start_node):
    visited = {}
    stack = []
    dfs = []

    for node in graph.keys():
        visited[node] = False
    stack.append(start_node)

    while(stack):
#        for node in stack:
        print 'stack : ', stack
        print '_' * 30
        current = stack.pop()
        visited[current] = True
        dfs.append(current)
        print 'CURRENT - ', current
        for adj in graph[current]:
            print '\t adj - ', adj
            if adj not in stack and visited[adj] == False:
#                if visited[adj] == False:
                stack.append(adj)

        print 'stack : ', stack
        print '_' * 30
        print '\t \t DFS : ', dfs

    return dfs

print depth_first_search_copy(graph, graph.keys()[0])
